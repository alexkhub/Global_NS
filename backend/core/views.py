from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import redirect, render
# Create your views here.
from rest_framework.generics import CreateAPIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework.response import Response
import requests


class IndexView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'core/index.html'

    def get(self, request, format=None):
        return Response({})

    def post(self, request, format=None):
        headers = {'Content-Type': 'application/json',
                   'Authorization': 'Bearer RLPUUOQAMIKSAB2PSGUECA'
                   }
        r = requests.post(url='https://order.drcash.sh/v1/order', json={
            "stream_code": "vv4uf",
            "client": {
                "phone": request.data['phone'],
                "name": request.data['name']
            }
        }, headers=headers)

        if r.status_code == 200:
            return HttpResponseRedirect(reverse('index2'))
        else:
            return Response({})


class Index2View(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'core/index2.html'

    def get(self, request, format=None):
        return Response({})
