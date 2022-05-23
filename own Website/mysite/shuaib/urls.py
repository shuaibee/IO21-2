
from django.urls import path
from . import views

app_name='shuaib'

urlpatterns = [
    path('', views.IndexView.as_view(),name="home"),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('about/',views.about,name="about"),
    path('projects/',views.projects,name="projects"),
    path('contact/',views.contact,name="contact"),

]
