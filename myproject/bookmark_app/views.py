from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import inputform
from django.urls import reverse




class CustomLoginView(LoginView):
	template_name = 'login.html';
	redirect_authenticated_user = True

class CustomLogoutView(LogoutView):
    template_name = 'login.html'
    next_page = 'login'

def home(request):
    return HttpResponse('Hello User')


      
@login_required(redirect_field_name='',login_url='/')
def berhasil(request):
    mypost = Post.objects.all()
    form=inputform()
    template=loader.get_template('berhasil.html')
    context ={
        'mypost':mypost,'form':form
    }
    return HttpResponse(template.render(context,request))
    
def addrecord(request):
  x = request.POST['content']
  y = request.POST['name']
  member = Post(content=x,name=y)
  member.save()
  return HttpResponseRedirect(reverse('berhasil'))

def delete(request, id):
  member = Post.objects.get(id=id)
  member.delete()
  return HttpResponseRedirect(reverse('berhasil'))

