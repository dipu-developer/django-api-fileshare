from django.db import models
import uuid
import os
# Create your models here.

class Folder(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True, editable=False)
    created_at = models.DateTimeField(auto_now_add = True)

def get_upload_path(instance,filename):
    return os.path.join(str(instance.folder.uid),filename)

class File(models.Model):
    folder = models.ForeignKey(Folder,on_delete=models.CASCADE)
    file = models.FileField(upload_to=get_upload_path)
    create_at = models.DateField(auto_now_add = True)