import pytube
link = "youtube_link"
yt = pytube.YouTube(link)
stream = yt.streams.get_highest_resolution()
stream.download()
