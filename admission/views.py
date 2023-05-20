from django.shortcuts import render, redirect
from .forms import PersonalInformationForm, EducationalBackgroundForm, ParentGuardianForm, EmergencyContactForm, AdmissionFormForm
from .models import StudentPersonalInformation
from students.models import Student


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
        person_data = StudentPersonalInformation.objects.order_by('-id').first()
        if form.is_valid():
            personal_info = form.save(commit=False)
            personal_info.personal_information = person_data
            personal_info.save()
            return redirect('parent_guardian_form')
    else:
        form = EducationalBackgroundForm()
    
    return render(request, 'admission/educational_background_form.html', {'form': form})


def parent_guardian_view(request):
    if request.method == 'POST':
        form = ParentGuardianForm(request.POST, prefix='guardian1')
        person_data = StudentPersonalInformation.objects.order_by('-id').first()
        if form.is_valid():
            personal_info = form.save(commit=False)
            personal_info.personal_information = person_data
            personal_info.save()
            return redirect('emergency_contact_form')
    else:
        form = ParentGuardianForm(prefix='guardian1')
    
    return render(request, 'admission/parent_guardian_form.html', {'form': form})





def emergency_contact_view(request):
    if request.method == 'POST':
        form = EmergencyContactForm(request.POST)
        person_data = StudentPersonalInformation.objects.order_by('-id').first()
        if form.is_valid():
            personal_info = form.save(commit=False)
            personal_info.personal_information = person_data
            personal_info.save()
            return redirect('admission_form')
    else:
        form = EmergencyContactForm()
    
    return render(request, 'admission/emergency_contact_form.html', {'form': form})


def admission_form_view(request):
    if request.method == 'POST':
        form = AdmissionFormForm(request.POST)
        person_data = StudentPersonalInformation.objects.order_by('-id').first()
        if form.is_valid():
            personal_info = form.save(commit=False)
            personal_info.personal_information = person_data
            personal_info.save()
            return redirect('success_page')
    else:
        form = AdmissionFormForm()
    
    return render(request, 'admission/admission_form.html', {'form': form})


def success_page(request):
    return render(request, 'admission/success_page.html')



def studentsdetail(request):
    detail = StudentPersonalInformation.objects.all()


    return render(request ,"admission/studentsdetail.html",{
        "details":detail,
    })




def shift_data_view(request, pk):
    if request.method == 'POST':
        personal_info_queryset = StudentPersonalInformation.objects.filter(pk=pk)
        if personal_info_queryset.exists():
            personal_info = personal_info_queryset.first()
            student = Student(
                admission_no=personal_info.admission_no,
                date_of_admission=personal_info.date_of_admissionapplication,
                first_name=personal_info.first_name,
                last_name=personal_info.last_name,
                gender=personal_info.gender,
                date_of_birth=personal_info.date_of_birth,
                address=personal_info.address,
                current_class=personal_info.admission_form.course,
                profile_image=personal_info.profile_image,
                is_studying = True,
            )
            student.save()

            return redirect('success_page')

    return render(request, 'admission/studentsdetail.html',{
        'student':student,
    })