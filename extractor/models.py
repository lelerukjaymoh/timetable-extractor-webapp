from django.db import models
import random
import string

class Timetable(models.Model):
    timetable = models.FileField(upload_to='timetables/')
    timetable_id = models.CharField(max_length=50)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.timetable_id)


class Year(models.Model):
    year = models.IntegerField()

    def __str__(self):
        return str(self.year)

class Semester(models.Model):
    year = models.ForeignKey(Year, on_delete=models.CASCADE, related_name='semesters')
    sem = models.IntegerField()

    def __str__(self):
        return str(self.sem)    

class Exam(models.Model):
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, related_name='exams')
    timetable_id = models.CharField(max_length=50)
    exam_no = models.IntegerField()
    unit_name = models.CharField(max_length=100)
    invigilator = models.CharField(max_length=100)
    venue = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    time = models.CharField(max_length=100)

    def __str__(self):
        return self.unit_name
