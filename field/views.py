from django.shortcuts import render, redirect
from .forms import PersonalInfoForm, CareerApplicationInfoForm,ExperienceInformationOneForm,\
      ExperienceInformationTwoForm, ExperienceInformationThreeForm,TrainingInformationForm,ContactInformationForm,\
        Reference1Form,Reference2Form


def HomePage(request):
    return render(request, 'base.html')

def personal_info_form(request):
    if request.method == 'POST':
        form = PersonalInfoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Redirect to a success page or do something else
            return redirect('/success/')
    else:
        form = PersonalInfoForm()

    return render(request, 'field/personal_info_form.html', {'form': form})

def career_application_info_form(request):
    if request.method == 'POST':
        form = CareerApplicationInfoForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page or do something else
            return redirect('/success/')
    else:
        form = CareerApplicationInfoForm()

    return render(request, 'field/career_application_info_form.html', {'form': form})
 

def experience_info_one_form(request):
    if request.method == 'POST':
        form = ExperienceInformationOneForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page or do something else
            return redirect('/success/')
    else:
        form = ExperienceInformationOneForm()

    return render(request, 'field/experience_info_one_form.html', {'form': form})


def experience_info_two_form(request):
    if request.method == 'POST':
        form = ExperienceInformationTwoForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page or do something else
            return redirect('/success/')
    else:
        form = ExperienceInformationTwoForm()

    return render(request, 'field/experience_info_two_form.html', {'form': form})


def experience_info_three_form(request):
    if request.method == 'POST':
        form = ExperienceInformationThreeForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page or do something else
            return redirect('/success/')
    else:
        form = ExperienceInformationThreeForm()

    return render(request, 'field/experience_info_three_form.html', {'form': form})


def training_info_form(request):
    if request.method == 'POST':
        form = TrainingInformationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page or do something else
            return redirect('/success/')
    else:
        form = TrainingInformationForm()

    return render(request, 'field/training_info_form.html', {'form': form})


def contact_info_form(request):
    if request.method == 'POST':
        form = ContactInformationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page or do something else
            return redirect('/success/')
    else:
        form = ContactInformationForm()

    return render(request, 'field/contact_info_form.html', {'form': form})



def reference1_form(request):
    if request.method == 'POST':
        form = Reference1Form(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page or do something else
            return redirect('/success/')
    else:
        form = Reference1Form()

    return render(request, 'field/reference1_form.html', {'form': form})


def reference2_form(request):
    if request.method == 'POST':
        form = Reference2Form(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page or do something else
            return redirect('/success/')
    else:
        form = Reference2Form()

    return render(request, 'field/reference2_form.html', {'form': form})


def success_page(request):
    return render(request, 'field/success.html')