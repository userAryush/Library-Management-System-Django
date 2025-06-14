from .models import Books, User, Borrow
from rest_framework.serializers import ModelSerializer



class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password','college_id']
        
class BooksSerializer(ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'
        
class BorrowSerializer(ModelSerializer):
    class Meta:
        model = Borrow
        fields = '__all__'
        


