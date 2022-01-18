from pytube import YouTube

link = input("Enter the link: ")
yt = YouTube(link)

print("Title: ", yt.title)
print("Number of views: ", yt.views)
print("Length of video: ", yt.length, " seconds")
print("Ratings: ", yt.rating)

print("Downloading....")
ys = yt.streams.get_highest_resolution()
ys.download()
print("Doanload completed!")
