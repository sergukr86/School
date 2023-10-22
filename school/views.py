from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import SubjectForm, TeacherForm, StudentForm, GroupForm, StudentsGroupForm

from .models import Subject, Teacher, Student, Group, StudentsGroup


def index(request):
    return HttpResponse("Django main page")


def teacher_form(request):
    if request.method != "POST":
        # if not POST we create a blank form
        form = TeacherForm()
        return render(request, "teacher_form.html", {"form": form})

    form = TeacherForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect(reverse("teacher_edit", args=[form.instance.pk]))

    return render(request, "teacher_form", {"form": form})


def teacher_edit(request, pk):
    teacher = Teacher.objects.get(pk=pk)
    if request.method == "GET":
        form = TeacherForm(instance=teacher)
        return render(request, "teacher_edit.html", {"form": form})
    form = TeacherForm(request.POST, instance=teacher)
    if form.is_valid():
        form.save()
        return redirect("teachers")

    return render(request, "teacher_edit", {"form": form})


def teachers(request):
    teacher = Teacher.objects.all()
    return render(request, "teachers.html", context={"teacher": teacher})


def teacher_delete(request, pk):
    teacher = Teacher.objects.get(pk=pk)
    if request.method == "GET":
        form = TeacherForm(instance=teacher)
        return render(request, "teacher_delete.html", {"form": form})
    teacher.delete()
    return redirect("teachers")


def subject_form(request):
    if request.method != "POST":
        form = SubjectForm()
        return render(request, "subject_form.html", {"form": form})
    form = SubjectForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect(reverse("subjects"))

    return render(request, "subject_form.html", {"form": form})


def subjects(request):
    subject = Subject.objects.all()
    return render(request, "subjects.html", context={"subject": subject})


def student_form(request):
    if request.method != "POST":
        # if not POST we create a blank form
        form = StudentForm()
        return render(request, "student_form.html", {"form": form})

    form = StudentForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect(reverse("student_edit", args=[form.instance.pk]))

    return render(request, "student_form.html", {"form": form})


def student_edit(request, pk):
    student = Student.objects.get(pk=pk)
    if request.method == "GET":
        form = StudentForm(instance=student)
        return render(request, "student_edit.html", {"form": form})
    form = StudentForm(request.POST, instance=student)
    if form.is_valid():
        form.save()
        return redirect("students")

    return render(request, "student_edit.html", {"form": form})


def students(request):
    student = Student.objects.all()
    return render(request, "students.html", context={"student": student})


def student_delete(request, pk):
    student = Student.objects.get(pk=pk)
    if request.method == "GET":
        form = StudentForm(instance=student)
        return render(request, "student_delete.html", {"form": form})
    student.delete()
    return redirect("students")


def group_form(request):
    if request.method != "POST":
        form = GroupForm()
        return render(request, "group_form.html", {"form": form})

    form = GroupForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect(reverse("groups"))

    return render(request, "group_form.html", {"form": form})


def groups(request):
    all_groups = Group.objects.all()
    return render(request, "groups.html", {"groups": all_groups})


def add_student(request):
    if request.method != "POST":
        form = StudentsGroupForm()
        return render(request, "students-group_form.html", {"form": form})
    form = StudentsGroupForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect(reverse("stud_groups"))

    return render(request, "students-group_form.html", {"form": form})


def stud_groups(request):
    groupen = StudentsGroup.objects.all()
    return render(request, "student_groups.html", {"groupen": groupen})
