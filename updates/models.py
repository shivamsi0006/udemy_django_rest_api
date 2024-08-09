from django.db import models
from django.conf import settings
from django.core.serializers import serialize

# Create your models here.


def upload_update_image(instance,filename):
    return "updates/{user}/{filename}".format(user=instance.user,filename=filename)


class UpdateQuerySet(models.QuerySet):
    def serialize(self):
        qs=self
        return serialize('json',qs,fields=('user','content','image'))


class UpdateManager(models.Manager):
    def serialize(self):
        return UpdateQuerySet(self.model,using=self._db)


class update(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    content=models.TextField(blank=True,null=True)
    image=models.ImageField(upload_to=upload_update_image,blank=True,null=True)
    updated =models.DateTimeField(auto_now=True)
    timestamp=models.DateTimeField(auto_now_add=True)

    objects=UpdateManager()

    def __str__(self):
        return self.content


    def serialize(self):
        return serialize("json",[self],fields=('user','content','image'))

