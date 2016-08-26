from rest_framework import serializers
from apis.models import NewsItems

class NewsSerializer(serializers.ModelSerializer):
	class Meta:
		model = NewsItems
		fields = ('title','body','language')
