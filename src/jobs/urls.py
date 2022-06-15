from django.urls import path
from . import views


app_name = 'jobs'
urlpatterns = [
    path('', views.jobs_view, name='jobs-list'),
    # path('<slug:slug>/details/', views.designs_details_view, name='design-detail'),
]
