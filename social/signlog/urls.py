from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from signlog import views

app_name='signlog'

urlpatterns = [
    
   url(r'^signup1/$',views.Signn.as_view(),name='signup'),
   url(r'^register/$',views.register,name='register'),
   url(r'^success1/$',views.Success.as_view(),name='success'),
   url(r'^login/$',views.loginuser,name='login'),
   url(r'^ghome/$',views.ghome.as_view(),name='ghome'),
   url(r'^logout/$',views.logoutuser,name='logout'),
   url(r'^log/$',views.Log.as_view(),name='Log'),
   url(r'^groups/$',views.GroupsCreateView.as_view(),name='groups'),
   url(r'^email1/$',views.index,name='mail'),
   url(r'^groups1/$',views.GroupsListView.as_view(),name='grp1'),
   url(r'^groups2/$',views.UGListView.as_view(),name='grp2'),
   url(r'^cpost/$',views.PostCreateView.as_view(),name='createpost'),
   url(r'^(?P<pk>\d+)/$',views.GroupsDetailView.as_view(),name='detail'),
   url(r'^post/(?P<pk>\d+)/$',views.PostDetailView.as_view(),name='pdetail'),
   url(r'^deletejoin/(?P<pk>\d+)/$',views.deletejoin,name='deletejoin'),
   url(r'^deletepost/(?P<pk>\d+)/$',views.PostDeleteView.as_view(),name='delpost'),
   url(r'^postcount/(?P<pk>\d+)/$',views.PostCount,name='postcount'),
   url(r'^postcount1/(?P<pk>\d+)/$',views.PostCount1,name='postcount1'),
   url(r'^t/(?P<pk>\d+)/$',views.updatejoin,name='updatejoin'),
   url(r'^postlist/(?P<pk>\d+)/$',views.PostListView,name='postlist'),
   url(r'^grouppost/$',views.GroupPost.as_view(),name='grouppost'),
   url(r'^groupdetail/(?P<pk>\d+)/$',views.PostInParticularGroup.as_view(),name='groupdetail'),
#    url(r'^logt/$',views.firstfunc,name='firstfunc'),
    # url(r'^otherperson/(?P<pk>\d+)/$',views.otherpersonpost,name='otherperson'),


    # url(r'^update/(?P<pk>\d+)/$',views.GroupsUpdateView.as_view(),name='update'),
    # path('login1/',views.LoginDetailView.as_view(),name='verify'),
    
    
    
    
    
]