from django.db import models
import uuid 
from itertools import chain
import datetime
from hello_world.core import utils as core_utils

# Create your models here.
class BaseModel(models.Model):
    id = models.CharField(default=uuid.uuid4, max_length=50, primary_key=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=50,blank=True,null=True)
    updated_by = models.CharField(max_length=50,blank=True,null=True)

    class Meta:
        abstract = True

    def to_json(self):
        response_json = {}
        opts = self._meta

        for data in chain(opts.concrete_fields, opts.private_fields):
            value = data.value_from_object(self)
            if isinstance(value, datetime.datetime):
                value = core_utils.convert_to_datetime_string(value)
            elif isinstance(value, datetime.date):
                value = core_utils.convert_to_date_string(value)
            elif isinstance(value, uuid.UUID):
                value = str(value)
            response_json[data.name] = value

        return response_json


