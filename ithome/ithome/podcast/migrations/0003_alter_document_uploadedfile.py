# Generated by Django 4.0.4 on 2022-04-18 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('podcast', '0002_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='uploadedFile',
            field=models.FileField(upload_to='Uploaded_Files/'),
        ),
    ]