from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return self.title