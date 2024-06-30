from django.db import models

# Create your models here.

class Message(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(blank=True)
    message=models.TextField(max_length=1000)

class Topic(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Question(models.Model):
    title = models.CharField(max_length=255)
    link = models.URLField()
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='questions')

    def __str__(self):
        return self.title
