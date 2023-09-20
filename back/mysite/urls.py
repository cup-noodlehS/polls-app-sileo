from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    # path("polls/", include("polls.urls")),
    path('api-sileo/', include(('sileo.sileo.urls', 'sileo'), namespace='sileo'))
    # path("", redirect("polls")),
]
