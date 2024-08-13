from updates.models import update
from django.http import HttpResponse
from django.views.generic import View

from updates.forms import UpdateModelForm

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
        json_data=obj.all()
        return HttpResponse(json_data,content_type='application/json')
    
    def post(self,request):
        form=UpdateModelForm(request.POST)
        if form.is_valid():
            obj=form.save(commit=True)
            obj_data=obj.serialize()
            return HttpResponse(obj_data,content_type='application/json')

    def put(self,request):
        pass
    def delete(self,request):
        pass