from django.shortcuts import render
from .models import Podcast, Document
# Create your views here.


def showtemplate(request):
    podcast_list = Podcast.objects.all()
    context = {'podcast_list': podcast_list}
    return render(request, 'podcast_index.html', context)


def showfile(request):
    book_path = "podcast_file1.txt"
    with open(book_path, 'rt') as f:
        text = f.read()
    print(text)
    context = {'podcastFile_list': text}
    return render(request, 'podcast/show.html', context)


def uploadFile(request):
    if request.method == "POST":
        # Fetching the form data
        fileTitle = request.POST["fileTitle"]
        uploadedFile = request.FILES["uploadedFile"]

        # Saving the information in the database
        document = Document(
            title=fileTitle,
            uploadedFile=uploadedFile,
        )
        document.save()

    documents = Document.objects.all()

    return render(request, "podcast/upload_file.html", context={
        "files": documents,
    })


def uploadShow(request):
    if request.method == "POST":
        # Fetching the form data
        fileTitle = request.POST["fileTitle"]
        uploadedFile = request.FILES["uploadedFile"]
        str = uploadedFile.read().decode('utf-8')
        print(str)
        #print(uploadedFile.read().decode('utf-8'))
        #print(uploadedFile.read())
        #print(type(uploadedFile.read()))

    return render(request, "podcast/upload_show.html", context={
        "file_context": str,
    })
