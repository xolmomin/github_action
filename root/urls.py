from django.contrib import admin
from django.urls import path
from django.http.response import JsonResponse


def view(request):
    import socket
    _id = socket.gethostname()
    return JsonResponse({"result": _id})


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view)
]
