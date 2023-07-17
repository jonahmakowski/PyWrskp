import matplotlib.pyplot as plt

def draw_rocket():
    fig, ax = plt.subplots()

    # Draw the rocket components
    ax.add_patch(plt.Rectangle((0.4, 0), 0.2, 0.2, fill=True, color='blue'))  # Mk1 Command Pod
    ax.add_patch(plt.Rectangle((0.4, -0.05), 0.2, 0.05, fill=True, color='gray'))  # Heat Shield
    ax.add_patch(plt.Rectangle((0.4, -0.3), 0.2, 0.25, fill=True, color='white'))  # First-stage Fuel Tank
    ax.add_patch(plt.Rectangle((0.45, -0.55), 0.1, 0.25, fill=True, color='orange'))  # Solid Rocket Boosters
    ax.add_patch(plt.Circle((0.5, -0.7), 0.05, fill=True, color='red'))  # Liquid Fuel Engine
    ax.add_patch(plt.Rectangle((0.4, -1.0), 0.2, 0.1, fill=True, color='gray'))  # Landing Struts
    ax.add_patch(plt.Rectangle((0.4, 0.2), 0.2, 0.1, fill=True, color='black'))  # RCS Thruster Block
    ax.add_patch(plt.Polygon([[0.3, 0.2], [0.5, 0.2], [0.4, 0.35]], fill=True, color='black'))  # RCS Thruster
    ax.add_patch(plt.Circle((0.5, 0.35), 0.02, fill=True, color='yellow'))  # RCS Thruster Firing

    # Label the rocket components
    ax.text(0.5, 0.4, 'Mk1 Command Pod', ha='center', va='center', color='white')
    ax.text(0.5, -0.1, 'Heat Shield', ha='center', va='center', color='black')
    ax.text(0.5, -0.475, 'First-stage Fuel Tank', ha='center', va='center', color='black')
    ax.text(0.5, -0.8, 'Solid Rocket Boosters', ha='center', va='center', color='black')
    ax.text(0.5, -1.05, 'Liquid Fuel Engine', ha='center', va='center', color='black')
    ax.text(0.5, -1.15, 'Landing Struts', ha='center', va='center', color='black')
    ax.text(0.5, 0.25, 'RCS Thruster Block', ha='center', va='center', color='white')
    ax.text(0.47, 0.205, 'RCS Thruster', ha='center', va='center', color='white')
    ax.text(0.5, 0.37, 'RCS Thruster Firing', ha='center', va='center', color='black')

    # Set plot limits and remove axis
    ax.set_xlim(0, 1)
    ax.set_ylim(-1.2, 0.5)
    ax.axis('off')

    plt.show()

if __name__ == "__main__":
    draw_rocket()
    