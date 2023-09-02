from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name='bloghome'),
    path('article/<slug:article>/', views.single_article, name='article'),
]
