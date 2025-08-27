import yt_dlp
import os

video_url = input("Enter Link: ")
usr_dl_dir = input("Enter Download Directory (or press Enter for default): ")

dl_dir = usr_dl_dir if usr_dl_dir else os.getcwd()
os.makedirs(dl_dir, exist_ok=True)

# Set up the options for yt-dlp
ydl_opts = {
    'format': 'best',
    'outtmpl': os.path.join(dl_dir, '%(title)s.%(ext)s'),  # Output file name template
    'postprocessors': [{
        'key': 'FFmpegVideoConvertor',
        'preferedformat': 'mp4',
    }],
}

# Create a yt-dlp instance
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([video_url])
