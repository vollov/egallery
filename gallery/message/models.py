from django.db import models
import uuid

class Message(models.Model):
#     name = models.CharField(max_length=60, blank=True, null=False)
#     email = models.EmailField(max_length=60, blank=True, null=False)
#     title = models.CharField(max_length=160, blank=True, null=True)
#     message = models.TextField(blank=True, null=True)
#     created = models.DateTimeField(auto_now_add=True)
    
    
    name = models.CharField(max_length=60, blank=True, null=False)
    title = models.CharField(max_length=160, blank=True, null=True)
    id = models.CharField(max_length=64, primary_key=True, verbose_name=u"Activation key",
                 default=uuid.uuid4)
    
    #Before persist to db, create a unique serial number
#     def save(self, *args, **kwargs):
#         super(Message, self).save(*args, **kwargs)
        
    def __unicode__(self):
        return self.title
