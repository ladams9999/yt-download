#!/bin/sh
#
# yt_download.sh - Download YouTube videos using Dockerized yt_downloader
#
# Usage:
#   ./yt_download.sh [DOWNLOAD_DIR]
#
# Arguments:
#   DOWNLOAD_DIR   Optional. Directory where videos will be downloaded.
#                  If not provided, defaults to ./downloads in the script's directory.
#
# Description:
#   This script creates the download directory if it doesn't exist,
#   then runs a Docker container (yt_downloader) with the directory mounted
#   at /downloads for storing downloaded videos.

if [ -n "$1" ]; then
    download_dir="$(cd "$(dirname "$1")" && pwd)/$(basename "$1")"
else
    script_dir="$(cd "$(dirname "$0")" && pwd)"
    download_dir="$script_dir/downloads"
fi

if [ ! -d "$download_dir" ]; then
    echo "Creating directory: $download_dir"
    mkdir -p "$download_dir" || { echo "Failed to create directory: $download_dir"; exit 1; }
fi

docker run -it --mount type=bind,src="$download_dir",dst=/downloads yt_downloader bash
