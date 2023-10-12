from django.forms import ModelForm

from .models import Teacher, Group, Subject, Student, StudentsGroup


class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = ["first_name", "last_name", "fathers_name", "birth_date"]


class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = ["group_name", "teacher"]


class SubjectForm(ModelForm):
    class Meta:
        model = Subject
        fields = ["name", "description", "score", "teacher"]


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ["first_name", "last_name", "admission_year"]


class StudentsGroupForm(ModelForm):
    class Meta:
        model = StudentsGroup
        fields = ["group", "student"]
