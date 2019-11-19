from django.urls import path
from . import views

urlpatterns = [
    path('student/list/', views.student_list, name='student_list'),
    path('student/<int:pk>/', views.student_detail, name="student_detail"),
    path('student/new', views.new_student, name='new_student'),
    path('student/<int:pk>/edit/', views.student_edit, name='student_edit'),
]