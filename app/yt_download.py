from argparse import ArgumentParser
import os
from pytubefix import YouTube
from pytubefix.cli import on_progress 


def yt_download(url:str, save_dir:str, audio_only:bool=False, verbose:bool=True):
    """_summary_

    Args:
        url (str): _description_
        path (str): _description_
        audio_only (bool, optional): _description_. Defaults to False.
        verbose (bool, optional): _description_. Defaults to True.
    """
    yt = YouTube(url, on_progress_callback=on_progress)
    if verbose:
        print(yt.title)

    if audio_only:
        if verbose:
            print("Downloading audio only")
        ys = yt.streams.get_audio_only()
    else:
        if verbose:
            print("Downloading video")
        ys = yt.streams.get_highest_resolution()
    ys.download(save_dir)


if __name__ == "__main__":
    parser = ArgumentParser(description="Download from YouTube")
    parser.add_argument("URL", help="YouTube video URL")
    parser.add_argument("-a", "--audio", action="store_true", default=False, help="Download audio only")
    parser.add_argument("--save-dir", default="/downloads", help="Directory to save the downloaded file")
    args = parser.parse_args()

    url = args.URL
    audio_only = args.audio
    save_dir = args.save_dir

    if not os.access(save_dir, os.W_OK):
        raise Exception(f"Downloads directory {save_dir} is not writable")
    
    try:
        yt_download(url, save_dir, audio_only=audio_only)
    except Exception as e:
        print(f"Error downloading video: {e}")

    print("Done!")
