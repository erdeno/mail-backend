from django.urls import path, include

from mailapp import views

urlpatterns = [    
    path("emails/<str:mailbox>", views.EmailsList.as_view()),
    path("email/<int:emailId>", views.EmailDetail.as_view()),
]

