from distutils.command import upload
from django.db import models

# Create your models here.


class UsersGLB(models.Model):
    glb_file = models.FileField(upload_to="glb/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.glb_file.name
