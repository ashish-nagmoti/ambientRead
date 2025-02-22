from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='files/')
    # bookid = models.AutoField(primary_key=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.file.name
    

