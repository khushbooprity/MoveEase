from django.urls import path
from Admin_panel import  views
urlpatterns = [
   path('dashboard/', views.dashboard, name="dashboard")

]
