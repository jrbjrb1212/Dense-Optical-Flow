import cv2
import numpy as np
import argparse

def combine_videos(video_path: str, output_video_name: str, video_names: list):
    # Open the video capture object
    cap = cv2.VideoCapture(video_path)

    # Get video properties (assuming all videos have the same properties)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    # Create a video writer object
    combined_video = cv2.VideoWriter(output_video_name, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width * 2, height * 2))

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.resize(frame, (width // 2, height // 2))

        # Define positions for text
        positions = [
            (0, 0),                     # Top-left
            (width // 2, 0),            # Top-right
            (0, height // 2),           # Bottom-left
            (width // 2, height // 2)   # Bottom-right
        ]

        try:
            for i, pos in enumerate(positions):
                text = f"{video_names[i]}"  # Modify this text as needed
                x, y = pos
                frame_with_text = cv2.putText(frame.copy(), text, (x + 10, y + 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
                combined_video.write(frame_with_text)
        except:
            continue

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