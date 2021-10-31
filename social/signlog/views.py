from typing import List
from django.db.models import fields
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls.base import reverse_lazy
from django.views.generic.edit import UpdateView
from signlog import models
from django.contrib.auth.models import User, auth
from django.contrib import auth
from django.views.generic import CreateView, TemplateView, DetailView, ListView, DeleteView
from django.core.mail import send_mail
from signlog.models import Groups
from . import forms
# LOGIN REQUIRED
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, logout, authenticate


def index(request):

    send_mail(
        'Subject here',
        'Here is the message.',
        'abca63459@gmail.com.com',
        ['anand2710dubey@gmail.com'],
        fail_silently=False,)
    return HttpResponse("Mail Sent")


class Signn(TemplateView):
    template_name = 'registerr.html'


class Index(TemplateView):
    template_name = 'base1.html'


class Gpbase(LoginRequiredMixin, TemplateView):
    login_url = '/signlog/log/'
    redirect_field_name = 'Log'
    template_name = 'gpbase.html'


class Success(TemplateView):
    template_name = 'success.html'


class Log(TemplateView):
    template_name = 'login.html'


class ghome(LoginRequiredMixin, TemplateView):
    login_url = '/signlog/log/'
    redirect_field_name = 'login'
    template_name = 'group/gphome.html'


def register(request):
    if request.method == 'POST':
        try:
            user = User.objects.get(username=request.POST['Name'])
            return render(request, "registerr.html", {'error': 'Username Already Exists!'})
        except User.DoesNotExist:
            user = User.objects.create_user(
                username=request.POST['Name'], password=request.POST['Password'], email=request.POST['Email'])
            return render(request, 'login.html')


def loginuser(request):
    if request.method == 'POST':
        uname = request.POST['Name']
        pwd = request.POST['Password']
        user = auth.authenticate(username=uname, password=pwd)
        if user is not None:
            auth.login(request, user)
            return render(request, 'group/gphome.html')
        else:
            return render(request, 'login.html', {'error': 'Invalid Login credencials'})
    else:
        return render(request, 'login.html')


@login_required
def logoutuser(request):
    logout(request)
    return redirect('index')


@login_required
def updatejoin(request, pk):
    grpobj = get_object_or_404(models.Groups, pk=pk)
    grpobj.cjoin = grpobj.cjoin+1
    grpobj.usrname+=request.user.username
    grpobj.tf = True
    grpobj.save()
    return redirect('signlog:detail', pk=grpobj.pk)


@login_required
def deletejoin(request, pk):
    grpobj = get_object_or_404(models.Groups, pk=pk)
    grpobj.cjoin = grpobj.cjoin-1
    grpobj.usrrname+=request.user.username
    grpobj.tf = False
    grpobj.save()
    return redirect('signlog:detail', pk=grpobj.pk)


@login_required
def Login(request):
    return HttpResponse("Hi")


class GroupsCreateView(LoginRequiredMixin, CreateView):
    # context_object_name='Ngroups'
    login_url = '/signlog/log/'
    redirect_field_name = 'login'
    fields = ('name', 'desc')
    model = models.Groups


class GroupsListView(ListView):

    context_object_name = 'Ngroups'
    model = models.Groups


class GroupsDetailView(LoginRequiredMixin, DetailView):
    login_url = '/signlog/log/'
    redirect_field_name = 'login'
    context_object_name = 'groups_detail'
    fields = ('name', 'desc', 'cjoin', 'cpost')
    model = models.Groups


class UGListView(LoginRequiredMixin, ListView):
    login_url = '/signlog/log/'
    redirect_field_name = 'Log'
    context_object_name = 'ug_list'
    model = models.Groups
    template_name = 'signlog/usergroup_list.html'


class PostCreateView(LoginRequiredMixin, CreateView):
    login_url = '/signlog/log/'
    redirect_field_name = 'login'
    form_class = forms.postcreateform
    model = models.Post
    template_name = 'signlog/createpost.html'


class PostDetailView(LoginRequiredMixin, DetailView):
    login_url = '/signlog/log/'
    redirect_field_name = 'login'
    context_object_name = 'post_detail'
    model = models.Groups
    template_name = 'signlog/post_detail.html'

# class PostListView(ListView):
#     context_object_name='post_list'
#     model=models.Post
#     template_name='signlog/post_list.html'


class PostDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/signlog/log/'
    redirect_field_name = 'login'
    context_object_name = 'delete_post'
    model = models.Post
    template_name = 'signlog/deletepost.html'
    
    def get_success_url(self):
        return reverse_lazy('signlog:postcount1',kwargs={'pk': self.object.Group.pk})


@login_required
def PostCount(request, pk):
    postobj = get_object_or_404(models.Post, pk=pk)
    postobj.created_by = request.user.username
    postobj.Group.cpostsave()
    postobj.save()
    return redirect('signlog:pdetail', pk=postobj.Group.pk)


@login_required
def PostCount1(request, pk):
    grp=get_object_or_404(models.Groups,pk=pk)
    grp.cpostsave1()
    return redirect('signlog:grouppost')


class GroupPost(LoginRequiredMixin, ListView):
    login_url = '/signlog/log/'
    redirect_field_name = 'login'
    context_object_name = 'grouppost'
    model = models.Groups
    template_name = 'signlog/grouppost.html'


class PostInParticularGroup(LoginRequiredMixin, DetailView):
    login_url = '/signlog/log/'
    redirect_field_name = 'login'
    context_object_name = 'group_detail'
    model = models.Groups
    template_name = 'signlog/postingroup.html'


@login_required
def PostListView(request, pk):
    pobj = get_object_or_404(models.Post, pk=pk)
    uname = pobj.created_by
    pp = models.Post.objects.filter(created_by=uname)

    return render(request, 'signlog/post_list.html', context={'obj': pp, 'name': uname})




# class LoginDetailView(DetailView):
#     model=models.SignUp
#     def Login(request):
#      if request.method=='POST':
#         Name=request.Post.get('Name')
#         Password=request.Post.get('Password')
#         {% for student in signup_detail %}
#         {% endfor %}

# class Sign(CreateView):
#     fields=('name','email','password')
#     model=models.SignUp


#  if request.method=='POST':
#         name=request.POST.get('Name')
#         password=request.POST['Password']
#         email=request.POST['Email']
#         obj=User(username=name,password=password,email=email)
#         obj.save()
#         return HttpResponse('Done')

# def updatefunc(request):
#         if request.method=='POST':
#             c=Groups.objects.all().filter(id=pk)
