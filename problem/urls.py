from django.urls import path
from . import views

urlpatterns = [ 
    path('logic/', views.LogicView.as_view(), name='usercreate'),
    path('combination/',views.CombinationView.as_view(), name='usercreate'),
    path('geometry/',views.GeometryView.as_view(), name='usercreate')
               ]
