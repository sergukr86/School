import phonenumbers

from django import forms

from school.models import Teacher, Group, Subject, Student, StudentsGroup


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ["first_name", "last_name", "fathers_name", "birth_date", "photo"]


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ["group_name", "teacher"]


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ["name", "description", "score", "teacher"]


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["first_name", "last_name", "phone_number", "admission_year"]

    def clean_phone(self):
        phone = self.cleaned_data["phone_number"]
        if not phone:
            raise forms.ValidationError("Phone cannot be empty.")
        try:
            parsed = phonenumbers.parse(phone, None)
        except phonenumbers.NumberParseException as e:
            raise forms.ValidationError(e.args[0])
        return phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.INTERNATIONAL)


class StudentsGroupForm(forms.ModelForm):
    class Meta:
        model = StudentsGroup
        fields = ["group", "student"]
