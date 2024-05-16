from pytube import YouTube
url = input("Enter your url: ")

yt = YouTube(url)

print("Title: ", yt.title)

# Video Description
print("Description: ", yt.description)

# Thumbnail URL for the video
print("Thumbnail URL: ", yt.thumbnail_url)

# Video length is sec
print("Video Length: ", yt.length)

# Views
print("Views: ", yt.views)