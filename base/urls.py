from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),
    path('', views.home, name="home"),

    path('reports/', views.report, name="user-reports"),
    path('create-report/', views.createReport, name="create-report"),
    
    path('update-user/', views.updateUser, name="update-user"),
  
    path('staff-reports/', views.staffReports, name="staff-reports"),
    path('update-report/<str:pk>/', views.updateReport, name="update-report"),
    path('delete-report/<str:pk>/', views.deleteReport, name="delete-report")
]