from django.db import models
from users.forms import UserForm   
from users.models import User

class Blog(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(upload_to="blogs/", default="avatar.png")
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    
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
    date_created=models.DateTimeField(auto_now_add=True, null=True)
    likes=models.ManyToManyField(User, related_name='blog_posts')
    post_views=models.IntegerField(default=0, null=True, blank=True)

    def total_likes(self):
        return self.likes.count()
    
    def __str__(self):
        return f"{self.author}{self.title}"
    

class Comment(models.Model):
    post= models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    body=models.TextField()
    date_added=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.post.title}{self.name}"
