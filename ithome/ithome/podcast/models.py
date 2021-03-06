from django.db import models
from django.contrib import admin
# Create your models here.


class Podcast(models.Model):
    podcast_name = models.CharField(max_length=20)  # 攤販的名稱

    def __str__(self):
        return self.podcast_name


@admin.register(Podcast)
class PodcastAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Podcast._meta.fields]


class Document(models.Model):
    title = models.CharField(max_length=200)
    uploadedFile = models.FileField(upload_to="Uploaded_Files/")
    dateTimeOfUpload = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'dateTimeOfUpload')
