from django.contrib import admin
from .models import Message,Topic,Question
# Register your models here.

admin.site.register(Message)
admin.site.register(Topic)
admin.site.register(Question)
