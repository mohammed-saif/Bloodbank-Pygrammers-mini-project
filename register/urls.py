from django.urls import path

from . import views 

urlpatterns=[
    path('',views.login,name='login'),
    path('login',views.login,name='login'),
    path('add-donor',views.add_donor,name='add_donor'),
    path('display',views.display,name='display'),
    path('signup',views.signup,name='signup'),
    path('logout',views.logout,name='logout')
]