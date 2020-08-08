from django.shortcuts import render, HttpResponse
from django.views import View
#Hàm xác thực nội dung
from django.contrib.auth import authenticate, login, decorators
#Hàm kết nối các đối tượng lại với nhau
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostForm


# Create your views here.
class indexClass(View):
    def get(self,request):
        return HttpResponse('<h1>Hello World</h1>')


class loginClass(View):
    def get(self,request):
        return render(request, 'login/login.html')

    def post(self,request):
        user_name = request.POST.get('tendangnhap')
        password = request.POST.get('matkhau')
        my_user = authenticate(username=user_name, password=password)
        if my_user is None:
            return HttpResponse('Tên đăng nhập %s không tồn tại hoặc mật khẩu không đúng' %(user_name))
        
        login(request,my_user)
        return render(request, 'login/success.html')

#Phải đặt LoginRequiredMixin trước => View
class viewUserClass(LoginRequiredMixin,View):
    login_url='/login/'
    def get(self,request):
        #if not request.user.is_authenticated:
        return HttpResponse('<h1>Đây là view của user</h1>')

#yêu cầu đăng nhập để vào. nếu chưa đăng nhập thì đưa đến trang login_url
@decorators.login_required(login_url='/login/')
def xem_sp(request):
    return HttpResponse('Nếu bạn thấy tôi nghĩa là bạn đã đăng nhập vào roài đó')

class addPost(LoginRequiredMixin,View):
    login_url = '/login/'
    def get(self,request):
        f = PostForm()
        context = {'pf':f}
        return render(request,'login/addpost.html',context)

    def post(self,request):
        f = PostForm(request.POST)
        if f.is_valid():
            if request.user.has_perm('login.add_post'):
                f.save()
                return HttpResponse('Lưu OK')
            else:
                return HttpResponse('Bạn không có quyền')
        else:
            return HttpResponse('Không đúng kiểu')
