from django.urls import path,include
from rest_framework.authtoken import views

urlpatterns=[
    
    path("category/",include("api.category.urls")),
    path("product/",include("api.product.urls")),
    path("payment/",include("api.payment.urls")),
    path("order/",include("api.order.urls")),
    path("accounts/",include("api.accounts.urls")),
    path('api-token-auth/', views.obtain_auth_token),
    
]
