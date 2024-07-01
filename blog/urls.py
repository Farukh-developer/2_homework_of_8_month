from django.urls import path, include
from .views import (CoursesCreateViewList, CoursesUpdateDeleteView, TeachersCreateViewList, TeachersUpdateDeleteView, StudentsCreateViewList, StudentsUpdateDeleteView
    )

urlpatterns = [
    
    path('api/v1/course/', CoursesCreateViewList.as_view()),
    path('api/v1/course/<int:pk>/', CoursesUpdateDeleteView.as_view()),
    
    path('api/v1/teacher/', TeachersCreateViewList.as_view()),
    path('api/v1/teacher/<int:pk>/', TeachersUpdateDeleteView.as_view()),
    
    path('api/v1/student/', StudentsCreateViewList.as_view()),
    path('api/v1/student/<int:pk>/', StudentsUpdateDeleteView.as_view()),
    
    
    
    
    
    path('api-auth/', include('rest_framework.urls'))
    
    
]
