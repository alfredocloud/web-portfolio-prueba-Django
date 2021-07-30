from django.urls import path
from portfolio import views

app_name = 'portfolio'

urlpatterns = [

    path('', views.portfolio, name ='portfolio'),
    path('<int:project_id>/', views.detail, name ='detail'),

]