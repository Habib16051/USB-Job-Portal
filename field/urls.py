from django.urls import path
from .views import personal_info_form, career_application_info_form,experience_info_one_form, \
    experience_info_two_form, experience_info_three_form,training_info_form,contact_info_form,reference1_form, reference2_form

urlpatterns = [
    path('personal_info_form/', personal_info_form, name='personal_info_form'),
    path('career_application_info_form/', career_application_info_form, name='career_application_info_form'),
    path('experience_info_one_form/', experience_info_one_form, name='experience_info_one_form'),
    path('experience_info_two_form/', experience_info_two_form, name='experience_info_two_form'),
    path('experience_info_three_form/', experience_info_three_form, name='experience_info_three_form'),
    path('training_info_form/', training_info_form, name='training_info_form'),
    path('contact_info_form/', contact_info_form, name='contact_info_form'),
    path('reference1_form/', reference1_form, name='reference1_form'),
    path('reference2_form/', reference2_form, name='reference2_form'),

    # Add other URL patterns as needed
]
