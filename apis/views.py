from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from apis.models import NewsItems
from apis.serializers import NewsSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

class JsonResponse(HttpResponse):
	def __init__(self,data,**kwargs):
		content = JSONRenderer().render(data)
		kwargs['content_type'] = 'application/json'
		super(JsonResponse, self).__init__(content, **kwargs)

@csrf_exempt
def get_news(request):
	if request.method == 'POST':
		data = JSONParser().parse(request)
		if 'language' not in data:
			lang = 'eng'
		else:
			lang = data.get('language')
		if 'count' not in data:
			limit = 10
		else:
			limit = data.get('count')
		news = NewsItems.objects.filter(language=lang)[:limit]
		serialized_news = NewsSerializer(news,many=True)
		
		return JsonResponse(serialized_news.data)

@csrf_exempt
def add_news(request):
	if request.method == 'POST':
		data = JSONParser().parse(request)
		serialized_news = NewsSerializer(data=data)
		if serialized_news.is_valid():
			serialized_news.save()
			return JsonResponse(serialized_news.data, status=201)

		return JsonResponse(serialized_news.errors, status=400)

# function based viewscd
@api_view(['POST'])
def get_news2(request):
	if request.method == 'POST':
		data = request.data
		if 'language' not in data:
			lang = 'eng'
		else:
			lang = data.get('language')
		if 'count' not in data:
			limit = 10
		else:
			limit = data.get('count')
		news = NewsItems.objects.filter(language=lang)[:limit]
		serialized_news = NewsSerializer(news,many=True)

		return Response(serialized_news.data,status=status.HTTP_200_OK)
	return Response(status=status.HTTP_404_NOT_FOUND)

