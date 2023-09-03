import cv2
from katna.video import Video

# Instantiate the video class
vd = Video()

# Load the video file
video_file = "path/to/your/video.mp4"

# Call the extract_frames_as_images method of video object
# The method accepts two parameters and returns a list of numpy 2D arrays which are images
keyframes = vd.extract_frames_as_images(video_file, num_frames=10)

# Save the extracted keyframes as images
for i, frame in enumerate(keyframes):
    cv2.imwrite(f"keyframe_{i}.png", frame)