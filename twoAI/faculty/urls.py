from django.urls import path
from faculty import views

urlpatterns = [
    path('',views.faculties, name = 'faculties'),
]
