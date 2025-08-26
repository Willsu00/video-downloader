# Video Downloader Script
This Downloader script relies on yt-dlp python library and ffmpeg. This script works on most website besides YouTube if not signed in. It will download as .mp4 format to the specified directory or the script directory if no specified directory is entered.

### Requirements:
- Python 3.7+
- ```ffmpeg```
- ```yt-dlp``` (must be available in system path)

### Install requirements:
**yt-dlp**
```
pip install yt-dlp
```
**ffmpeg**
Download and install ffmpeg from https://ffmpeg.org/download.html
* Linux (Deb/Ubuntu)
``` sudo apt update && sudo apt install ffmpeg```
* macOS
``` brew install ffmpeg ```

### How to run:
1. Run using python:
```
python vd-dl.py
```
> Try use ```python3``` if the command doesn't work
2. Enter video link
3. Enter download directory (or leave blank to save to the script's directory)

26/08/25

