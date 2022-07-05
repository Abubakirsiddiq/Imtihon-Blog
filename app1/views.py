from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.views import View
from .models import Todo


class LoginView(View):
    def get(self,request):
        return render(request, "registir.html")

    def post(self, request, ):
        u=request.POST.get("l")
        p=request.POST.get("p")
        users=authenticate(username=u,password=p,)
        if users is None:
            return redirect("login")
        else:
            login(request,users)
            return redirect("blog.html")


class BlogView(View):
    def get(self, request):
        return redirect(request, "blog.html")

    def post(self, request):
        hammasi = Todo.objects.all()




class Maqola(View):
    def get(self, request):
        return redirect(request, "maqola.html")

    def post(self, request, pk):
        bir = Todo.objects.filter(id=pk)




class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("login.html")

