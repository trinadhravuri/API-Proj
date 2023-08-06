from django.urls import path
from . import views

urlpatterns = [
    path('',views.BookApiView.as_view(),name='books'),
    path('weat',views.weather,name='weat'),
    path('home',views.home,name='home'),
]
