from django.urls import path
from . import views



urlpatterns=[
    path('qarzlar/',views.QarzPage,name='qarzlar'),
    path('qarz-yaratish/',views.QarzCreate,name='qarz-yaratish'),
    path('qarz-tahrirlash/<str:pk>/',views.QarzUpdate,name='qarz-tahrirlash'),
    path('qarz-delete/<str:pk>/',views.QarzDelete,name='qarz-delete'),
    path('',views.loginUser,name='login')
]