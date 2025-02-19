# from django.urls import path
# from .views import calculator  # Import your view

# urlpatterns = [
#     path("calculate/", calculator, name="calculator"),  # Correct endpoint
# ]
from django.urls import path
from .views import calculator ,clear_history # Import your view

urlpatterns = [
    path("calculate/", calculator, name="calculator"),  # Correct endpoint
    path('clear-history/', clear_history, name='clear_history'),
]
