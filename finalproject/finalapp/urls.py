from django.urls import path,include
from finalapp import views
app_name = 'finalapp'
urlpatterns=[
    path('signup/', views.signup, name='signup_page'),
    path('signin/',views.signin, name='signin_page'),
]
