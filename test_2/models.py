from django.db import models

# Create your models here.
class Comment(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return self.text
