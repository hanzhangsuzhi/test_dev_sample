from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import auth


# Create your views here.
# 主要代码逻辑

# 登录界面
def index(request):
    return render(request, "index.html")

# 处理登录请求
def login_action(request):
    if request.method == 'POST':
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")

        # 用户名或密码为空
        if username == "" or password =="":
            return render(request, "index.html", {"error": "用户名或密码为空"})

        else:
            user = auth.authenticate(username=username, password=password)
            print(user)
            print(type(user))
            # 登录成功
            if user is not None:
                auth.login(request, user)
                return render(request, "project_manage.html")
            # 用户名或密码错误
            else:
                return render(request, "index.html", {"error": "用户名或密码错误"})
