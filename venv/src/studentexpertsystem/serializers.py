from rest_framework import serializers

from .models import Boards, Courses, Groups,DetailModel

class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = ["courseId", "courseName","board","group", "isActive", "createdDate" ]


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boards
        fields = ["boardId", "boardName","isActive", "createdDate" ]



class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Groups
        fields = ["groupId", "groupName","isActive", "createdDate" ]

class DetailModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetailModel
        fields = ["id", "account","board", "group","courses" ]

