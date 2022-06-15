from django.urls import path
from . import views


app_name = 'studies'
urlpatterns = [
    path('', views.studies_view, name='studies-list'),
    # path('<slug:slug>/details/', views.designs_details_view, name='design-detail'),
]
