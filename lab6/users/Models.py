from django.db import models


class User(models.Model):
    idUser = models.IntegerField(unique=True)
    email = models.EmailField(max_length=255, unique=True, null=False)
    bill = models.IntegerField()
    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)


class Comment(models.Model):
    idComment = models.IntegerField(unique=True)
    Course = models.TextField(max_length=255, null=False)
    Text = models.TextField(max_length=255, null=False)


class Course(models.Model):
    idCourse = models.IntegerField(unique=True)
    Name = models.TextField(max_length=255, null=False)
    Duration = models.TextField(max_length=255, null=False)
    Teacher = models.TextField(max_length=255, null=False)
    Value = models.TextField(max_length=255, null=False)

    def __str__(self):
        return 'Course {}'.format(self.title)