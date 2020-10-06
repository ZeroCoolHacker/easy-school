# Create your views here.
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView as DefaultLoginView
from django.views.generic import CreateView
from forms.forms import TeacherSignUpForm
from .models import Teacher
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.views import View



def Login(request):
    
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        print(username)
        user=auth.authenticate(username=username,password1=password)
        if user is not None:
            auth.login(request,user)
            print('hello')
            return redirect('home')
                
        else:
            messages.error(request,'username or password not correct')
            print('hey')
            return redirect('login')

            
    else:
        print('hii')
        return render(request,'login.html') 


    

class TeacherSignUpFormView(CreateView):
    model = Teacher
    form_class = TeacherSignUpForm
    template_name = 'signup.html'
    success_url = "/"

    def form_valid(self, form):
        c = {'form': form, }
        user = form.save(commit=False)
        # Cleaned(normalized) data
        phone_no = form.cleaned_data['phone_no']
        date_of_birth = form.cleaned_data['date_of_birth']
        password1 = form.cleaned_data['password1']
        password2 = form.cleaned_data['password2']
        if password1 != password2:
            messages.error(self.request, "Passwords do not Match", extra_tags='alert alert-danger')
            return render(self.request, self.template_name, c)
        user.set_password(password1)
        user.save()
        date_of_joining= form.cleaned_data['date_of_joining']
        cnic = form.cleaned_data['cnic']
        is_teaching= form.cleaned_data['is_teaching']
        profile_image=form.cleaned_data['profile_image']
        address = form.cleaned_data['address']
        gender = form.cleaned_data['gender']
 
        # Create UserProfile model
        Teacher.objects.create(user=user, phone_no=phone_no, date_of_birth=date_of_birth,date_of_joining=date_of_joining,cnic=cnic,
                                    is_teaching=is_teaching,profile_image=profile_image,address=address,gender=gender,)

        return super(TeacherSignUpFormView, self).form_valid(form)
 
