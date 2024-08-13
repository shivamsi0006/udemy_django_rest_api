
from django .urls import path
from .views import UpdateModelDetailApiView,UpdtaeModelListApiView


urlpatterns= [
    path('',UpdtaeModelListApiView.as_view(),name='list view'),
    path('<int:id>/',UpdateModelDetailApiView.as_view(),name='updatemodel'),

]