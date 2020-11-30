

from django.urls import path
from .  import views


urlpatterns = [
    path('', views.articles_list , name='list'),
    path('<id>', views.articles_show , name='articles_show'),
]
