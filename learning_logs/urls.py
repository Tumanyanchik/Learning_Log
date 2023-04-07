"""URLs shemes for learning_logs"""
from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page with all topics
    path('topics/', views.topics, name='topics'),
    # Page with information about 1 theme
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # Page with information for new theme
    path('new_topic/', views.new_topic, name='new_topic'),
    # Page for new entries
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # Page for edit entries
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]
