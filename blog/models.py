from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField

    GENDER =(
        ("1", "Female"),
        ("2", "Male"),
        ("3", "Other"),
        ("4", "Prefer Not Say"),
    )

    gender = models.CharField(max_length=50, choices=GENDER)
    number = models.IntegerField(unique=True, blank=True, null=True)
    image = models.ImageField(upload_to="student/", default="avatar.png")

    def __str__(self):
        return f"{self.number} {self.first_name} {self.last_name}"
