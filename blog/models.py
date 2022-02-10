from django.db import models
from users.forms import UserForm   
from users.models import User

class Blog(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(upload_to="student/", default="avatar.png")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    Category =(
        ("1", "Tecnology"),
        ("2", "Social"),
        ("3", "Travel"),
        ("4", "Other"),
    )
    
    Status =(
        ("1", "Draft"),
        ("2", "View"),
    )
    
    category = models.CharField(max_length=50, choices=Category)
    status = models.CharField(max_length=50, choices=Status)

    def __str__(self):
        return f"{self.author}{self.title}"
