from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required
from App_bankingSolution.forms import Group_Form, Add_MembersForm
from django.utils.text import slugify
from django.contrib import messages


# Create your views here.
class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

@login_required
def register_group(request):
    group_form = Group_Form()
    
    if request.method == "POST":
        group_form = Group_Form(request.POST, request.FILES)

        if group_form.is_valid():
            groupName = request.POST.get('groupName')
            slug = slugify(groupName)

            group = group_form.save(commit=False)
            group.user = request.user
            group.slug = slug
            group.save()

            messages.success(request, 'Your group was created successfuly!')

            return redirect('add_member')
    else:
        group_form = Group_Form()



    context = {"g_form": group_form, "title": "Create Group"}
    return render(request, 'register_group.html', context )


@login_required
def add_member(request):
    membership_form = Add_MembersForm()
    
    if request.method == "POST":
        
        membership_form = Add_MembersForm(request.POST, request.FILES)

        if membership_form.is_valid():
            memberName = request.POST.get('memberName')
            slug = slugify(memberName)

            member = membership_form.save(commit=False)
            member.user = request.user
            member.slug = slug
            member.save()

            
            messages.success(request, 'The member was added successfuly!')

            return redirect('user_admin')
    else:
        membership_form = Add_MembersForm()



    context = {"m_form": membership_form, "title": "Add Member"}
    return render(request, 'add_member.html', context )

@login_required
def user_admin(request):
    members = request.user.group_user.exclude(available=False)
    context = {"title": "User Admin Site"}
    return render(request, 'user_admin.html', context)



    