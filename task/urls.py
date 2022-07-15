from django.urls import path
from . import views

urlpatterns = [
    path('signup', views.signup),
    path('signin', views.signin),
    path('task', views.task_list),
    path('task/new', views.new_task),
    path('task/<int:id>', views.get_one_task),
    path('task/done/<int:id>', views.done_task),
    path('task/edit/<int:id>', views.edit_task),
    path('task/delete/<int:id>', views.delete_task),
]
