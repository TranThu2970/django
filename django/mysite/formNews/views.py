from django.shortcuts import render
from django.http import HttpResponse
from .forms import PostForm,EmailForm
from django.views import View


# Create class base view
#class kế thừa từ view

class indexClass(View):
    #get: như request: nhập địa chỉ, click vào link,..
    def get(self,request):
        return HttpResponse("Hello World")

#def add_post(request):
#    #model=>form=>views
#    a = PostForm()      #form đẩy sang template
#    return render(request, "news/add_new.html", {'f':a})    
#Khi dùng class base view dạng 'post' thì không cần dùng if để kiểm tra xem có phải post ko
class save_news_class(View):
    #if request.method =="POST":
        #xem form gửi lên cái chi
    def get(self,request):
        #form hiển thị trên template của client với các field của model để lấy dữ liệu
        a = PostForm()      
        #lấy dữ liệu từ form để hiển thị trên client
        return render(request, "news/add_new.html", {'f':a})          
        #nếu muốn vừa get vừa post trong một class


    def post(self,request):
        #Dữ liệu về database khi nhấn submit
        g = PostForm(request.POST)
        if g.is_valid():
            g.save()
            return HttpResponse("Lưu OK")
        else:
            return HttpResponse("Không validate")
    #else:
        #return HttpResponse("Không phải Post request")

def sendEmail(request):
    #lấy dạng form để hiển thị lên template
    e = EmailForm()
    return render(request,"news/sendemail.html", {'f':e})

def printEmail(request):
    #Khi nhấn submit thì nhận dữ liệu về
    if request.method == "POST":
        #Bắt dữ liệu gửi lên bởi form 'EmailForm'
        e =EmailForm(request.POST)
        if e.is_valid():
            #Không có model nên dùng cleaned_data???
            tieude = e.cleaned_data['title']
            email = e.cleaned_data['email']
            noidung = e.cleaned_data['content']
            c = e.cleaned_data['cc']
            context = {'td':tieude, 'em':email,'nd': noidung, 'c':c}
            #Cách 2:
            context2 = {'data_email': e}
            return render(request, 'news/printEmail.html', context2)