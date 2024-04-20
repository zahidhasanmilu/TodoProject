from django.urls import path
from todoapp import views


urlpatterns = [
    path('', views.home, name="home"),
    path('register/', views.register, name="register"),
    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_page, name="logout"),
    
    path('upadate/<int:id>/', views.upadate_task, name="update"),
    path('delete_task/<int:id>/', views.delete_task, name="delete"),
    
]
