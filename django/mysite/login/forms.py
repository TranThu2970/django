from django.forms import ModelForm
from .models import PostLogin

class PostForm(ModelForm):
    class Meta:
        model = PostLogin
        fields = ('title','content')