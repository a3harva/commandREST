from django.urls import path
from commandREST import views as command_views

urlpatterns = [
    path("test/", command_views.TestHandler.as_view(), name="test-view"),
    path("user/", command_views.UserHandler.as_view(), name="user-views"),
    path("command/", command_views.CommandHandler.as_view(), name="command-views"),
]
