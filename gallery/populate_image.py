import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gallery.settings')

import django
django.setup()

from picture.models import Album, Image
from django.contrib.auth.models import User

from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile

class PicturePopulate:
    def __init__(self):
        self.u1, created = User.objects.get_or_create(username='Katie', password='password')
        test_directory = os.path.join(settings.BASE_DIR,'test')
        self.img_directory = os.path.join(test_directory, 'image')      
        
    def addAlbum(self, title, active):
        album, created = Album.objects.get_or_create(title=title, public=active)
        return album
    
    def addImage(self,t,u,a, i):
        image, created = Image.objects.get_or_create(title=t, user=u, album = a, image=i)
        return image
    
    def populateAlbum(self):
        self.a1 = self.addAlbum('armpit', True)
        self.a2 = self.addAlbum('gretta', True)
    
    def getImage(self, file_path):
        g1_path = os.path.join(self.img_directory,file_path)
        g1_file = open(g1_path, 'rb')
        return SimpleUploadedFile(g1_file.name, g1_file.read())
        
    def populateImage(self):
        g=self.getImage('gretta/g1.jpg')
        self.addImage('g1', self.u1, self.a2, g)
        
        g=self.getImage('gretta/g2.jpg')
        self.addImage('g2', self.u1, self.a2, g)
        
        g=self.getImage('gretta/g3.jpg')
        self.addImage('g3', self.u1, self.a2, g)
        
        g=self.getImage('armpit/h1.jpg')
        self.addImage('h1', self.u1, self.a1, g)
        
        g=self.getImage('armpit/h2.jpg')
        self.addImage('h2', self.u1, self.a1, g)
        
        g=self.getImage('armpit/h3.jpg')
        self.addImage('h3', self.u1, self.a1, g)
                
        g=self.getImage('armpit/h4.jpg')
        self.addImage('h4', self.u1, self.a1, g)
        
    def populate(self):
        p.populateAlbum()
        p.populateImage()
        
if __name__ == '__main__':
    print "Starting Album population script..."
    p = PicturePopulate()
    p.populate()
    
