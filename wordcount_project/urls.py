






from . import views



from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('count/', views.count, name='count'),
    path('about1/',views.about1, name='about1')
]
