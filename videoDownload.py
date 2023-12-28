from pytube import YouTube
import tkinter as tk
from tkinter import filedialog


def download_video(url, save_path):
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(progressive=True, file_extension="mp4")
        highest_res_stream = stream.get_highest_resolution()
        highest_res_stream.download(output_path=save_path)
    except Exception as e:
        print(e)


def open_file_ui():
    folder = filedialog.askdirectory()
    if folder:
        print(f'Selected folder path: {folder}')

    return folder


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    video_url = input("Give the URL of the Youtube URL: ")
    save_dir = open_file_ui()

    if not save_dir:
        print("Invalid location to save.")
    else:
        print("Initiating download....")
        download_video(video_url, save_dir)
        print("Completed Download!!! ")
