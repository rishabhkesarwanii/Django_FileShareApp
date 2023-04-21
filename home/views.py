from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from home.serailizers import FileListSerializer
# Create your views here.


def home(request):
    return render(request, 'home.html')

def download(request, uid):
    return render(request, 'download.html', context = {'uid': uid})

class HandleFileUpload(APIView):
    # parser_classes = [MultiPartParser]
    def post(self, request):
        try:
            data = request.data
            serializer = FileListSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status': 200,
                    'message': 'Files uploaded successfully',
                    'data' : serializer.data
                })
            return Response({
                'status': 400,
                'message': 'Invalid data',
                'data': serializer.errors
            })
        except Exception as e:
            print(e)
        