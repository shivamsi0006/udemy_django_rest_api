from django.shortcuts import render
from django.core.serializers import serialize
from django.http import JsonResponse,HttpResponse
from django.views.generic import View
from .models import update
import json


def update_model_detail_view(request):
    data={
        "count":1000,
        "content":"some json content"
    }

    return JsonResponse(data)

# Create your views here.


class JsonCBV(View):
    def get(self):
        data={
        "count":1000,
        "content":"some json content"
    }
        return JsonResponse(data)
    

class SerializedDetailView(View):
    def get(self,request):
        obj=update.objects.get(id=1)
        data={
            "count":obj.user.username,
            "content":obj.content
        }
        json_data=json.dumps(data)

        return HttpResponse(json_data,content_type='application/json')
    


class SerializeListView(View):
    def get(self,request):
        qs=update.objects.all()
        data=serialize("json",qs,fields=('user','content'))
        
        return HttpResponse(data,content_type='application/json')


