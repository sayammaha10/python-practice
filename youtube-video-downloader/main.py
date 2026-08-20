import os
import tkinter as tk
from tkinter import filedialog
from yt_dlp import YoutubeDL


def download_video(url, save_dir):
    try:
        options = {
            "outtmpl": os.path.join(save_dir, "%(title)s.%(ext)s"),
            "format": "best"
        }

        with YoutubeDL(options) as ydl:
            ydl.download([url])

        print("\nDownload completed successfully.")
    except Exception as e:
        print(f"\nDownload failed: {e}")


def open_file_dialog():
    print("\nPlease select a folder to save the video.")

    folder = filedialog.askdirectory()

    if folder:
        print(f"Save location: {folder}")

    return folder


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    print("=" * 40)
    print("YouTube Video Downloader")
    print("=" * 40)

    video_url = input("\nEnter the YouTube video URL: ").strip()

    if video_url:
        save_dir = open_file_dialog()
        root.destroy()

        if save_dir:
            print("\nStarting download...")
            download_video(video_url, save_dir)
        else:
            print("\nNo folder selected. Please choose a folder to save the video.")
    else:
        print("Please enter a valid YouTube URL.")
