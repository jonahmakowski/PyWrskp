import numpy as np
import matplotlib.pyplot as plt
import feat
from feat.utils import openface_AU_presence # AU ids
from feat.plotting import interpolate_aus # cubic easing interpolation
from feat.plotting import plot_face
from celluloid import Camera

def animate_aus():
    # Link AU ids to their descriptions; might be wrong? see:
    au_name_map = list(
        zip(
            openface_AU_presence,
            [
                "inner brow raiser",
                "outer brow raiser",
                "brow lowerer",
                "upper lid raiser",
                "cheek raiser",
                "lid tightener",
                "nose wrinkler",
                "upper lip raiser",
                "lip corner puller",
                "dimpler",
                "lip corner depressor",
                "chin raiser",
                "lip puckerer",
                "lip stretcher",
                "lip tightener",
                "lip pressor",
                "lips part",
                "jaw drop",
                "lip suck",
                "eyes closed",
            ],
        )
    )

    # Start all AUs at neutral
    starting_intensities = np.zeros((20, 20))

    # And eventually get to 3
    ending_intensities = np.eye(20) * 3

    # Define some animation settings
    fps = 15
    duration = 0.5
    padding = 0.25
    num_frames = int(np.ceil(fps * duration))

    # Add some padding frames so when the animation loops it pauses on the endpoints
    num_padding_frames = int(np.ceil(fps * padding))
    total_frames = (num_frames + num_padding_frames) * 2
    # Loop over each frame of the animation, plot a 4 x 5 grid of faces
    fig, axs = plt.subplots(4, 5, figsize=(12, 18))
    camera = Camera(fig)

    for frame_num in range(total_frames):
        for i, ax in enumerate(axs.flat):
            au_interpolations = interpolate_aus(
                start=starting_intensities[i, :],
                end=ending_intensities[i, :],
                num_frames=num_frames,
                num_padding_frames=num_padding_frames,
            )

            ax = plot_face(
                model=None,
                ax=ax,
                au=au_interpolations[frame_num],
                title=f"{au_name_map[i][0]}\n{au_name_map[i][1]}",
            )
        _ = camera.snap()

    # Create the animation
    animation = camera.animate()
    animation.save("all.gif", fps=fps)
