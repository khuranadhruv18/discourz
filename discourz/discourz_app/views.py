from django.shortcuts import render
from discourz_app.models import Account


# Create your views here.
def profile(request):
    account = Account.objects.filter(username__exact="alexsun")

    context = {
        'username': account[0].username,
        'email': account[0].email,
        'bio' : account[0].bio,
        'img' : account[0].img,
    }

    return render(request, 'profile.html', context=context)
    