from updates.models import update
from django.http import HttpResponse
from django.views.generic import View

class UpdateModelDetailApiView(View):
    def get(self,request,id):

        obj=update.objects.get(id=id)
        json_data=obj.serialize()
        return HttpResponse(json_data,content_type='application/json')
        
    def post(self,request):
        pass
    def put(self,request):
        pass
    def delete(self,request):
        pass



class UpdtaeModelListApiView(View):
    def get (self,request):
        obj=update.objects.all()
        json_data=obj.serialize()
        return HttpResponse(json_data,content_type='application/json')
    
    def post(self,request):
        pass
    def put(self,request):
        pass
    def delete(self,request):
        pass