from django.db import models
from django.contrib.auth.models import User
from django.db.models.expressions import OrderBy
from django.db.models.fields import CharField
from ckeditor_uploader.fields import RichTextUploadingField


class Task(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE ,null=True, blank=True)
    title=CharField(max_length=200)
    description=RichTextUploadingField()

    complete=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering=['complete']
        