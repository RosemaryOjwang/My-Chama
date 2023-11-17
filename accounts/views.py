from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required
from App_bankingSolution.forms import Group_Form 
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
        files = request.FILES.getlist('images')
        group_form = Group_Form(request.POST, request.FILES)

        if group_form.is_valid():
            groupName = request.POST.get('groupName')
            slug = slugify(groupName)

            group = group_form.save(commit=False)
            group.user = request.user
            group.slug = slug
            group.save()

            #for file in files:
                #MultipleImage.objects.create(house=house, images=file)

            messages.success(request, 'Your group was created successfuly!')

            #return redirect('payments:process')

            return redirect('user_admin')
    else:
        group_form = Group_Form()
        #images_form = MultipleImagesForm()



    context = {"h_form": house_form, "i_form": images_form, "title": "Add House"}
    return render(request, 'Agency/add_house.html', context )


@login_required
def add_member(request):
    house_form = House_DetailsForm()
    images_form = MultipleImagesForm()
    if request.method == "POST":
        files = request.FILES.getlist('images')
        house_form = House_DetailsForm(request.POST, request.FILES)

        if house_form.is_valid():
            title = request.POST.get('title')
            slug = slugify(title)

            house = house_form.save(commit=False)
            house.user = request.user
            house.slug = slug
            house.save()

            for file in files:
                MultipleImage.objects.create(house=house, images=file)

            messages.success(request, 'The house was added successfuly!')

            #return redirect('payments:process')

            return redirect('user_admin')
    else:
        house_form = House_DetailsForm()
        images_form = MultipleImagesForm()



    context = {"h_form": house_form, "i_form": images_form, "title": "Add House"}
    return render(request, 'Agency/add_house.html', context )


    