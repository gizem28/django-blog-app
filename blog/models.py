from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(upload_to="student/", default="avatar.png")

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
        return f"{self.title} {self.content}"
