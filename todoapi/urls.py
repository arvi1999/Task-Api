from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import ItemViewset, CategoryViewset, UserViewset

router = routers.DefaultRouter()
router.register('category', CategoryViewset)
router.register('item', ItemViewset)
router.register('user', UserViewset)


urlpatterns = [
    path('', include(router.urls)),
]
