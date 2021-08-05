from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .forms import LoginForm,PlotForm,Change_Password,UserRegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from .models import Question,Choice,Answer,Post,Comment
from django.contrib.auth.models import User
# Create your views here.

def index(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            pf = PlotForm(request.POST)
            if pf.is_valid():
                instance = pf.save(commit=False)
                instance.user = request.user
                instance.save()
                messages.success(request, 'post created success')
                return HttpResponseRedirect('/')
        else:
            pf = PlotForm()    
        return render(request, 'index.html', {'PlotForm':pf})
    else:
        return HttpResponseRedirect('login')


def signin(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    else:
        if request.method == "POST":
            fm = LoginForm(request=request, data=request.POST)
            if fm.is_valid():
                username = fm.cleaned_data['username']
                password = fm.cleaned_data['password']

                if password != password:
                    messages.info(request, 'password not match')
                    

                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    messages.error(request, 'This user is not admin')
                    print(messages)
        else:
            fm = LoginForm()
        return render(request, 'login.html', {'form':fm})

def register(request):
    return render(request, 'register.html')


def logout_view(request):
    if request.user.is_staff:
        logout(request)
        return HttpResponseRedirect('admin-login')
    else:
        return HttpResponseRedirect('login')


def main(request):
    qs = Question.objects.all()
    return render(request, 'main.html', {'question':qs})


def question_detail_view(request, id=None):

    qs = get_object_or_404(Question, id=id)
    
    context= {'question': qs,
              }
    
    return render(request, 'detail.html', context)


def single_question(request, id=None):
    if request.method == "GET":
        qs = Question.objects.get(id=id)
        return render(request, 'single_question.html',{'question':qs})
    elif request.method == "POST":
        user_id = request.user.id
        data = request.POST
        ans = Answer.objects.create(user_id=user_id, choice_id=data['choice'])
        if ans:
            return HttpResponse('Vote Done')
        else:
            return HttpResponse('Vote fail')


def user_post(request):
    up = Post.objects.all()
    return render(request, 'post.html', {'UserPost':up})



def change_password(request):

    if request.method == 'POST':
        form = Change_Password(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = Change_Password(request.user)
    return render(request, 'change_password.html', {
        'form': form
    })

def adminRegister(request):
    if request.user.is_staff:
        if request.method == "POST":
            sf = UserRegisterForm(data=request.POST)
            if sf.is_valid():
                username = sf.cleaned_data['username']
                email = sf.cleaned_data['email']
                password1 = sf.cleaned_data['password1']
                password2 = sf.cleaned_data['password2']

                if password1 == password2:
                    user = User.objects.create_user(username=username, email=email, password=password1)
                    user.is_staff=True 
                    user.save()
                    messages.info(request, "Admin account created Successfully")
                    return HttpResponseRedirect('admin-register')
                else:
                    messages.info(request, "Password not match")
        else:
            sf = UserRegisterForm()
        return render(request, 'adminRegister.html', {"staff_form":sf})
    else:
        return HttpResponseRedirect('/main')

def adminSignIn(request):
    if request.method == "POST":
        fm = LoginForm(request=request, data=request.POST)
        if fm.is_valid():
            username = fm.cleaned_data['username']
            password = fm.cleaned_data['password']
                

            user = authenticate(username=username, password=password)
            if user.is_staff:
                login(request, user)
                return HttpResponseRedirect('admin-register')
            else:
                messages.error(request, 'This user is not admin')
                print(messages)
    else:
        fm = LoginForm()
    return render(request, 'admin_login.html', {'form':fm})



