import numpy as np
import cv2
import sys
import argparse


def dense_optical_flow(method, video_path, output_path, params=[], to_gray=False):
    cap = cv2.VideoCapture(video_path)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    ret, old_frame = cap.read()
    frames_itered = 1
    next_ten = .1
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

    hsv = np.zeros_like(old_frame)
    hsv[..., 1] = 255

    if to_gray:
        old_frame = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)
    while True:
        frames_itered+=1
        print(f"frames_itered: {frames_itered}")
        if frames_itered / total_frames > next_ten:
            print(f"Finished {next_ten * 100}% of frames")
            next_ten += 0.1
        ret, new_frame = cap.read()
        frame_copy = new_frame
        if not ret:
            break

        if to_gray:
            new_frame = cv2.cvtColor(new_frame, cv2.COLOR_BGR2GRAY)

        flow = method(old_frame, new_frame, None, *params)

        mag, ang = cv2.cartToPolar(flow[..., 0], flow[..., 1])
        hsv[..., 0] = ang * 180 / np.pi / 2
        hsv[..., 2] = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX)
        bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

        # Write the frame to the output video
        out.write(bgr)

        # cv2.imshow("frame", frame_copy)
        # cv2.imshow("optical flow", bgr)
        k = cv2.waitKey(25) & 0xFF
        if k == 27:
            break

        old_frame = new_frame

    # Release everything when finished
    cap.release()
    out.release()
    cv2.destroyAllWindows()


def main():
    parser = argparse.ArgumentParser(description="Test")
    parser.add_argument(
        "--algorithm",
        metavar="N",
        type=str,
        help="an integer for the accumulator",
    )
    parser.add_argument(
        "--video_path",
        type=str,
        help="sum the integers (default: find the max)",
    )
    args = parser.parse_args()
    algorithm = args.algorithm
    video_path = args.video_path
    method = None

    if algorithm == "lucaskanade_dense":
        method = cv2.optflow.calcOpticalFlowSparseToDense
        frames = dense_optical_flow(
            method,
            video_path,
            video_path.replace(".mp4", "") + "_out.mp4",
            [],
            to_gray=True,
        )
    elif algorithm == "farneback":
        method = cv2.calcOpticalFlowFarneback
        pyramid_scale = 0.5
        levels = 3
        window_sz = 25
        iterations = 3
        poly_n = 5
        poly_sigma = 1.2
        flags = 0
        params = [
            pyramid_scale,
            levels,
            window_sz,
            iterations,
            poly_n,
            poly_sigma,
            flags,
        ]  # default Farneback's algorithm parameters
        frames = dense_optical_flow(method, video_path, params, to_gray=True)
    elif algorithm == "rlof":
        method = cv2.optflow.calcOpticalFlowDenseRLOF
        frames = dense_optical_flow(method, video_path, [], to_gray=False)
    else:
        print("Algorithm not found")


if __name__ == "__main__":
    main()
