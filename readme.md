##References
file validation
http://timmyomahony.com/blog/upload-and-validate-image-from-url-in-django/

file overwrite
http://stackoverflow.com/questions/9522759/imagefield-overwrite-image-file-with-same-name


## implements
0.1 when save image, save it to selected albums folder. (Overwrite save method)
0.2 overwrite a existing image if have same name

#install jpeg lib
http://www.ijg.org/files/jpegsrc.v8c.tar.gz.

apt-get install libjpeg libjpeg-dev libfreetype6 libfreetype6-dev zlib1g-dev
pip install -I pillow

##Save a thumb file

#         print self.image.path
        thumb = TImage.open(self.image.path)
        thumb.thumbnail(100, 100)
        filename = "{}_thumbnail.{}".format(self.image_key, 'jpg')
        os.path.join(str(self.album), filename)
        
        
I've had to do this in a few steps, imagejpeg() in php requires a similar process. Not to say theres no way to keep things in memory, but this method gives you a file reference to both the original image and thumb (usually a good idea in case you have to go back and change your thumb size).

save the file
open it from filesystem with PIL,
save to a temp directory with PIL,
then open as a Django file for this to work.
Model:

class YourModel(Model):
    img = models.ImageField(upload_to='photos')
    thumb = models.ImageField(upload_to='thumbs')
Usage:

#in upload code
uploaded = request.FILES['photo']
from django.core.files.base import ContentFile
file_content = ContentFile(uploaded.read())
new_file = YourModel() 
#1 - get it into the DB and file system so we know the real path
new_file.img.save(str(new_file.id) + '.jpg', file_content)
new_file.save()

from PIL import Image
import os.path

#2, open it from the location django stuck it
thumb = Image.open(new_file.img.path)
thumb.thumbnail(100, 100)

#make tmp filename based on id of the model
filename = str(new_file.id)

#3. save the thumbnail to a temp dir

temp_image = open(os.path.join('/tmp',filename), 'w')
thumb.save(temp_image, 'JPEG')

#4. read the temp file back into a File
from django.core.files import File
thumb_data = open(os.path.join('/tmp',filename), 'r')
thumb_file = File(thumb_data)

new_file.thumb.save(str(new_file.id) + '.jpg', thumb_file)



from django.core.files.uploadedfile import InMemoryUploadedFile
import StringIO
def MakeThumbnail(file):
    img = Image.open(file)
    img.thumbnail((128, 128), Image.ANTIALIAS)
    thumbnailString = StringIO.StringIO()
    img.save(thumbnailString, 'JPEG')
    newFile = InMemoryUploadedFile(thumbnailString, None, 'temp.jpg', 'image/jpeg', thumbnailString.len, None)
    return newFile
    
    def createThumbnail(self):
        if not self.image:
             return
        
        from PIL import Image as TImage
        import StringIO
        from django.core.files.uploadedfile import SimpleUploadedFile
        
        THUMBNAIL_SIZE = (200,200)
        
#         DJANGO_TYPE = self.image.file.content_type
#   
#         if DJANGO_TYPE == 'image/jpeg':
#             PIL_TYPE = 'jpeg'
#             FILE_EXTENSION = 'jpg'
#         elif DJANGO_TYPE == 'image/png':
#             PIL_TYPE = 'png'
#             FILE_EXTENSION = 'png'
             
        print self.image.path, self.image
        
        image = TImage.open(self.image.path)
        image.thumbnail(THUMBNAIL_SIZE, TImage.ANTIALIAS)
         
        temp_handle = StringIO()
        image.save(temp_handle, 'jpeg')
        temp_handle.seek(0)
     
        suf = SimpleUploadedFile(os.path.split(self.image.name)[-1],
                 temp_handle.read())
        
        self.thumbnail.save('%s_thumbnail.%s'%(os.path.splitext(suf.name)[0],'jpg'), suf, save=False)
        
        