from django.db import models

from django.contrib.auth.models import User

from django.conf import settings
from storage import OverwriteStorage
# from sorl.thumbnail import ImageField as TImageField

import os,uuid
# import uuid


class Album(models.Model):
    title = models.CharField(max_length=60, unique=True)
    public = models.BooleanField(default=False)
    
    #Before save to db, create album folder in settings.MEDIA_ROOT, if the folder is not existing
    def save(self, *args, **kwargs):
        album_directory = os.path.join(settings.MEDIA_ROOT, self.title)
        
        print album_directory
        if not os.path.exists(album_directory):
            os.makedirs(album_directory)
    
        super(Album, self).save(*args, **kwargs)
                
    def __unicode__(self):
        return self.title

def image_upload_path(instance, name):
    ext = name.split('.')[-1]
    filename = "{}.{}".format(instance.image_key, ext)
    return os.path.join(str(instance.album), filename)

class Image(models.Model):
    
    title = models.CharField(max_length=60, blank=True, null=True)
    image_key = models.CharField(max_length=64, verbose_name=u"Activation key",
                 default=uuid.uuid4)
    album = models.ForeignKey('picture.Album')
#     image = TImageField(upload_to=image_upload_path)
#     image = models.ImageField(upload_to=image_upload_path)
    image = models.ImageField(storage=OverwriteStorage(), upload_to=image_upload_path)
#     thumbnail = models.ImageField(storage=OverwriteStorage(), upload_to=thumbnail_upload_path,blank=True,null=True)
    
#     image = models.ImageField(max_length=SOME_CONST, storage=OverwriteStorage(), upload_to=image_path)

    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, null=True, blank=True)
    
    #uid = models.CharField(max_length=64, verbose_name=u"Activation key", default=uuid.uuid1())
    

#     def save(self, *args, **kwargs):
# #         print str(self.album)
#         
#         super(Image, self).save(*args, **kwargs)
#         self.createThumbnail()
        
#         img_file = os.path.join(settings.MEDIA_ROOT, self.image)
#         print img_file
#         TImage.open(img_file).thumbnail((50,50), TImage.ANTIALIAS)
#         .save(os.path.join(settings.MEDIA_ROOT, self.album.title + '/' + self.image_key + "_thumbnail.jpg"))



    def __unicode__(self):
        return self.image.name
    
# Receive the pre_delete signal and delete the file associated with the model instance.
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver

@receiver(pre_delete, sender=Image)
def auto_delete_image_on_delete(sender, instance, **kwargs):
    """Deletes file from filesystem
    when corresponding Image object is deleted.
    """
    # Pass false so FileField doesn't save the model.
    instance.image.delete(False)

@receiver(models.signals.pre_save, sender=Image)
def auto_delete_image_on_change(sender, instance, **kwargs):
    """Deletes file from filesystem
    when corresponding Image object is changed.
    """
    if not instance.pk:
        return False
 
    try:
        old_file = Image.objects.get(pk=instance.pk).image
    except Image.DoesNotExist:
        return False
 
    new_file = instance.image
    if not old_file == new_file:
        old_file.delete(False)