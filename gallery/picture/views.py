from django.shortcuts import render

from django.shortcuts import render_to_response, get_object_or_404
# def blogs(request):
#     return render_to_response('blogs.html', {
#         'page_title': 'blog',
#         'categories': Category.objects.all(),
#         'posts': Blog.objects.all()[:5]
#     })
#

from picture.models import Album, Image

def albums(request):
    albums = Album.objects.all()
    print 'getting albums '
    context = {'albums': albums,
               'page_title' : 'albums'}
    return render(request, 'albums.html', context)

def album(request, title):
    album = get_object_or_404(Album, title=title)
    images = Image.objects.filter(album=album)
    return render_to_response('album_images.html', {
        'page_title': 'album-images',
        'images': images,
        'album':album,
    })


def image(request, album_id):
    album = get_object_or_404(Image, id=album_id)
    images = Image.objects.filter(album=album)
    return render_to_response('album_images.html', {
        'page_title': 'album-images',
        'images': images,
        'album':album,
    })
#     
# def album