from django.contrib.auth.models import User
from .models import Task
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer, TaskSerializer, UserSerializerTask
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from django.db.models import Count, Q, Avg


# Create your views here.


@csrf_exempt
@api_view(['POST'])
@permission_classes((AllowAny,))
def signup(request):
    try:
        user = User(
            username=request.data['username'],
            email=request.data['email']
        )
        user.set_password(request.data['password'])
        user.save()
        return Response({"status": "done"}, status=status.HTTP_201_CREATED)
    except Exeption as err:
        print(err)
        return Response({"error": "internal server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@csrf_exempt
@api_view(['POST'])
@permission_classes((AllowAny,))
def signin(request):
    try:
        username = request.data['username']
        password = request.data['password']
        user = authenticate(username=username, password=password)
        if not user:
            return Response({"error":"invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({"token": token.key}, status=status.HTTP_202_ACCEPTED)
    except Exception as err:
        print(err)
        return Response({"error":"internal server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@csrf_exempt
@api_view(["GET"])
def task_list(request):
    user = request.user
    tasks = user.tasks.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@csrf_exempt
@api_view(['POST'])
def new_task(request):
    try:
        task = Task(
            title=request.data['title'],
            description=request.data['description'],
            user=request.user
        )
        task.save()
        serializer = TaskSerializer(task)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except Exception as err:
        print(err)
        return Response({"error":"internal server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@csrf_exempt
@api_view(['GET'])
def get_one_task(request, id):
    try:
        user = request.user
        task = user.tasks.get(id=id)
        serializer = TaskSerializer(task)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as err:
        print(err)
        return Response({"error":"internal server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@csrf_exempt
@api_view(['PUT'])
def edit_task(request, id):
    try:
        user = request.user
        task = user.tasks.get(id=id)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    except Exception as err:
        print(err)
        return Response({"error":"internal server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@csrf_exempt
@api_view(['DELETE'])
def delete_task(request, id):
    try:
        user = request.user
        task = user.tasks.get(id=id)
        if task:
            task.delete()
            serializer = TaskSerializer(task)
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    except Exception as err:
        print(err)
        return Response({"error":"internal server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@csrf_exempt
@api_view(['POST'])
def done_task(request, id):
    try:
        user = request.user
        task = user.tasks.get(id=id)
        if task:
            task.is_done = True
            task.save()
            serializer = TaskSerializer(task)
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    except Exception as err:
        print(err)
        return Response({"error":"internal server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@csrf_exempt
@api_view(['GET'])
def get_users(request):
    try:
        users = User.objects.annotate(tsks=Count('tasks'))
        serializer = UserSerializerTask(users, many=True)
        return Response(serializer.data)
    except Exception as err:
        print(err)
        return Response({"error":"internal server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@csrf_exempt
@api_view(['GET'])
def get_done_tasks(request):
    try:
        users = User.objects.annotate(tsks=Count('tasks', filter=Q(tasks__is_done=True)))
        serializer = UserSerializerTask(users, many=True)
        return Response(serializer.data)
    except Exception as err:
        print(err)
        return Response({"error":"internal server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

