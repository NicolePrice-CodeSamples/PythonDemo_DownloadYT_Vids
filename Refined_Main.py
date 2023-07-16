import subprocess
import sys
import os
import time

def check_venv():
    project_path = os.path.abspath(os.path.dirname(__file__))
    venv_activate_path = os.path.join(project_path, "DevVenv", "Scripts", "activate.bat")

    if not os.path.exists(venv_activate_path):
        print("Virtual environment not found in the specified project path.")
        sys.exit(1)

    if not hasattr(sys, "real_prefix") and not (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
        print("Virtual environment not activated. Activating...")
        try:
            activate_cmd = f"\"{venv_activate_path}\""
            subprocess.check_call(activate_cmd, shell=True)
            print("Virtual environment activated successfully.")
        except subprocess.CalledProcessError:
            print("Failed to activate the virtual environment.")
            sys.exit(1)

def check_dependencies():
    try:
        import required_package
        print("All required packages are installed.")
    except ImportError:
        print("Some required packages are missing. Installing from requirements.txt...")
        try:
            subprocess.check_call(["pip", "install", "-r", "requirements.txt"])
            print("Required packages installed successfully.")
        except subprocess.CalledProcessError:
            print("Failed to install the required packages.")
            sys.exit(1)

def welcome_message():
    print("Welcome, I'm here to help you download any YouTube video to your desired directory, without a subscription!")
    print("Initializing...checking to see if you have all you need installed on your system to execute...")
    time.sleep(7)  # Add a 7-second pause here
    # Perform any necessary setup tasks here

def main():
    welcome_message()  # Moved this call to the beginning of the main() function
    check_venv()
    check_dependencies()
    # Execute the main functionality of the program
    # Rest of your YouTube video download code or other functionality here

#  This next step determines if the program is triggered via the main, or if it is initiated from another function
if __name__ == "__main__":
    main()

    #  This next step determines if the program is triggered via the main, or if it is initiated from another function
    if __name__ == "__main__":
        main()
        # Execute the main functionality of the program

    #  This next step determines if the program is triggered via the main, or if it is initiated from another function
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
