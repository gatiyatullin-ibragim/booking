from django.urls import path
from . import views

app_name = 'listings'

urlpatterns = [
    # Главная страница каталога (корень приложения)
    path('', views.catalog_view, name='catalog'),
    # Страница конкретного жилья
    path('<int:pk>/', views.listing_detail_view, name='detail'),
]