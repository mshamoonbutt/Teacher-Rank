
from django.urls import path
from ..app.views import rank_teachers

urlpatterns = [
    # ...existing code...
    path('rank/', rank_teachers, name='rank_teachers'),
    # ...existing code...
]