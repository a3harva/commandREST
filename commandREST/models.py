from django.db import models

# Create your models here.
from hello_world.core import models as core_models

class User(core_models.BaseModel):
    email = models.CharField(max_length=255)
    pin = models.IntegerField(unique=True)
    password = models.CharField(max_length=255, unique=True)

    def to_json(self):
        obj_dict = super().to_json()
        response_dict={}
        response_dict["id"]= obj_dict.get("id")
        response_dict["email"]= obj_dict.get("email")
        response_dict["pin"]=obj_dict.get("pin")
        response_dict["password"]=obj_dict.get("password")
        response_dict["createdOn"]=obj_dict.get("created_on")
        response_dict["updatedOn"]=obj_dict.get("updated_on")
        response_dict["createdBy"]=obj_dict.get("created_by")
        response_dict["updatedBy"]=obj_dict.get("updated_by")
        return response_dict

    @classmethod
    def get_user_by_email(cls,user_email):
        user_object=None
        try:
            user_object=cls.objects.get(email=user_email)
            print(user_object)
        except Exception as exc:
            print(exc)

        return user_object

    @classmethod
    def get_all_users(cls):
        user_queryset=None
        try:
            user_queryset = cls.objects.all()
            print(user_queryset)
        except Exception as exc:
            print(exc)

        return user_queryset
    
    @classmethod
    def add(cls,email,password,pin,user_email):
        user_object= None
        try:
            print(pin,"in add")
            user_object = cls.objects.create(
                email=email,
                pin=pin,
                password=password,
                created_by=str(user_email).strip().lower(),
                updated_by=str(user_email).strip().lower(),
            )
        except Exception as exc:
            print(exc)
        return user_object

    @classmethod
    def remove(cls,id):
        success=False
        try:
            cls.objects.get(id=id).delete()
            success = True
        except Exception as exc:
            print(exc)
        return success