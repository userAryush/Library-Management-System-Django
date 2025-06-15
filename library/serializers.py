from .models import Books, User, Borrow
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import Group


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password','college_id','groups']
   
class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = ['id','name']
class BooksSerializer(ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'
        
class BorrowSerializer(ModelSerializer):
    class Meta:
        model = Borrow
        fields = '__all__'
        


