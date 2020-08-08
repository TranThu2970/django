from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

# Create your views here.
def index(request):
    #Truyền biến vào
    myName = "Trần Thu"
    myProperty = ['Family','House','Money']
    return render(request, 'polls/index.html', {'name':myName, 'property':myProperty})

def viewList(request):
    DanhSach = Question.objects.all()
    context = {'dSach': DanhSach}
    return render(request, 'polls/list.html', context)

def viewDetail(request,question_id):
    #lấy tất cả giá trị có trong một object của Question
    q = Question.objects.get(pk=question_id)
    return render(request, 'polls/detail.html', {'qs':q})

def vote(request,question_id):
    q = Question.objects.get(pk=question_id)
    try:
        #Lấy kết quả được chọn gửi đến server: cái value được chọn 
        #"choice" là tên của cái radio được chọn bên detail.html
        #value trả về chính là 'choice.id'
        #Nhận dữ liệu từ form nhưng ko cần tạo formModels
        value_id = request.POST["choice"]
        c = q.choice_set.get(pk=value_id)
        c.vote = c.vote +1
        c.save()                
    except:
        #HttpResponse("Lỗi không có dữ liệu Choice")
        pass
    
    return render(request,'polls/result.html', {'q':q})