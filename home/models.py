import os
import uuid
from uuid import uuid4
from django.db import models

# Create your models here.


class Folder(models.Model):
    uid = models.UUIDField(primary_key= True , editable= False , default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now=True)


def get_upload_path(instance, filename):
    return os.path.join(str(instance.folder.uid), filename)


class Files(models.Model):
    # uid = models.UUIDField(primary_key=True, default=uuid4.uuid, editable=False)
    file = models.FileField(upload_to=get_upload_path)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)