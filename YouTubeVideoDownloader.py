from pytube import YouTube
from pytube.cli import on_progress

# def progress(stream, chunk, file_handle, bytes_remaining):
#     contentSize = d_video.filesize
#     size = contentSize - bytes_remaining

#     print('\r' + '[Download progress]:[%s%s]%.2f%%;' % (
#     '1' * int(size*20/contentSize), ' '*(20-int(size*20/contentSize)), float(size/contentSize*100)), end='')



link = input("ENter the url of the video to be downloaded: ")
yt = YouTube(link,on_progress_callback=on_progress)

# Video Title
print("Title of video is : ")
print(yt.title)

# THumbnail
print("THumbnail url of link is: "+yt.thumbnail_url)

# streams
print("Streams of video is : ")
videos = yt.streams.all()
video = list(enumerate(videos))
for i in video:
    print(i)
while True:
    d_input = int(input("Enter the desired option to download video:  "))
    d_video = videos[d_input]
    print("Video is downloading...")
    d_video.download()
    print(f"Video is downloaded ...and saved at{d_video.get_file_path()}")

    user_inp = input("Enter: ")
    if user_inp=="685":
        exit()
    else:
        continue

