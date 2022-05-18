# Generated by Django 4.0.3 on 2022-04-15 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='notes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=100)),
                ('selectop', models.CharField(max_length=50)),
                ('des', models.TextField()),
                ('myfile', models.FileField(upload_to='NotesUpload')),
            ],
        ),
    ]
