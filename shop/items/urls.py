from django.urls import path
from .views import catalog, shoe_detail

urlpatterns = [
    path('', catalog, name='shoes_catalog'),
    path('<int:id>/', shoe_detail, name='shoes_detail')
]