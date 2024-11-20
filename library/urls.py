"""
URL configuration for library project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from author.views import AuthorAPIView
from publisher.views import PublisherAPIView
from book.views import BooksAPIView, BookAPIView
from rest_framework import routers

router = routers.DefaultRouter()




urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('authors/', AuthorAPIView.as_view()),
    path('authors/<uuid:id_author>/', AuthorAPIView.as_view()),
    path('publishers/', PublisherAPIView.as_view()),
    path('publishers/<uuid:id_publisher>/', PublisherAPIView.as_view()),
    path('books/', BooksAPIView.as_view(), name='books'),
    path('books/<uuid:id_book>/', BookAPIView.as_view(), name='book'),

]
