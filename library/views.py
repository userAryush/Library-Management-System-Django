from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .models import Books, Borrow
from .serializers import BooksSerializer,BorrowSerializer



# Create your views here.
class BooksViewSet(ModelViewSet):
    queryset = Books.objects.all()
    # data should be in json format when requesting so we use serializer to convert obj into json format
    serializer_class = BooksSerializer
    filterset_fields = ["author","genre"]
    search_fields = ["title","author","genre"]
    
class BorrowViewSet(ModelViewSet):
    queryset = Borrow.objects.all()
    # data should be in json format when requesting so we use serializer to convert obj into json format
    serializer_class = BorrowSerializer
    filterset_fields = ["user"]
    
    
  
    
    

