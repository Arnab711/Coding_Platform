from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path('roadmap/',views.roadmap_page, name='roadmap_view'),
    path('aboutus/',views.aboutus_page, name='aboutus_view'),
    path('contact/',views.contact_page, name='contact_view'),
	path('login/', views.login_page, name='login_page'),
    path('register/', views.register_page, name='register_page'),
    path('restricted/', views.restricted_view, name='restricted'),
    path('logout/',views.logout_page, name='logout'),
     path('questions/<int:topic_id>/', views.questions_page, name='questions'),
]