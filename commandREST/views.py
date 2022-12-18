from django.shortcuts import render 
from hello_world.views_base import BaseHandler
from commandREST import models as command_rest_models
import typing 
# Create your views here.


class TestHandler(BaseHandler):
    def process_get_request(self, parameters, kwargs):
        print(parameters,kwargs)
        
        return {"success":"true","data":"nothing"}
    
    def process_post_request(self, parameters, body, kwargs):
        print(parameters, body, kwargs)
        return {"success":"true"}

class UserHandler(BaseHandler):
    def process_get_request(self,parameters,kwargs):
        response_dict: dict[str, typing.Union[bool, str, list, dict]] ={"success":False}        
        user_email = parameters.get("userEmail")
        print(user_email)
    
        if user_email:
            user_object = command_rest_models.User.get_user_by_email(user_email)
            if user_object:
                response_dict["success"]=True
                response_dict["data"] = user_object.to_json()

        else:
            user_objects = command_rest_models.User.get_all_users()
            response_dict["success"] = True
            response_dict["data"] = {"users":[]}
            for a_obj in user_objects:
                response_dict["data"]["users"].append(a_obj.to_json()) 

        return response_dict 

    def process_post_request(self, parameters, body, kwargs):
        response_dict: dict[str, typing.Union[bool, str, list, dict]] ={"success":False}
        email = body.get("email","")
        pin = body.get("pin",1234)
        print(body)
        print(pin)
        password = body.get("password","testPassword")
        user_email = body.get("userEmail")

        user_object = command_rest_models.User.add(email,password,pin,user_email)
        if user_object:
            response_dict["success"]=True
            response_dict["data"]={
                "user":user_object.to_json()
            }
        else:
            response_dict["success"]=False
            response_dict["message"]="system error"

        return response_dict


    def process_delete_request(self,parameters,kwargs):
        response_dict: dict[str, typing.Union[bool, str, list, dict]] ={"success":False}

        id = parameters.get("id",None)
        
        if id:
            command_rest_models.User.remove(id)
            response_dict["success"] = True
        
        return response_dict


class CommandHandler(BaseHandler):

    def process_get_request(self, parameters, kwargs):
        response_dict: dict[str, typing.Union[bool, str, list, dict]] ={"success":False}        
        search_text = parameters.get("searchText","")
        catagory = parameters.get("catagory","")
        user_email = parameters.get("userEmail","")

        if search_text is not None:
            qs = command_rest_models.Command.list(search_text, catagory, user_email)
            if not qs:
                response_dict["message"]="could not find commands"
                return response_dict
            
            response_dict["success"] = True

            response_dict["data"]={"commands":[]}
            for a_obj in qs:
                response_dict["data"]["commands"].append(a_obj.to_json())

        return response_dict

    def process_post_request(self, parameters, body, kwargs):
        response_dict: dict[str, typing.Union[bool, str, list, dict]] ={"success":False}        
        name = body.get("name")
        text =body.get("text")
        description=body.get("description")
        catagory=body.get("catagory")
        user_email= body.get("userEmail")

        result =command_rest_models.Command.add(name, text, description, catagory, user_email)
        if result:
            response_dict["success"]= True
            response_dict["data"]={
                "command":[result.to_json()]
            }
            
        return response_dict