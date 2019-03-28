from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from rest_framework import generics,viewsets
from rest_framework.views import APIView
from .models import QuestionData,TrackData,ChoiceData
from .api import TrackDataSerializer,QuestionDataSerializer,ChoiceDataSerializer,QuestionDataGETSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.db import connection
from django.views.generic import View
from .utils import is_json
from .mixins import HttpResponseMixin,SerializeMixin
import json


class TestCRED(HttpResponseMixin,SerializeMixin,View):
    def get_id_based_data(self,id):
        try:
            # s=QuestionData.objects.get(id=id)
            s=QuestionData.objects.get(id=id)
        except QuestionData.DoseNotExist:
            s=None
        return s

    def get(self,request,*args,**kwargs):
        data=request.body
        data=json.dumps({'id':1})
        valid_json=is_json(data)
        if not valid_json:
            return self.render_to_http_respone(json.dumps({"msg":"Not valid json data"}),status=400)
        pdata=json.loads(data)
        id=pdata.get('id',None)
        if id is not None:
            Qdata=self.get_id_based_data(id)
            if Qdata is None:
                return self.render_to_http_respone(json.dumps({"msg": "No record founded"}), status=400)
            json_data=self.serialize([Qdata,])
            return self.render_to_http_respone(json_data)
        qs=QuestionData.objects.all()
        json_data=self.serialize(qs)
        return self.render_to_http_respone(json_data)




# @api_view(['GET','POST'])
#
# def TrackData(request):
#     if request.method == 'GET':
#         tracks = TrackData.objects.all()
#         serializer = TrackDataSerializer(tracks, many=True)
#         return Response(serializer.data)
#     if request.method == 'POST':
#         serializer = TrackDataSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# @api_view(['GET', 'PUT', 'DELETE'])
#
# def QuestionData2(request,pk):
#     try:
#         cursor1 = connection.cursor()
#         snippet = QuestionData.objects.get(track_id=pk)
#         serializer_class = QuestionDataGETSerializer
#         # print(snippet)
#         # queary = "select * from newapp_questiondata where track_id="+str(pk)
#         # cursor1.execute(queary)
#         # rowdata=[]
#         # for row in cursor1.fetchall():
#         #     rowdata.append(row)
#         # return Response(rowdata)
#         # exit()
#     except QuestionData.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = QuestionDataSerializer(snippet)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = QuestionDataSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
class TrackViewSet(viewsets.ModelViewSet):
    queryset = TrackData.objects.all()
    serializer_class = TrackDataSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = QuestionData.objects.all()
    serializer_class =QuestionDataSerializer
class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = ChoiceData.objects.all()
    serializer_class =ChoiceDataSerializer

class QuestionData2ViewSet(viewsets.ModelViewSet):
    queryset = QuestionData.objects.all()
    serializer_class =QuestionDataGETSerializer