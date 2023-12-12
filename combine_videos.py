import cv2
import numpy as np
import argparse
from moviepy.editor import VideoFileClip, clips_array, TextClip, CompositeVideoClip

# Function to add text to video frames
def add_text_to_video(video, text, pos):
    txt_clip = TextClip(text, fontsize=20, color='white', method='caption', size=(video.w, None))
    txt_clip = txt_clip.set_position(pos).set_duration(video.duration)
    return CompositeVideoClip([video, txt_clip])

def main():
    parser = argparse.ArgumentParser(description="Test")
    parser.add_argument("--video_name", type=str, help="Base video name")
    args = parser.parse_args()

    base_video = args.video_name
    video_list = [f'{base_video}']
    base_video = base_video.replace(".mp4", "")
    base_video_name = base_video.split("/")[-1]
    video_list.append(f'{base_video}_farneback_out.mp4')
    video_list.append(f'{base_video}_lucaskanade_dense_out.mp4')
    video_list.append(f'{base_video}_rlof_out.mp4')

    print(video_list)
    # Replace these paths with your video file paths
    video1 = VideoFileClip(video_list[0])
    video2 = VideoFileClip(video_list[1])
    video3 = VideoFileClip(video_list[2])
    video4 = VideoFileClip(video_list[3])

    # Resize videos to 320 x 240
    video1 = video1.resize(width=320, height=240)
    video2 = video2.resize(width=320, height=240)
    video3 = video3.resize(width=320, height=240)
    video4 = video4.resize(width=320, height=240)

    # Add text to each video
    video1_with_text = add_text_to_video(video1, "Base", ("left", "top"))
    video2_with_text = add_text_to_video(video2, "Video 2", ("right", "top"))
    video3_with_text = add_text_to_video(video3, "Video 3", ("left", "bottom"))
    video4_with_text = add_text_to_video(video4, "Video 4", ("right", "bottom"))

    # Combine videos in the four corners
    final_clip = clips_array([[video1_with_text, video2_with_text], [video3_with_text, video4_with_text]])

    # Write the final video file
    final_clip.write_videofile("combined_video_with_text.mp4", fps=24)

if __name__ == "__main__":
    main()
