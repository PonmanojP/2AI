from Domains import views
from django.urls import path

urlpatterns = [
    path('ml/',views.ML_view, name = 'ml'),
    path('dl/',views.DL_view, name = 'dl'),
    path('vision/',views.Vision_view, name = 'vision'),
    path('bigdata/',views.Bigdata_view, name = 'bigdata'),
    path('edge/',views.Edge_view, name = 'edge'),
    path('nlp/',views.NLP_view, name = 'nlp'),
    path('cloud/',views.Cloud_view, name = 'cloud'),
    path('web/',views.Web_view, name = 'web'),
    path('design/',views.Design_view, name = 'design'),
]