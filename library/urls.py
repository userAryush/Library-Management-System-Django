from django.urls import path, include
from .views import *

urlpatterns = [
    path('books-set/',BooksViewSet.as_view({'get':'list','post':'create'})), #list gets all data   
    path('books-set/<int:pk>/',BooksViewSet.as_view({'get':'retrieve','put':'update','delete':'destroy'})), #retrive gets only one by id 
    path('books-borrow/',BorrowViewSet.as_view({'get':'list','post':'create'})), 
    path('books-borrow/',BorrowViewSet.as_view({'get':'retrieve','put':'update','delete':'destroy'})), 
]