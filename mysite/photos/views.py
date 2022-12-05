from django.shortcuts import render, redirect
from pytube import YouTube
from django.http import HttpResponse
from .forms import transcriptForm
from .models import transcript
import speech_recognition as sr
import wave, math, contextlib
import speech_recognition as sr
from moviepy.editor import AudioFileClip


# Create your views here.
def index(request):
   return HttpResponse('hello world!')

def audio_conversion(request):
    linkdocuments = transcript.objects.all()
    #rank = Document.objects.latest('id')
    #print(rank)
    for obj in linkdocuments:
        baseurls = obj.url
        tittle = obj.tittle
        #print(rank)
    print(baseurls)
    print(tittle)
    try:
        yt = YouTube(baseurls)
    except:
        print("Connection Error")
    yt.streams.filter(file_extension='mp4')
    stream = yt.streams.get_by_itag(139)
    stream.download('',"./media/video/test.mp4")

    #src = "./media/video/test.mp4"
    #dst = "./media/video/test.wav"

    transcribed_audio_file_name = "./media/video/test.wav"
    zoom_video_file_name = "./media/video/test.mp4"

    audioclip = AudioFileClip(zoom_video_file_name)
    audioclip.write_audiofile(transcribed_audio_file_name)
    with contextlib.closing(wave.open(transcribed_audio_file_name,'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)
        total_duration = math.ceil(duration / 60)
        r = sr.Recognizer()
    file1 = open("./media/file/sample.txt","w")
    file1.truncate(0)
    file1.close()
    for i in range(0, total_duration):
        with sr.AudioFile(transcribed_audio_file_name) as source:
            audio = r.record(source, offset=i*60, duration=60)
            with open("./media/file/sample.txt", "a") as f:
                f.write(r.recognize_google(audio))
                print(r.recognize_google(audio))
                f.write(" ")
            f.close()
                
    

    return render(request, 'file.html', { 'linkdocuments': linkdocuments })

def file_upload(request):
    if request.method == 'POST':
        form = transcriptForm(request.POST, request.FILES)
        if form.is_valid():
            #func_obj = form
            #func_obj.sourceFile = form.cleaned_data['sourceFile']
            form.save()
            #print(form.Document.document)
            #form.save()
            return redirect('audio_conversion')
    else:
        form = transcriptForm()
    return render(request, 'home.html', {
        'form': form
    })