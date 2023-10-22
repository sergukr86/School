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
    def clean_phone_number(self):
        phone_number = self.cleaned_data["phone_number"]
        if not phone_number:
            raise forms.ValidationError("Phone cannot be empty")
        try:
            parsed_num = phonenumbers.parse(phone_number, None)
            if not phonenumbers.is_valid_number(parsed_num):
                raise forms.ValidationError("Wrong number")
        except phonenumbers.NumberParseException as error:
            raise forms.ValidationError(error.args[0])
        return phonenumbers.format_number(
            parsed_num, phonenumbers.PhoneNumberFormat.INTERNATIONAL
        )

    class Meta:
        model = Student
        fields = ["first_name", "last_name", "phone_number", "admission_year"]


class StudentsGroupForm(forms.ModelForm):
    class Meta:
        model = StudentsGroup
        fields = ["group", "student"]
