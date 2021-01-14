from rest_framework import serializers
from .models import Course

class GetAllCourseSerializer(serializers.ModelSerializer):
    #Nhận từ database về client theo dạng nào đó
    class Meta:
        model = Course
        fields = ('id','title')
        
class PostCourseSeralizer(serializers.Serializer):
    # gửi từ client lên=> xác thực thấy ok  thì nhét vô database
    title1 = serializers.CharField(max_length=20)
    price1 = serializers.IntegerField()
    content1 = serializers.CharField(max_length=20)
    