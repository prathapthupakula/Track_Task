from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from .models import QuestionData, TrackData, ChoiceData

class TrackDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrackData
        fields = '__all__'

class QuestionDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionData
        fields = '__all__'
        depth = 1
#
class ChoiceDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChoiceData
        fields = '__all__'
        depth=1
class QuestionDataGETSerializer(serializers.ModelSerializer):

    track = TrackDataSerializer()
    track = serializers.StringRelatedField(many=True)

    class Meta:
        model = QuestionData
        fields = '__all__'


# class TrackSerializer(serializers.ModelSerializer):
#     # avatar_set = QuestionDataSerializer(source='questiondata_track', many=True)
#     class Meta:
#         model = Track
#         fields = '__all__'
#
# class QuestionDataSerializer(serializers.ModelSerializer):
#     track=TrackSerializer()
#     # track_id = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
#     class Meta:
#         model = QuestionData
#         fields = '__all__'

# class QuesViewSet(viewsets.ModelViewSet):
#     queryset = QuestionData.objects.all()
#     serializer_class = QuesSerializer
#
# class ChoiceViewSet(viewsets.ModelViewSet):
#     queryset = Choice.objects.all()
#     serializer_class = ChoiceSerializer

# class TrackViewSet(viewsets.ModelViewSet):
#     queryset = Track.objects.all()
#     serializer_class = TrackSerializer


# class Data1Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = Data1
#         fields = '__all__'
# class Choice1Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = Choice1
#         fields = '__all__'