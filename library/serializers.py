from .models import Books, User, Borrow
from rest_framework.serializers import ModelSerializer


class BooksSerializer(ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'
class BorrowSerializer(ModelSerializer):
    class Meta:
        model = Borrow
        fields = '__all__'
        


