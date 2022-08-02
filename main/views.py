from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import *
# Create your views here.
class Home(TemplateView):
    template_name = 'index.html'
class About(View):
    template_name = 'about.html'
    def get(self,request):
        about_data = AboutUs.objects.all()
        context = {
            'about' : about_data,
        }
        return render(request,self.template_name,context)
class Cakes(TemplateView):
    template_name = 'cakes.html'
class Message(View):
    template_name = 'contact.html'
    def get(self,request):
        return render(request,self.template_name)
    def post(self,request):
        if request.method == 'POST':
            name = request.POST.get('name','')
            email = request.POST.get('email', '')
            subject = request.POST.get('subject', '')
            message = request.POST.get('message', '')
            form = Contact(name=name,email=email,subject=subject,message=message)
            form.save()
            return redirect('contact')
class BlogView(View):
    template_name = 'blog.html'
    def get(self,request,):
        blog = Blog.objects.all()
        category = Category.objects.all()
        print(blog)
        context = {
            'blog': blog,
            'category': category,
        }
        return render(request,self.template_name,context)

class BlogDetailView(View):
    template_name = 'blog_details.html'
    def get(self,request, id):
        blog = Blog.objects.filter(id=id)
        comments = Comment.objects.filter(blog__id=id)
        count = len(comments)
        no = [count]
        context = {
            'blog': blog,
            'comment': comments,
            'no': no,
        }
        return render(request,self.template_name, context)


    def post(self,request,id):
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        contact = request.POST.get('contact', '')
        comment = request.POST.get('comment', '')
        post = Blog.objects.get(id=request.POST.get('blog_id'))
        comment = Comment(name=name, email=email, contact=contact, comment=comment, blog=post)
        comment.save()
        return redirect('home')
        messages.success(request, 'Comment post Successfully!')

class CustomCake(View):
    template_name = 'customcake.html'
    def get(self,request):
        return render(request,self.template_name)


class Registration(TemplateView):
    template_name = 'signin.html'
    def post(self, request):
        if request.method=="POST":
        # Get the post parameters
            user=request.POST['name']
            email=request.POST['email']
            pass1=request.POST['pswd1']
            pass2=request.POST['pswd2']

            # check for errorneous input
            # check for errorneous input
            if len(user)<5:
                messages.error(request, " Your user name must be under 10 characters")
                return redirect('registration')
            if User.objects.filter(username=user):
                messages.error(request, " user already exist")
                return redirect('registration')
            if not user.isalnum():
                messages.error(request, " User name should only contain letters and numbers")
                return redirect('registration')
            if (pass1!= pass2):
                messages.error(request, " Passwords do not match")
                return redirect('registration')
            # Create the user
            myuser = User.objects.create_user(username=user,email=email,password=pass1)
            myuser.save()
            messages.success(request, " Your BKRE account has been successfully created")
        return redirect("registration")

class Login(TemplateView):
    template_name = 'login.html'
    def post(self,request):
        if request.method=="POST":
                # Get the post parameters
            loginusername=request.POST['username']
            loginpassword=request.POST['password']
            loginemail=request.POST['email']
            user=authenticate(username= loginusername, password= loginpassword)
            if user is not None:
                login(request,user)
                messages.success(request, "Successfully Logged In")
                return redirect('home')
            else:
                messages.error(request, "Invalid credentials! Please try again")
                return redirect("login")

class forgetpassword(TemplateView):
    template_name = 'Frget-pswd.html'

def logoutt(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('home')