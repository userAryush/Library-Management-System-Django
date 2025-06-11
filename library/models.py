from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    ROLE = [('admin','Admin'), ('member', 'Member')]
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=200, unique=True)
    full_name = models.CharField(max_length=300)
    college_id = models.CharField(max_length=50)
    user_type = models.CharField(max_length=6, choices=ROLE)
    
    USERNAME_FIELD ='email'
    REQUIRED_FIELDS = ['username', 'full_name', 'college_id', 'user_type']
    
class Books(models.Model):
    GENRE_CHOICES = [
        ("Programming", "Programming"),
        ("Algorithms", "Algorithms"),
        ("Operating Systems", "Operating Systems"),
        ("Databases", "Databases"),
        ("Computer Networks", "Computer Networks"),
        ("Software Engineering", "Software Engineering"),
        ("Artificial Intelligence", "Artificial Intelligence"),
        ("Cybersecurity", "Cybersecurity"),
        ("Web Development", "Web Development"),
        ("IoT", "IoT"),
        ("Mathematics", "Mathematics"),
        ("Electronics", "Electronics"),
        ("Robotics", "Robotics"),
        ("Communication Skills", "Communication Skills"),
        ("Interview Preparation", "Interview Preparation"),
        ("Self-Help", "Self-Help"),
        ("Fiction", "Fiction"),
        ("Other", "Other"),
    ]

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publication_date = models.DateField()
    genre = models.CharField(max_length=50, choices = GENRE_CHOICES)
    total_books = models.PositiveIntegerField(default=0) #allows numbers from 0 
    available_books = models.PositiveIntegerField(default=0)
    #add image if at last if doing frontend also
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    created_by = models.CharField(max_length=300)
    updated_by = models.CharField(max_length=300)
    
class Borrow(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    book = models.ForeignKey(Books, on_delete=models.SET_NULL, null=True)
    borrowed_date = models.DateTimeField(auto_now_add=True)
    


