from rest_framework import serializers
from apis.models import NewsItems

class NewsSerializer(serializers.ModelSerializer):
	language = serializers.CharField(default='eng',allow_blank=True,
										trim_whitespace=True,max_length=50)
	class Meta:
		model = NewsItems
		fields = ('title','body','language')
