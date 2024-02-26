from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter() # make wifi 
router.register('', views.AppointmentViewSet)  # ekta entena toiri kora holo

urlpatterns =[
    path('', include(router.urls)),
]