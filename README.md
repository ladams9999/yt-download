# Youtube Downloader #
---
This is a tool to download Youtube videos.
---
A lot of the overhead in this repo is because I usually run my projects in a Docker container.  There's no reason you couldn't just install the packages in `requirements.txt` and then run `app/yt_download.py` directly.

My usage is to build the image once, then run the container and connect a terminal when I need to use it, which is handled by `yt_download.sh`:

## Build the image
You should only need to do this step once, unless you update to a newer version of code.

```docker build -t yt_downloader .```

## Run the image and connect
```yt_download.sh```

```yt_download.sh <download directory>```

## Downloading a video

```python yt_download.py <youtube url>```

Use help to get additional args:

```python yt_download.py -h```
