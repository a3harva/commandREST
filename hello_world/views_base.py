import json
import logging
import os

from hello_world.core import utils as core_utils

from rest_framework import response as rest_framework_response
from rest_framework import views as rest_framework_views


from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect


class BaseHandler(rest_framework_views.APIView):
    def process_get_request(self, parameters, kwargs):

        return {"method": "get"}

    def process_post_request(self, parameters, body, kwargs):
        return {"method": "post"}

    def process_put_request(self, parameters,body, kwargs):
        return {"method": "put"}

    def process_delete_request(self, parameters, kwargs):
        return {"method": "delete"}

    def get(self, request, **kwargs):
        kwargs = core_utils.decode_request_kwargs(request)
        parameters = core_utils.decode_request_parameters(request)
        response = self.process_get_request(parameters, kwargs)

        if not isinstance(response, HttpResponse):
            response = rest_framework_response.Response(response)

        return response

    def post(self, request, **kwargs):
        kwargs = core_utils.decode_request_kwargs(request)
        parameters = core_utils.decode_request_parameters(request)
        body = core_utils.decode_request_body(request)
        response = self.process_post_request(parameters, body, kwargs)

        if not isinstance(response, HttpResponse):
            response = rest_framework_response.Response(response)

        return response

    def put(self, request, **kwargs):
        kwargs = core_utils.decode_request_kwargs(request)
        parameters = core_utils.decode_request_parameters(request)
        body = core_utils.decode_request_body(request)
        response = self.process_put_request(parameters, body, kwargs)

        if not isinstance(response, HttpResponse):
            response = rest_framework_response.Response(response)

        return response

    def delete(self, request, **kwargs):
        kwargs = core_utils.decode_request_kwargs(request)
        parameters = core_utils.decode_request_parameters(request)
        response = self.process_delete_request(parameters,kwargs)

        if not isinstance(response, HttpResponse):
            response = rest_framework_response.Response(response)

        return response
