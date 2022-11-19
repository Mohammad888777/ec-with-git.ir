from django.urls import path,include
from . import views
from rest_framework import routers


router=routers.SimpleRouter()
router.register("",views.OrderViewSet,basename="order_list")



urlpatterns=[

        path("",include(router.urls)),
        path("add_order/<str:id>/<str:token>/",views.make_order,name="add_order"),

]
