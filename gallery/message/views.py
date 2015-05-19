from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404

from message.forms import MessageForm
from models import Message

def add_msg(request):
    # A HTTP POST?
    if request.method == 'POST':
        form = MessageForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            human = True
            # Save the new category to the database.
            new_message = form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the homepage.
            return show_msg(request, str(new_message.id))
#             return render(request, 'add.html', {
#                 'page_title': 'message delivered',
#             })
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = MessageForm()

    return render(request, 'add.html', {
        'page_title': 'Contact us',
        'form': form,
    })
    
def show_msg(request, mid):
    message = get_object_or_404(Message, id=mid)
    return render(request, 'show.html', {
        'page_title': 'message - '+ mid,
        'message': message,
    })
# 
# def add_msg(request):
#     print 'In message.views.contact_us'
#  
#     if request.method == 'GET':
#         print '[GET] In message.views.contact_us'
#         form = MessageForm()
#      
#     return render_to_response('new_msg.html', {
#         'page_title': 'Contact us',
#         'form': form,
#     })
#      
# def save_msg(request):
#     if request.method == 'POST':
#         print '[POST] In message.views.contact_us'
#         form = MessageForm(request.POST)
#         if form.is_valid():
#             # Save the form to the database.
#             form.save(commit=True)
#              
#             return contact_us(request)
#         else:
#             print form.errors
#              
#     return render_to_response('view_msg.html', {
#         'page_title': 'Contact us',
#         'form': form,
#     })