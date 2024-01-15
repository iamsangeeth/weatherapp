from rest_framework import serializers

class SearchSerializer(serializers.Serializer):
    text = serializers.CharField()
    
