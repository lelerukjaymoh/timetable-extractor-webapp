from django.contrib import admin
from .models import Timetable, Year, Semester, Exam

admin.site.register(Timetable)
admin.site.register(Year)
admin.site.register(Semester)
admin.site.register(Exam)