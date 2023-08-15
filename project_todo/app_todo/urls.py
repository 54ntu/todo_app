from django.urls import path
from .views import taskApiView,taskApiIDView


urlpatterns = [
    path('tasks/', taskApiView.as_view()),
    path('tasks/<int:id>/',taskApiIDView.as_view()),
    
]
