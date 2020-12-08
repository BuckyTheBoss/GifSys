from django.urls import path
from . import views
urlpatterns = [
    path('add_gif/', views.add_gif, name='add_gif'),
    path('view_gif/<int:id>', views.view_gif, name='view_gif'),
    path('view_categories/', views.view_categories, name='view_categories'),
    path('view_category/<int:id>', views.view_category, name='view_category'),
    path('', views.homepage, name='homepage'),
    path('like_gif/<int:id>/<int:mode>', views.like_gif, name='like_gif'),
    path('trending/', views.view_gifs_by_like, name='trending')

]
