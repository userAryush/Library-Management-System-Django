from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .models import Books, Borrow
from .serializers import BooksSerializer,BorrowSerializer,UserSerializer, GroupSerializer
from rest_framework.decorators import api_view , permission_classes
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import AllowAny, DjangoModelPermissions
from django.contrib.auth.models import Group



# Create your views here.
@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    password = request.data.get('password')
    hashed_password = make_password(password)
    request.data['password'] = hashed_password
    serializer = UserSerializer(data= request.data)
    if serializer.is_valid():
        serializer.save()
        return Response('User Created!')
    else:
        return Response(serializer.errors)
    
@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    
    user = authenticate(request, email=email, password=password) #if matched returns user object else None
    
    if user == None:
        return Response({'error': 'Invalid credentials!'})
    else:
        #create token
        token,_ = Token.objects.get_or_create(user=user)
        return Response(token.key)
@api_view(['GET'])   
@permission_classes([AllowAny]) 
def group_listing(request):
    group_objs = Group.objects.all()
    serializer_class = GroupSerializer(group_objs, many=True)
    return Response(serializer_class.data)
    

class BooksViewSet(ModelViewSet):
    queryset = Books.objects.all()
    # data should be in json format when requesting so we use serializer to convert obj into json format
    serializer_class = BooksSerializer
    filterset_fields = ["author","genre"]
    search_fields = ["title","author","genre"]
    permission_classes = [DjangoModelPermissions]
    
class BorrowViewSet(ModelViewSet):
    queryset = Borrow.objects.all()
    # data should be in json format when requesting so we use serializer to convert obj into json format
    serializer_class = BorrowSerializer
    filterset_fields = ["user"]
    permission_classes = [DjangoModelPermissions]
    

    
  
    
    

