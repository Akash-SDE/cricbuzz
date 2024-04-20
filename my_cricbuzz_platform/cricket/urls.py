from django.urls import path
from .import views

urlpatterns=[
    path('base/', views.base_view, name="base"),
    path('news/<int:pk>/', views.news_detail, name='news'),
    path('', views.home, name='home'),
    path('profile/', views.profile_view, name='profile'),
    path('series/', views.series_list, name='profile'),
    path('news/', views.news_list, name='profile'),

]