import argparse
from moviepy.editor import VideoFileClip
import PIL
PIL.Image.ANTIALIAS = PIL.Image.LANCZOS

def downgrade_video(input_file, frame_rates=[5, 10, 15, 20, 25], widths=[640, 768, 1024], duration=None):
    clip = VideoFileClip(input_file)
    
    # Truncate the video to the specified duration if provided
    if duration:
        clip = clip.subclip(0, duration)
    
    for frame_rate in frame_rates:
        for width in widths:
            output_file = f"{input_file.split('.')[0]}_fr_{frame_rate}_w_{width}.mp4"
            clip_resized = clip.resize(height=int(clip.size[1] * width / clip.size[0]))
            clip_resized.write_videofile(output_file, fps=frame_rate)
            print(f"Created {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Downgrade video script.')
    parser.add_argument('input_file', type=str, help='Input video file.')
    parser.add_argument('--frame-rates', type=int, nargs='+', default=[10, 15],
                        help='Frame rates for downgraded videos.')
    parser.add_argument('--widths', type=int, nargs='+', default=[512,640],
                        help='Widths for downgraded videos.')
    parser.add_argument('--duration', type=int, help='Duration to which video should be truncated (in seconds).', default=None)

    args = parser.parse_args()
    downgrade_video(args.input_file, args.frame_rates, args.widths, args.duration)
