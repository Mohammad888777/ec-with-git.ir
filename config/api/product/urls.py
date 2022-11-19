from django.urls import path,include
from . import views
from rest_framework import routers

router=routers.SimpleRouter()

router.register("",views.ProductViewSet,basename="product_list")

urlpatterns=[

    path("",include(router.urls)),

]