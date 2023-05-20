from django.urls import path
from . import views

urlpatterns = [
    path('personal-information/', views.personal_information_view, name='personal_information_form'),
    path('educational-background/', views.educational_background_view, name='educational_background_form'),
    path('parent-guardian/', views.parent_guardian_view, name='parent_guardian_form'),
    path('emergency-contact/', views.emergency_contact_view, name='emergency_contact_form'),
    path('admission-form/', views.admission_form_view, name='admission_form'),
    path('success/', views.success_page, name='success_page'),
    path("studentsdetail/", views.studentsdetail, name="studentsdetail"),
    path("shift_data_view/<int:pk>",views.shift_data_view, name='shift_data_view')

]