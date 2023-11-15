from django.urls import path
from . import views

app_name = 'clean_excel'

urlpatterns = [
    path('', views.clean_excel_data, name='clean_excel')

]