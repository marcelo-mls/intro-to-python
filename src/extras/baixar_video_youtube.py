# pip install pytube
from pytube import YouTube

# insira o link do video abaixo
link = YouTube('https://www.youtube.com/watch?v=uMQb9LCNGxs')
video = link.streams.get_highest_resolution()
video.download()
