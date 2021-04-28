from django.urls import path
from bibl import views
app_name = 'bibl'

urlpatterns = [
    path('', views.index, name='index'),
]