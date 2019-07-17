from django.shortcuts import render
from api.models import Note
# Create your views here.


note = Note(title="First Note", body="This is certainly noteworthy")
note.save()
Note.objects.all()
