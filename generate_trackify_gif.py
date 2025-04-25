import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import os

# Ensure 'static' folder exists
os.makedirs('static', exist_ok=True)

# Setup figure
fig, ax = plt.subplots(figsize=(19.2, 10.8), dpi=100)  # 1920x1080 resolution (16:9 HD)
ax.set_xlim(0, 10)
ax.set_ylim(-2, 2)
ax.set_facecolor('#191414')  # Spotify dark background
plt.axis('off')
fig.tight_layout(pad=0)
fig.patch.set_facecolor('#191414')

# Colors
spotify_green = '#1DB954'
dark_green = '#0A3D21'

# Grid lines for futuristic effect (very subtle)
num_grid_lines = 12
grid_opacity = 0.05
horizontal_grid = [ax.axhline(y=y, color=spotify_green, alpha=grid_opacity, linestyle='-', linewidth=0.5) 
                  for y in np.linspace(-2, 2, num_grid_lines)]
vertical_grid = [ax.axvline(x=x, color=spotify_green, alpha=grid_opacity, linestyle='-', linewidth=0.5) 
                for x in np.linspace(0, 10, num_grid_lines)]

# Particles
particles_count = 80  # Increased for more variation
particles = ax.scatter([], [], s=3, color=spotify_green, alpha=0.0)

# Parameters for perfect loop
total_frames = 180  # 6 seconds at 30fps

# Initialize
def init():
    particles.set_offsets(np.empty((0, 2)))
    return [particles]

# Generate fixed particle positions for perfect looping
np.random.seed(42)  # Fixed seed for reproducibility
# Generate more positions than needed, so we can select the best ones
fixed_positions_x = np.random.uniform(0, 10, particles_count * 2)
fixed_positions_y = np.random.uniform(-2, 2, particles_count * 2)

# Filter positions to ensure good spacing (minimal scattering)
min_distance = 0.4  # Minimum distance between particles
selected_positions = []

for i in range(len(fixed_positions_x)):
    pos = (fixed_positions_x[i], fixed_positions_y[i])
    # Check if this position is far enough from all selected positions
    too_close = False
    for sel_pos in selected_positions:
        dist = np.sqrt((pos[0] - sel_pos[0])**2 + (pos[1] - sel_pos[1])**2)
        if dist < min_distance:
            too_close = True
            break
    if not too_close and len(selected_positions) < particles_count:
        selected_positions.append(pos)

# Convert to numpy arrays
fixed_positions_x = np.array([p[0] for p in selected_positions])
fixed_positions_y = np.array([p[1] for p in selected_positions])

# Create staggered appearance/disappearance timing
np.random.seed(100)  # Different seed for timing variation
# Create timing offsets for each particle (when they appear/disappear)
appearance_offsets = np.random.uniform(0, 0.5, particles_count)  # Offsets between 0-0.5
disappearance_offsets = np.random.uniform(0.5, 1.0, particles_count)  # Offsets between 0.5-1.0
duration_factors = np.random.uniform(0.3, 0.7, particles_count)  # How long each particle stays visible

# Animate function
def animate(frame):
    # Perfect loop using normalized frame
    normalized_frame = frame / total_frames
    loop_phase = 2 * np.pi * normalized_frame
    
    # Individual particle animations (using fixed positions)
    particle_x = fixed_positions_x
    particle_y = fixed_positions_y
    
    # Individual alpha values with staggered appearances
    alpha_values = np.zeros(particles_count)
    sizes = np.zeros(particles_count)
    
    for i in range(particles_count):
        # Calculate individual particle lifecycle
        particle_phase = (normalized_frame + appearance_offsets[i]) % 1.0
        
        # Determine visibility based on lifecycle phase
        if particle_phase < duration_factors[i]:
            # Fade in during first 20% of visibility duration
            fade_in_portion = 0.2 * duration_factors[i]
            # Fade out during last 20% of visibility duration
            fade_out_start = duration_factors[i] - 0.2 * duration_factors[i]
            
            if particle_phase < fade_in_portion:
                # Fading in
                alpha = particle_phase / fade_in_portion
            elif particle_phase > fade_out_start:
                # Fading out
                alpha = (duration_factors[i] - particle_phase) / (duration_factors[i] - fade_out_start)
            else:
                # Fully visible with some variation
                alpha = 0.7 + 0.3 * np.sin(4 * np.pi * particle_phase)
                
            # Apply base alpha level and random variation
            alpha_values[i] = alpha * (0.3 + 0.3 * np.sin(loop_phase + i * 0.2))
            
            # Size also follows the visibility pattern
            base_size = 2 + np.sin(loop_phase) * 0.8
            sizes[i] = base_size * (0.8 + 0.4 * alpha)
        else:
            # Particle is invisible during this phase
            alpha_values[i] = 0
            sizes[i] = 0
    
    particles.set_offsets(np.c_[particle_x, particle_y])
    particles.set_sizes(sizes)
    particles.set_alpha(alpha_values)
    particles.set_color(spotify_green)
    
    return [particles]

# Generate and save the GIF
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=total_frames, 
                             interval=50, blit=True)
                             
# Higher fps for smoother animation
ani.save('static/bg.gif', writer='pillow', fps=30, dpi=100)
print("Minimalist Spotify-themed animation with staggered particles generated successfully at 'static/bg.gif'")
