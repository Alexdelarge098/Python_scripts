import os
import subprocess

def download_songs(playlist_url, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    command = ["spotdl", playlist_url, "--output", output_dir]
    subprocess.run(command, check=True)

if __name__ == "__main__":
    playlist_url = input("Enter the Spotify playlist URL: ")
    output_dir = input("Enter the output directory path: ")
    download_songs(playlist_url, output_dir)
