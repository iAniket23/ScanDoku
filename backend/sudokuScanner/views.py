from django.http import HttpRequest
from django.shortcuts import render
from django.http import HttpResponse
from  rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status 
from .models import user as User
from .models import sudoku as Sudoku
from .models import image as Image
from .serializers import UserSerializer
from .serializers import SudokuSerializer
from .serializers import ImageSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view, renderer_classes
from drf_yasg.utils import swagger_auto_schema

# Create your views here.
@api_view(['GET', 'POST'])
@renderer_classes([JSONRenderer])
def manageAllUser(request: HttpRequest):

    supportedHTTPmethods = ['GET', 'POST']

    if request.method not in supportedHTTPmethods:
        return Response("Provided HTTP method is not supported",status = status.HTTP_404_NOT_FOUND)

    else :
        # GET all users
        if request.method == 'GET':
            
            user = User.objects.all().order_by('userID')
            u = UserSerializer(user, many=True)
            content = {'users': u.data}
            return Response(content ,status = status.HTTP_200_OK)
        # POST a new user
        elif request.method == 'POST':
            new_user = User.objects.create(
                username = request.data['username'],
                password = request.data['password'],
            )
            new_user.save()
            content = {'message': "User created successfully"}
            return Response(content ,status = status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
@renderer_classes([JSONRenderer])
def manageSingleUser(request: HttpRequest, userID):
    
    supportedHTTPmethods = ['GET', 'PUT', 'DELETE']

    if request.method not in supportedHTTPmethods:
        return Response("Provided HTTP method is not supported",status = status.HTTP_404_NOT_FOUND)
    
    else:
        # GET a single user by ID
        if request.method == 'GET':
            user = User.objects.get(pk = userID)
            u = UserSerializer(user)
            content = {'users': u.data}
            return Response(content ,status = status.HTTP_200_OK)

        # TODO put, delete

@api_view(['GET', 'POST'])
@renderer_classes([JSONRenderer])
def manageSingleSudoku(request: HttpRequest, userID):
        
        supportedHTTPmethods = ['GET', 'POST']
    
        if request.method not in supportedHTTPmethods:
            return Response("Provided HTTP method is not supported",status = status.HTTP_404_NOT_FOUND)

        else:
            if request.method == 'GET':
                sudoku = Sudoku.objects.filter(userID = userID)
                s = SudokuSerializer(sudoku, many=True)
                content = {'sudokus': s.data}
                return Response(content ,status = status.HTTP_200_OK)
            
            elif request.method == 'POST':
                new_sudoku = Sudoku.objects.create(
                    row1 = request.data['row1'],
                    row2 = request.data['row2'],
                    row3 = request.data['row3'],
                    row4 = request.data['row4'],
                    row5 = request.data['row5'],
                    row6 = request.data['row6'],
                    row7 = request.data['row7'],
                    row8 = request.data['row8'],
                    row9 = request.data['row9'],
                    user = request.data['user'],
                )
                new_sudoku.save()
                content = {'message': "Sudoku created successfully"}
                return Response(content ,status = status.HTTP_201_CREATED)

@api_view(['GET','POST'])
def manageAllImage(request: HttpRequest):
    
    supportedHTTPmethods = ['GET','POST']

    if request.method not in supportedHTTPmethods:
        return Response("Provided HTTP method is not supported",status = status.HTTP_404_NOT_FOUND)
    else:
        if request.method == 'GET':
            image = Image.objects.all()
            i = ImageSerializer(image, many=True)
            content = {'images': i.data}
            return Response(content ,status = status.HTTP_200_OK)
        
        elif request.method == 'POST':
            new_image = Image.objects.create(
                image = request.data['image'],
            )
            new_image.save()
            content = {'message': "Image created successfully"}
            return Response(content ,status = status.HTTP_201_CREATED)
    
    
@api_view(['GET'])
def manageSingleImage(request: HttpRequest, imageID):
    
    supportedHTTPmethods = ['GET']

    if request.method not in supportedHTTPmethods:
        return Response("Provided HTTP method is not supported",status = status.HTTP_404_NOT_FOUND)
    else:
        if request.method == 'GET':
            image = Image.objects.filter(imageID = imageID)
            i = ImageSerializer(image, many=True)
            content = {'images': i.data}
            return Response(content ,status = status.HTTP_200_OK)
        

