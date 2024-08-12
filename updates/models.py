from django.db import models
from django.conf import settings
from django.core.serializers import serialize
import json

# Create your models here.

# jsonclassbasedview



def upload_update_image(instance,filename):
    return "updates/{user}/{filename}".format(user=instance.user,filename=filename)

class UpdateQuerySet(models.QuerySet):
    def serialize(self):
        qs=self
        return serialize('json',qs,fields=('id','user','content','image'))


class UpdateManager(models.Manager):
    def get_queryset(self):
        return UpdateQuerySet(self.model,using=self._db)


class update(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    content=models.TextField(blank=True,null=True)
    image=models.ImageField(upload_to=upload_update_image,blank=True,null=True)
    updated =models.DateTimeField(auto_now=True)
    timestamp=models.DateTimeField(auto_now_add=True)

    objects=UpdateManager()

    def __str__(self):
        return self.content or ""


    def serialize(self):
        # return serialization 
        # return serialize('json',[self],fields=('id','user','content','image'))

        try:
            image=self.image.url
        except:
            image=""

        data={
            "id":self.id,
            "content":self.content,
            "user":self.user.id,
            "image":image
        }
        data=json.dumps(data)
        return data


