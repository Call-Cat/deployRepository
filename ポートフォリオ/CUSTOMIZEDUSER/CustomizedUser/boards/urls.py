from django.urls import path
from . import views

app_name = 'boards'

urlpatterns = [
    path('create_memo', views.create_memo, name='create_memo'),
    path('list_memos', views.list_memos, name='list_memos'),
    path('edit_memo/<int:id>', views.edit_memo, name='edit_memo'),
    path('delete_memo/<int:id>', views.delete_memo, name='delete_memo'),
]
