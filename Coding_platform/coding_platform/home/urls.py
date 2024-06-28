from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path('roadmap/',views.roadmap_page, name='roadmap_view'),
    path('aboutus/',views.aboutus_page, name='aboutus_view'),
    path('contact/',views.contact_page, name='contact_view'),
	path('register/', views.register_page, name='register_page'),
	
]