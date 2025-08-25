import cv2
import os

# Change these values to match your setup
frames_folder = "./renders/frames_to_video_tester"  # folder containing your rendered frames
output_file = os.path.join(frames_folder, "animation.mp4")  # save video in same folder
frame_rate = 30  # frames per second

# Collect and sort all image files in the folder
frames = [f for f in os.listdir(frames_folder) if f.endswith((".png", ".jpg", ".jpeg", ".bmp"))]
frames.sort()  # assumes frames are numbered sequentially

if not frames:
    raise ValueError("No image frames found in the specified folder.")

# Read the first frame to get dimensions
first_frame = cv2.imread(os.path.join(frames_folder, frames[0]))
height, width, layers = first_frame.shape

# Define the video writer (MP4 with H.264 codec)
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
video = cv2.VideoWriter(output_file, fourcc, frame_rate, (width, height))

# Write each frame to the video
for frame_name in frames:
    frame_path = os.path.join(frames_folder, frame_name)
    frame = cv2.imread(frame_path)
    video.write(frame)

video.release()
print(f"Video saved as {output_file}")
