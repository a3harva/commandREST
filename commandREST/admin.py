from django.contrib import admin
from commandREST import models as command_rest_models
# Register your models here.
admin.site.register(command_rest_models.User)
admin.site.register(command_rest_models.Command)