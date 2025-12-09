from django.urls import path
from . import views

urlpatterns = [
    path("status/", views.get_server_status, name="api-status"),
    path("errors/", views.get_errors, name="api-errors"),
    path("error/<int:code>/", views.get_error_from_code, name="api-error-by-code"),
    path("error/create/", views.create_error, name="api-error-create"),
    path("error/<int:code>/edit/", views.error_update_delete, name="api-error-update-delete"),
]
