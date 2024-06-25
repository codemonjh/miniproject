from django.shortcuts import render
from rest_framework.views import APIView
from openai import OpenAI
from config.settings import OAI_API_KEY
# Create your views here.
client = OpenAI(api_key=OAI_API_KEY)

class LogicView(APIView):
    def post(self,request):
        pass