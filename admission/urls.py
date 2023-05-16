from django.urls import path
from . import views

urlpatterns = [
    path('personal-information/', views.personal_information_view, name='personal_information_form'),
    path('educational-background/', views.educational_background_view, name='educational_background_form'),
    path('parent-guardian/', views.parent_guardian_view, name='parent_guardian_form'),
    path('parent-guardian2/', views.parent_guardian_view2, name='parent_guardian_form2'),
    path('emergency-contact/', views.emergency_contact_view, name='emergency_contact_form'),
    path('admission-form/', views.admission_form_view, name='admission_form'),
    path('success/', views.success_page, name='success_page'),
]