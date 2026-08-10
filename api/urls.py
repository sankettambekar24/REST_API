from django.urls import  path
from . import views
 

urlpatterns=[
    path('students/', views.studentsview),
    path('students/<int:pk>/', views.studentsDetailView),

    path('employee/', views.EmployeeList.as_view()),
    path('employee/<int:pk>/', views.EmployeeDetail.as_view()),

    path('blogs/', views.BlogView.as_view()),
    path('blogs/<int:pk>/',views.BlogDetailView.as_view()),

    path('comments/', views.CommentView.as_view()),
        path('comments/<int:pk>/',views.CommentDetailView.as_view()),

]