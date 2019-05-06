from django.conf.urls import url
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView


from . import views
app_name = 'users'

urlpatterns = [
    # 登录页面
    url(r'^login/$', LoginView.as_view(template_name='users/login.html'), name='login'),
    # 注销
    url(r'^logout/$', LogoutView.as_view(), name='logout'),

    # 注册页面
    url(r'^register/$', views.register, name='register'),

]
