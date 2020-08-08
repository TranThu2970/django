from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','content',)
        widgets = {
            'title' : forms.TextInput(attrs={'class':'tieude123'}),
            'content' : forms.Textarea(attrs={'class':'noidung1234'})
        }

#form không liên quan tới model nên ko cập nhật vào CSDL
class EmailForm(forms.Form):
    #widgets: value, class, id,..
    title = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'tieude123'}))
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea)
    cc = forms.BooleanField(required=False)
