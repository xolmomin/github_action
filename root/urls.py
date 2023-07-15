from django.contrib import admin
from django.urls import path


def view(request):
    import socket
    _id = socket.gethostname()
    return _id


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view)
]
