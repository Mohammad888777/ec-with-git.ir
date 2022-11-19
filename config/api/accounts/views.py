from django.shortcuts import render
from django.contrib.auth import get_user_model

from .seriaizers import UserSeriaizer
from rest_framework import viewsets
from django.contrib.auth import login,logout,authenticate
from django.http import JsonResponse
from .utils import generate_token
from rest_framework.permissions import AllowAny
from django.views.decorators.csrf import csrf_exempt






@csrf_exempt
def  siginin(request):

    if request.method !="POST":
        return JsonResponse({"error":"only post is allowe=d"})
    
    email=request.POST.get("email")
    password=request.POST.get("password")

    if password:
        if len(password)<=3:
            return JsonResponse({"error":"length of password is low"})
        
    
    User=get_user_model()

    try:
        user=User.objects.get(email=email)
        if user:
            if user.check_password(password):
                user_dict=User.objects.filter(email=email).values().first()
                user_dict.pop("password")

                if user.session_token!="0":
                    user.session_token="0"
                    user.save()
                return JsonResponse({"error":"previous session is exsist"})

                token=generate_token()
                user.session_token=token
                user.save()
                login(request,user)

                return JsonResponse({"token":token,"msg":"you are logged in","user_dict":user_dict})
            else:
                return JsonResponse({"error":"password is incorrect "})
        else:
            return JsonResponse({"error":"not user found with this information "})

    except User.DoesNotExist:        
        return JsonResponse({"error":"user does not exsits"})








def signout(request,pk):

    logout(request)
    UserModel=get_user_model()
    user=UserModel.objects.get(pk=pk)
    if user:
        user.session_token="0"
        user.save()

    return JsonResponse({"msg":"you logged put"})





class UserViewSet(viewsets.ModelViewSet):


    serializer_class=UserSeriaizer
    permission_classes_by_action={"create":[AllowAny]}
    queryset=get_user_model().objects.all().order_by("-id")

    def get_permissions(self):
        
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]

        except KeyError :
            return [permission() for permission in self.permission_classes]


