def welcome_message():
    print("Congrats on finding a simple tool to download YouTube videos (without a Premium membership)")
    print("Initializing...")
    # Perform any necessary setup tasks here

def main():
    welcome_message()
    # Execute the main functionality of the program

if __name__ == "__main__":
    main()

# This is a quick Python script to download videos from YouTube without premium subscription

from pytube import YouTube
from yt_dlp import YoutubeDL
# import youtube_dl  - this is an installer that has a bug which surfaced as a change in the metadataRevel van
# served by YouTube in both youtube-dl and yt-dlp(the latter is the only one updated at this Point in Time


try:
    # Get the YouTube video URL from user input
    url = input("Enter the YouTube video URL: ")

    # Create a YouTube object using the provided link
    yt = YouTube(url)

    # Print the title and the number of views of the video

    print("Title:", yt.title)
    print("Views:", yt.views)

    # Download the video
    # This is the variable which declares the folder where the video will be downloaded
    download_folder = input(r'Enter the absolute folder path to download the video to, '
                            r'eg C:\users\yourname\YouTube_Downloads:  ')

    # Set options for video download
    options = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': f'{download_folder}/%(title)s.%(ext)s',
        'verbose': True
    }

    # Download the video to the specified folder
    print("Downloading video to specified folder...")
    with YoutubeDL(options) as ydl:
        ydl.download([url])

    yt.streams.get_highest_resolution().download(output_path=download_folder)
    print("Video downloaded successfully to the specified folder!")

except Exception as e:
    print("An error is preventing the completion of this operation:", str(e))
