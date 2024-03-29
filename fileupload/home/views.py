from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from home.serializers import FileListSerializer 
from rest_framework.parsers import MultiPartParser 
# Create your views here.

def home(request):
    return render(request,'home.html')

def download(request,uid):
    return render(request,'download.html',context = {'uid' : uid})


class HandleFiles(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request):
        try:
            data = request.data
            serializer = FileListSerializer(data=data)  # Corrected instantiation

            if serializer.is_valid():
                serializer.save()  
                return Response({
                    'status': 200,
                    'message': "Data added successfully"
                })
            return Response({
                'status': 400,
                'message': "Something is wrong",
                'data': serializer.errors  # Corrected accessing errors
            })
        except Exception as e:
            print(e)
            return Response({
                'status': 500,
                'message': str(e),
            })