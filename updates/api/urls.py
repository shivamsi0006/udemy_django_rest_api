
from django .urls import path
from .views import UpdateModelDetailApiView,UpdtaeModelListApiView


urlpatterns= [
    path('<int:id>/',UpdateModelDetailApiView.as_view(),name='updatemodel'),

]