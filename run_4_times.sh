# Run to generate dense optical flow videos for each tested video and a timing report

# Lucaskanade 
python3 openCV_impl.py --algorithm lucaskanade_dense --video_path videos/khaled.mp4 --timing True &
python3 openCV_impl.py --algorithm lucaskanade_dense --video_path videos/beach_people.mp4 --timing True &
python3 openCV_impl.py --algorithm lucaskanade_dense --video_path videos/dutch_traffic.mp4 --timing True &

# Farneback
python3 openCV_impl.py --algorithm farneback --video_path videos/dutch_traffic.mp4 --timing True &
python3 openCV_impl.py --algorithm farneback --video_path videos/khaled.mp4 --timing True &
python3 openCV_impl.py --algorithm farneback --video_path videos/beach_people.mp4 --timing True &

# Rlof
python3 openCV_impl.py --algorithm rlof --video_path videos/dutch_traffic.mp4 --timing True &
python3 openCV_impl.py --algorithm rlof --video_path videos/khaled.mp4 --timing True &
python3 openCV_impl.py --algorithm rlof --video_path videos/beach_people.mp4 --timing True 
