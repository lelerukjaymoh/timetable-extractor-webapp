from django.urls import path
from extractor import views

urlpatterns = [
    path('', views.home, name='home'),
    path('extract/<str:timetable_id>', views.extract, name='extract'),
    path('api/v1/exams/<str:timetable_id>', views.exam_list, name='exam_list'),
]
