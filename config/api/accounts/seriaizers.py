from .models import User
from rest_framework import serializers

class UserSeriaizer(serializers.ModelSerializer):

    password2=serializers.CharField(max_length=200,write_only=True,style={
        'input_type':'password'
    })

    class Meta:

        extra_kwargs={"password":{"write_only":True}}
        model=User
        fields=["first_name","password","password2","username","last_name","email","phone_number","last_login","date_joined","is_admin","is_active","is_staff"]
    
    def save(self, **kwargs):

        pass1=self.validated_data.get("password")
        pass2=self.validated_data.get("password2")

        if pass1!=pass2:
            raise serializers.ValidationError("not passwor mathc error")
        
        email=self.validated_data.get("wmail")
        user=User.objects.filter(email=email).exists()

        if user:
            raise serializers.ValidationError("email laready hehre")

        user=User(email=self.validated_data.get("email"),first_name=self.validated_data.get("first_name"),
        last_name=self.validated_data.get("last_name"),username=self.validated_data.get("username")
        )
        user.set_password(pass1)
        user.save()
        return user

    def create(self, validated_data):

        password=validated_data.get("password")
        instance=User(**validated_data)
        if password is not None:
            instance.set_password(password)
            instance.save()
        return instance
            
    def update(self, instance, validated_data):

        password=validated_data.get("password",None)
        if password:
            instance.set_password(password)
        instance.save()
        return instance
