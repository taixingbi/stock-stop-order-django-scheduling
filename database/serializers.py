from rest_framework import serializers
from .models import Peak, Valley, Order_placed
from rest_framework import filters

class PeakSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Peak
        fields = ['symbol', 'peak', 'timestamp']

class ValleySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Valley
        fields = ['symbol', 'valley', 'timestamp']

class Order_placedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Valley
        fields = ['symbol', 'order_id', 'side', 'quantity', 'price', 'limit', 'stop']

# class Teleconference_transcribeSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Teleconference_transcribe
#         fields = ['filename', 'transcription', 'transcription_baseline']