from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('', views.index, name='index'),
    path('write/', views.write, name='write'),
    path('read/<int:Did>', views.read, name='read'),
    path('delete/<int:Did>',  views.delete, name='delete'),
    path('edit/<int:Did>', views.edit, name='edit'),
    path('comment/<int:Did>', views.comment, name='comment'),
    path('comment/delete/<int:Cid>', views.comment_delete, name='comment_delete')
]