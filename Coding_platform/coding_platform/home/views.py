from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request,'index.html')
def roadmap_page(request):
    return render(request,'roadmap_home.html')
def aboutus_page(request):
    return render(request,'aboutus.html')
def contact_page(request):
    return render(request,'contact.html')

def register_page(request):
    """
    Returns the registration page.

    Returns
    -------
    HTTPResponse
        The registration page.
    """
    return render(request, 'register.html')


