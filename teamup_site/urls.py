from django.urls import path
from . import views
from .views import index, ProjectCreateView, ProjectList, ProfileView


app_name = 'teamupweb'

urlpatterns = [
    path('', index.as_view(), name='index'),
    path('test/', views.test, name='test'),
    path('projectList/', ProjectList.as_view(), name='projectlist'),
    path('postproject/', ProjectCreateView.as_view(), name='postproject'),
    path('Detail/<int:pk>/', views.ProjectDetail, name='detail'),
    #path('<int:pk>/delete/', views.Pro, name='projectdelete'),
    path('profile/<str:username>/', ProfileView.as_view(), name='profile'),
    path('help/', views.Help, name='help'),
]