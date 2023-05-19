from django.shortcuts import render, redirect
from .forms import PersonalInformationForm, EducationalBackgroundForm, ParentGuardianForm, EmergencyContactForm, AdmissionFormForm
from .models import PersonalInformation, EducationalBackground, EmergencyContact



def personal_information_view(request):
    if request.method == 'POST':
        form = PersonalInformationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('educational_background_form')
    else:
        form = PersonalInformationForm()
    
    return render(request, 'admission/personal_information_form.html', {'form': form})





def educational_background_view(request):
    if request.method == 'POST':
        form = EducationalBackgroundForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('parent_guardian_form')
    else:
        form = EducationalBackgroundForm()
    
    return render(request, 'admission/educational_background_form.html', {'form': form})


def parent_guardian_view(request):
    if request.method == 'POST':
        form = ParentGuardianForm(request.POST, prefix='guardian1')
        person_data = PersonalInformation.objects.order_by('-id').first()
        if form.is_valid():
            personal_info = form.save(commit=False)
            personal_info.personal_information = person_data
            personal_info.save()
            return redirect('parent_guardian_form2')
    else:
        form = ParentGuardianForm(prefix='guardian1')
    
    return render(request, 'admission/parent_guardian_form.html', {'form': form})


def parent_guardian_view2(request):
    if request.method == 'POST':
        form = ParentGuardianForm(request.POST, prefix='guardian2')
        person_data = PersonalInformation.objects.order_by('-id').first()
        if form.is_valid():
            personal_info = form.save(commit=False)
            personal_info.personal_information = person_data
            personal_info.save()
            return redirect('emergency_contact_form')
    else:
        form = ParentGuardianForm(prefix='guardian2')
    
    return render(request, 'admission/parent_guardian_form.html', {'form': form})


def emergency_contact_view(request):
    if request.method == 'POST':
        form = EmergencyContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admission_form')
    else:
        form = EmergencyContactForm()
    
    return render(request, 'admission/emergency_contact_form.html', {'form': form})


def admission_form_view(request):
    if request.method == 'POST':
        form = AdmissionFormForm(request.POST)
        person_data = PersonalInformation.objects.order_by('-id').first()
        contact = EmergencyContact.objects.order_by('-id').first()
        education = EducationalBackground.objects.order_by('-id').first()
        if form.is_valid():
            personal_info = form.save(commit=False)
            personal_info.personal_information = person_data
            personal_info.emergency_contact = contact
            personal_info.educational_background = education
            personal_info.save()
            return redirect('success_page')
    else:
        form = AdmissionFormForm()
    
    return render(request, 'admission/admission_form.html', {'form': form})


def success_page(request):
    return render(request, 'admission/success_page.html')
