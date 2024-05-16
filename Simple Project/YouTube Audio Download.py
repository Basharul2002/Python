from pytube import YouTube
url = input("Enter your url: ")

yt = YouTube(url)

audio = yt.streams.get_audio_only()

# Audio download
audio.download()


print(yt.title, " has been downloaded")