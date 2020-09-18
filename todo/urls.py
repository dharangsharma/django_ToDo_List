from django.urls import path
from . import views
urlpatterns = [
    
    path('', views.index , name='index'),
    path('add', views.addTodo , name='add'),
    path('completed/<todo_id>', views.completed, name='complete'),
    path('delete_completed', views.deleteCompleted, name = 'deleteCompleted'),
    path('delete_all',views.deleteAll,name='deleteAll')
]
