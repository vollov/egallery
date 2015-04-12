from django.test import TestCase

from models import Album, Image

class AlbumModelTests(TestCase):
    def setUp(self):
        a, created = Album.objects.get_or_create(title="lion", public=True)
#         a.save()
        b, created = Album.objects.get_or_create(title="cat", public=True)
#         b.save()
        
    def test_getAlbumByID(self):
        album = Album.objects.get(id=2)
        print album.__dict__
        self.assertEqual(album.title, 'cat')

        
    def test_getAlbumByTitle(self):
        album = Album.objects.get(title='cat')
        print album.__dict__
        self.assertEqual(album.id, 4)
        albums = Album.objects.all()
        self.assertEqual(len(albums), 2)

# class ImageModelTests(TestCase):
# 
#     def test_getImagesByAlbum(self):
#         
#         album = Album.objects.get(title=category_name_slug)
#         context_dict['category_name'] = category.name
# 
#         # Retrieve all of the associated pages.
#         # Note that filter returns >= 1 model instance.
#         pages = Page.objects.filter(category=category)
#         
#         
#         images = 
#         car = Car(make='Acura',model='TL', kilometers=74673, year=2012, color='White', engine_size=3.7, drivetrain='AWD', transmition='MA')
#         car.save()
#         
#         self.assertEqual(car.drivetrain, 'AWD')
#         self.assertEqual(car.transmition, 'MA')