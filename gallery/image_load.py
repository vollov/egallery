import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gallery.settings')

import django
django.setup()

from picture.models import Album, Image
from django.contrib.auth.models import User

from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
import glob

# Load images under data folder, the album name is the folder name
class ImageLoad:
    def __init__(self, p):
        self.data_directory = os.path.join(settings.BASE_DIR,'data')
        self.picturePopulater = p
        
    def addAlbums(self):
        for file_name in os.listdir(self.data_directory):
            album = self.picturePopulater.addAlbum(file_name, True)
            self.addPictures(album)
            
    def addPictures(self, album):
        album_directory = os.path.join(self.data_directory, album.title)
        jpg_file_list = glob.glob(os.path.join(album_directory, "*.jpg"))
        
        for file_path in jpg_file_list:
            image = self.picturePopulater.getImage(file_path)
            created = self.picturePopulater.addImage(album.title, p.user, album, image)
            print created
    
class PicturePopulater:
    def __init__(self):
        self.user, created = User.objects.get_or_create(username='Katie', password='password')

    def addAlbum(self, title, active):
        album, created = Album.objects.get_or_create(title=title, public=active)
        return album
    
    def addImage(self,t,u,a, i):
        image, created = Image.objects.get_or_create(title=t, user=u, album = a, image=i)
        return created
    
    def getImage(self, file_path):
        g1_file = open(file_path, 'rb')
        return SimpleUploadedFile(g1_file.name, g1_file.read())
    
if __name__ == '__main__':
    print "Loading Album population script..."
    
    p = PicturePopulater()
    l = ImageLoad(p)
    l.addAlbums() 