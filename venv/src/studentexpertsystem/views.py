from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from .models import Courses, Groups, Boards,DetailModel
from .serializers import CoursesSerializer,BoardSerializer,GroupSerializer,DetailModelSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
#from ..account.models import Account
import sys
sys.path.append("..account.models import Account")

#from application.app.account.models import Account
# Create your views here.
@api_view(['GET', 'POST',])
@permission_classes((IsAuthenticated,))
def courses_list(request):
    if request.method == 'GET':
        courses = Courses.objects.all()
        serializer = CoursesSerializer(courses,many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CoursesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return  JsonResponse(serializer.data,status=201)

        return JsonResponse(serializer.errors,status=400)

@api_view(['GET',])
@permission_classes((IsAuthenticated,))
def detail_model_view(request):
    if request.method == 'GET':
        detail_model = DetailModel.objects.all()
        serializer = DetailModelSerializer(detail_model,many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = DetailModelSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return  JsonResponse(serializer.data,status=201)

        return JsonResponse(serializer.errors,status=400)


@api_view(['GET', 'POST',])
@permission_classes((IsAuthenticated,))
def groups_list(request):
    if request.method == 'GET':
        groups = Groups.objects.all()
        serializer = GroupSerializer(groups,many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = GroupSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return  JsonResponse(serializer.data,status=201)

        return JsonResponse(serializer.errors,status=400)


@api_view(['GET', 'POST',])
@permission_classes((IsAuthenticated,))
def boards_list(request):
    if request.method == 'GET':
        boards = Boards.objects.all()
        serializer = BoardSerializer(boards,many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BoardSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return  JsonResponse(serializer.data,status=201)

        return JsonResponse(serializer.errors,status=400)


