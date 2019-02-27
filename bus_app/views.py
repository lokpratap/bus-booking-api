from django.shortcuts import render
# from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# from rest_framework import viewsets
from .models import Posts
from .serializers import PostSerializer
from rest_framework import status
# Create your views here.



# def index(request):
#     return HttpResponse('Hello')

#
# class PostsView(viewsets.ModelViewSet):
#     queryset = Posts.objects.all()
#     serializer_class = PostSerializer


# posts/
class PostsView(APIView):
    serializer_class = PostSerializer

    def get(self, request):
        pst = Posts.objects.all()
        serializer = PostSerializer(pst, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(data= request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




