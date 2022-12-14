from django.db import models
from django.db.models import UniqueConstraint

from users.models import CustomUser

import os
import uuid


class BaseModel(models.Model):
    """
    추상클래스
    """
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True # 추상 클래스로 만드는 코드
  
# Content : 사용자, 내용, 작성날짜, 수정날짜
class Content(BaseModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = models.TextField()

    class Meta:
        ordering = ["-created_at"]



# Image : content, image, image order, 작성날짜, 수정날짜 
def image_upload_to(instance, filename):
    ext = filename.split(".")[-1]
    return os.path.join(instance.UPLOAD_PATH, "%s.%s"%(uuid.uuid4(),ext))

class Image(BaseModel):

    UPLOAD_PATH = 'user-upload'

    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=image_upload_to)
    order = models.SmallIntegerField()

    class Meta:
        constraints = [UniqueConstraint(name='unique_together',
                        fields=['content','order'])]
        ordering = ['order']