from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.utils import timezone
# from .models import 
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from blogger.models import Plan,Post,Comment


# Create your views here.
def tripdiaries(request):
	return render(request, 'firstpage.html')

def signup(request):
	if request.method=="POST":
		username = request.POST.get('username',None)
		password = request.POST.get('password',None)
		email=request.POST.get("email")
		try:
			user = User.objects.get(username=username)
			print(user)
		except:
			user=None
		
		if user is not None:
			return render(request,'signup.html',{'show':'username.already.taken'})

		else:
			user=User.objects.create_user(username=username,email=email,password=password)	
			user.save()
			return redirect("/home/")
	return render(request, "signup.html")

def signin(request):
	if request.method=="POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		print(user)
		if user is not None:
			login(request, user)
			return redirect("/home/")
	return render(request,"signin.html")    	

def signout(request):
	logout(request)
	return redirect("/login/")	

def home(request):
	posts = Post.objects.all()
	return render(request, 'post_list.html', {'posts': posts})   	

def new_post(request):
	if request.method == "POST":
		title = request.POST.get('title')
		content = request.POST.get('content')
		Post.objects.create(title=title,content=content)
		return redirect('base.html', pk=post.pk)
	
	return render(request, 'new_post.html')

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'post_detail.html', {'post': post}) 

def plan_detail(request, pk):
	plan = get_object_or_404(Plan, pk=pk)
	return render(request, 'plan_detail.html', {'plan': plan}) 	

def plan(request):
	if request.method == "POST":
		place= request.POST.get('place')
		start_date= request.POST.get('start_date')
		end_date= request.POST.get('end_date')
		schedule = request.POST.get('schedule')
		to_do_list= request.POST.get('to_do_list')
		Plan.objects.create(start_date=start_date,end_date=end_date,place=place,schedule=schedule,to_do_list=to_do_list)
		return redirect("/plan_list/")
	return render(request, 'plan.html')

def post_list(request):
	post = Post.objects.all()
	return render(request, 'post_list.html', {'post': post}) 

def plan_list(request):
	plan = Plan.objects.all()
	return render(request, 'plan_list.html', {'plan': plan}) 	


def add_comment_to_post(request, pk):
	if request.method == "POST":
		post = get_object_or_404(Post, pk=pk)
		text= request.POST.get('text')
		Comment.objects.create(text=text)	
		return redirect('/post_detail/', pk=post.pk)
	return render(request, 'post_details.html')  	  	

# def post_remove(request, pk):
# 	post = get_object_or_404(Post, pk=pk)
# 	post.delete()
# 	return redirect('post_list.html')     