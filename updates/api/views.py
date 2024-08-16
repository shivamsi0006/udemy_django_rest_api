from updates.models import update
from django.http import HttpResponse
from django.views.generic import View
from updates.forms import UpdateModelForm
from .mixins import CSRFExemptMixin

import json



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



class UpdtaeModelListApiView(CSRFExemptMixin,View):

    def get (self,request):
        obj=update.objects.all()
        json_data=obj.all()
        return HttpResponse(json_data,content_type='application/json')
    
    def post(self,request):
        
        form=UpdateModelForm(request.POST)
        if form.is_valid():
            obj=form.save(commit=True)
            data=obj.serialize()
            json_data=json.loads(data)
            
            
            if json_data.get("content")==" ":
                data={
                    "user":data.get("user"),
                    "message":"could not update"
                }
                return HttpResponse(data,content_type='application/json')
            return HttpResponse(data,content_type='application/json')
        return HttpResponse({'message':'message'},content_type='application/json')

    def put(self,request):
        form=UpdateModelForm(request.POST)
        if form.is_valid():
            obj=form.save(commit=True)
            data=obj.serialize()
            return HttpResponse(data,content_type='application/json')
        return HttpResponse("invalid creditional",content_type='application/json')


    def delete(self,request):
        pass 