from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip


def add_text_to_video_segments(input_video, output_video, video_names):
    # Load the video clip
    clip = VideoFileClip(input_video)

    # Calculate dimensions of each segment
    width, height = clip.size
    segment_width = width // 2
    segment_height = height // 2

    # Create text clips for each segment
    text_clips = []
    for i, name in enumerate(video_names):
        text = TextClip(name, fontsize=30, color="white")
        text = text.set_position(("left", "top")).set_duration(clip.duration)
        text = text.set_start((i % 2) * segment_width, (i // 2) * segment_height)
        text_clips.append(text)

    # Composite text clips on the video
    composite_texts = CompositeVideoClip(text_clips)
    result = CompositeVideoClip([clip, composite_texts])

    # Save the result
    result.write_videofile(output_video, codec="libx264", fps=clip.fps)


<<<<<<< HEAD
    # Release capture object
    cap.release()

    # Release the video writer object
    combined_video.release()

def main():
    parser = argparse.ArgumentParser(description="Test")
    parser.add_argument("--video_name", type=str, help="Base video name")
    args = parser.parse_args()

    base_video_path = args.video_name
    video_names = ["base", "farneback", "lucas_kanade", "rlof"]

    combine_videos(base_video_path, "videos/test_w_text.mp4v", video_names)

if __name__ == "__main__":
    main()
=======
# Usage
video_names = ["base", "farneback", "lucas_kanade", "rlof"]
add_text_to_video_segments(
    "videos/test.mp4", "videos/test_w_text.mp4", video_names
)
>>>>>>> 4eb6166 (timing analysis)
