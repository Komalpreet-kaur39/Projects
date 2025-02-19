from django.urls import path
from .views import calculator  # Import your view

urlpatterns = [
    path("calculate/", calculator, name="calculator"),  # Correct endpoint
]
