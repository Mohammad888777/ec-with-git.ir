from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model
import braintree





gateway = braintree.BraintreeGateway(
    braintree.Configuration(
        braintree.Environment.Sandbox,
        merchant_id="wd73fq8kkxwmtn5b",
        public_key="vqztzq7ffxsxyynp",
        private_key="c3a79f463d0a67fc29753f78ec15fd4a"
    )
)



def validate_session_user(id,token):

    UserModel=get_user_model()
    try:
        user=UserModel.objects.get(pk=id)
        if user.session_token==token:
            return True
        return False

    except UserModel.DoesNotExist:

        return JsonResponse({"error":"user not found"})


@csrf_exempt
def generate_token(request,id,token):

    if not validate_session_user(id,token):
        return JsonResponse({"error":"invalid session token"})


    return JsonResponse({
        "clientToken":gateway.client_token.generate(),"success":True
    })  



@csrf_exempt
def process_payment(request,id,token):

    if not validate_session_user(id,token):
        return JsonResponse({"error":"invalid session token"})
    
    nonce_from_the_client=request.POST["paymentMethodNonce"]
    amount_from_client=request.POST["amount"]

    result=gateway.transaction.sale(
        {
            "amount":amount_from_client,
            "payment_method_nonce":nonce_from_the_client,
            "options":{"submit_for_settlement":True}
        }
    )
    if result.is_success:
        return JsonResponse({
            "success":result.is_success,
            "transaction":{"id":result.transaction.id,"amount":result.transaction.amount}
            })
    else:
        return JsonResponse({"error":True,"success":False})

