from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.core import serializers

from .forms import uploadForm
import random
import json
import string
from .models import Timetable, Exam
from .extract import Extractor
from .serializers import ExtractorSerializer


def home(request):
    if request.method == 'POST':
        form = uploadForm(request.POST, request.FILES)
        if form.is_valid():
            fileForm = form.save(commit=False)
            fileForm.timetable_id = ''.join(random.choices(
                string.ascii_uppercase + string.digits, k=30))
            fileForm.save()
            print(fileForm.timetable_id)
            return redirect('extract/'+fileForm.timetable_id)
    else:
        form = uploadForm()
    return render(request, 'home.html', {'form': form})

def extract(request, timetable_id):
    file_path = Timetable.objects.get(timetable_id=timetable_id).timetable.path

    # Run extractor on file
    extractor = Extractor()

    # Loop over all identifiers 
    indentifiers = ['Y1S1', 'Y1S2', 'Y2S1',
                    'Y2S2', 'Y3S1', 'Y3S2', 'Y4S1', 'Y4S2']

    for identifier in indentifiers:
        extractor.get_data(file_path, identifier, timetable_id)

    return render(request, "extract.html", {"file_path": file_path, 'timetable_id': timetable_id})


# API views
@csrf_exempt
def exam_list(request, timetable_id):
    """
    List all exams.
    """
    exams = Exam.objects.filter(timetable_id=timetable_id)
    serializer = serializers.serialize('json', exams)
    print(serializer)
    serializer = ExtractorSerializer(exams, many=True)
    return JsonResponse(serializer.data, safe=False)