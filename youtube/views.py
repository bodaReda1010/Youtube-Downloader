from django.shortcuts import render
from pytube import YouTube
# Create your views here.

def download(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        res = request.POST.get('video')
        if url:
            yt = YouTube(url)
            if res == 'Audio':
                stream = yt.streams.get_audio_only()
                stream.download('downloads/')
            elif res == '1080p50':
                stream = yt.streams.get_highest_resolution()
                stream.download('downloads/')
            else:
                stream = yt.streams.get_by_resolution(resolution = res)
                stream.download('downloads/')
    return render(request,'index.html')