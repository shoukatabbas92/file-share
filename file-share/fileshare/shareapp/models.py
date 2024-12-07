from django.db import models
import uuid


class File(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='uploads/')
    uuid = models.UUIDField(default=uuid.uuid4,editable=False,unique=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
