from django.contrib import admin
from .models import TrackData,QuestionData,ChoiceData
# Register your models here.
admin.site.register(TrackData)
admin.site.register(QuestionData)
admin.site.register(ChoiceData)
