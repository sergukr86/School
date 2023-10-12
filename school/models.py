from django.db import models


# Create your models here.


class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    fathers_name = models.CharField(max_length=50)
    birth_date = models.DateTimeField()
    photo = models.ImageField()

    def __str__(self):
        return f"ID: {self.pk} {self.first_name}"


class Subject(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    score = models.IntegerField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return f"ID: {self.pk} {self.name}"


class Group(models.Model):
    group_name = models.CharField(max_length=50)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return f"ID: {self.pk} {self.group_name}"


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20, null=True)
    admission_year = models.CharField(max_length=4)

    def __str__(self):
        return f"ID: {self.pk} {self.first_name}"


class StudentsGroup(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return f"Group: {self.group} {self.student}"


class Parameters(models.Model):
    request_path = models.CharField(max_length=50)
    request_method = models.CharField(max_length=50)
    execution_time = models.FloatField(max_length=20)
