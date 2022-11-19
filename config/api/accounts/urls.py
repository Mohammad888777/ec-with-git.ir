from django.urls import path,include
from . import views
from rest_framework import routers


router=routers.SimpleRouter()
router.register("",views.UserViewSet)


urlpatterns=[



    path("login/",views.signin,name="login"),
    path("logout/<str:pk>/",views.signout,name="logout"),
    path("",include(router.urls)),



]