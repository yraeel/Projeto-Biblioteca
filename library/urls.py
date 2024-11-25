
from django.contrib import admin
from django.urls import path, include
from author.views import AuthorViewSet
from publisher.views import PublisherViewSet
from book.views import BookViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"Author", AuthorViewSet)
router.register(r"Publisher", PublisherViewSet)
router.register(r"Book", BookViewSet)




urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),

]
