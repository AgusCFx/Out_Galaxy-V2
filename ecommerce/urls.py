from django.urls import path
from . import views

"""
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
"""

urlpatterns = [
    path("", views.home, name="home"),
    path("naves/<int:id>", views.nave, name="nave")
]
