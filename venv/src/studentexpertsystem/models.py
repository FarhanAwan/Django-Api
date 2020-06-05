from django.db import models

import sys
sys.path.append("..account.models import Account")

# Create your models here.


class Groups(models.Model):
    groupId = models.AutoField(primary_key=True)
    groupName = models.CharField(max_length= 25)
    isActive = models.BooleanField(default=True)
    createdDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return  self.groupName

class Boards(models.Model):
    boardId = models.AutoField(primary_key=True)
    boardName = models.CharField(max_length=10)
    isActive = models.BooleanField(default=True)
    createdDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.boardName


class Courses(models.Model):
    courseId = models.AutoField(primary_key=True)
    courseName = models.CharField(max_length=25)
    board = models.ForeignKey(Boards,on_delete=models.CASCADE,)
    group = models.ManyToManyField(Groups, blank=True)
    isActive = models.BooleanField(default=True)
    createdDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.courseName





class DetailModel(models.Model):
    account = models.OneToOneField('account.Account',on_delete=models.CASCADE,)
    board = models.OneToOneField(Boards, on_delete=models.CASCADE, )
    group = models.OneToOneField(Groups, on_delete=models.CASCADE,)
    courses = models.ManyToManyField(Courses,)

    def __str__(self):
        return str(self.account)


