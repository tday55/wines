from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:wine_id>/', views.wine, name='onewine'),
    path('<int:location_id>/slots/', views.slots, name='slots'),
    path('<int:wine_id>/regions/', views.types, name='region'),
    path('makers/<int:maker_id>/', views.makers, name='onemaker'),
    path('appellation/<str:appellation_in>/', views.appellations, name='oneappellation'),
]
