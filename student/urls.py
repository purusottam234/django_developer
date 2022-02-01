from django.urls import URLPattern, path
from .views import  *

urlpatterns = [
    #common django urls
    path('',StudentListView.as_view(),name='home'),
    path('student/new/', StudentCreateView.as_view(), name='student_new'),
    path('student/<int:pk>/edit/', StudentUpdateView.as_view(), name='student_edit'),
    path('student/<int:pk>/delete/',StudentDeleteView.as_view(), name='student_delete'),

   # Restapi urls
    path('api/',StudentApi.as_view()),
    path('api/create',StudentCreateApi.as_view()),
    path('api/<int:pk>',EmployeeUpdateApi.as_view()),

    path('api/<int:pk>/delete',StudentDeleteApi.as_view()),
]