from rest_framework import serializers
from .models import Exam

class ExtractorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = ['semester', 'timetable_id', 'exam_no', 'unit_name', 'invigilator', 'venue', 'date', 'time']
        depth = 1