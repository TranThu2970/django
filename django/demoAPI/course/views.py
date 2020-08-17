from django.shortcuts import render
#class views
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Course
from .serializers import GetAllCourseSerializer, PostCourseSeralizer
# Create your views here.

class GetAllCourses(APIView):

    def get(self,request):
        #lấy dữ liệu từ database
        listCourse = Course.objects.all()
        #Nhieu object nen many=true
        #Qua serial de ve client
        mydata  = GetAllCourseSerializer(listCourse, many=True)
        return Response(data=mydata.data ,status=status.HTTP_200_OK)
    
    def post(self,request):
        #Lấy dữ liệu từ client thông quá Serializer => trả về kiểu JSON
        mydata = PostCourseSeralizer(data=request.data)
        #Xác thực xem có đúng kiểu được quy định không
        if not mydata.is_valid():
            return Response('Sai dữ liệu roài!', status=status.HTTP_400_BAD_REQUEST)
        #Xử lý dữ liệu nhận được
        title = mydata.data["title1"]
        price = mydata.data["price1"]
        content = mydata.data["content1"]
        #Thêm vô database
        cs = Course.objects.create(title=title,price=price,content=content)
        #Thông báo ra coi sao
        return Response(data=cs.id, status=status.HTTP_200_OK)
