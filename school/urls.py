from django.urls import path
from . import views


urlpatterns = [
    path("", views.index),
    path("teacher/", views.teacher_form, name="teacher_form"),
    path("teacher/<int:pk>", views.teacher_edit, name="teacher_edit"),
    path("teacher_delete/<int:pk>", views.teacher_delete, name="teacher_delete"),
    path("teachers/", views.teachers, name="teachers"),
    path("subject/", views.subject_form, name="subject_form"),
    path("subjects/", views.subjects, name="subjects"),
    path("group/", views.group_form, name="group_form"),
    path("groups/", views.groups, name="groups"),
    path("student/", views.student_form, name="student_form"),
    path("student/<int:pk>", views.student_edit, name="student_edit"),
    path("student_delete/<int:pk>", views.student_delete, name="student_delete"),
    path("students/", views.students, name="students"),
    path("stud_group/", views.add_student, name="add_student"),
    path("stud_groups/", views.stud_groups, name="stud_groups"),
]
