from django import forms
from .models import PersonalInfo, CareerApplicationInfo,ExperienceInformationOne, ExperienceInformationTwo,\
    ExperienceInformationThree,TrainingInformation,ContactInformation,Reference1, Reference2

class PersonalInfoForm(forms.ModelForm):
    class Meta:
        model = PersonalInfo
        fields = ['full_name', 'father_name', 'Mother_Name', 'gender', 'marital_status', 'nationality', 'passport', 'nid', 'date_of_birth', 'cv']

class CareerApplicationInfoForm(forms.ModelForm):
    class Meta:
        model = CareerApplicationInfo
        fields = ['looking_for', 'present_salary', 'expected_salary', 'preferred_job_categor', 'preferred_district', 'preferred_ogranization_type']



class ExperienceInformationOneForm(forms.ModelForm):
    class Meta:
        model = ExperienceInformationOne
        fields = ['company_name', 'position', 'start_date', 'end_date']

class ExperienceInformationTwoForm(forms.ModelForm):
    class Meta:
        model = ExperienceInformationTwo
        fields = ['company_name', 'position', 'start_date', 'end_date']


class ExperienceInformationThreeForm(forms.ModelForm):
    class Meta:
        model = ExperienceInformationThree
        fields = ['company_name', 'position', 'start_date', 'end_date']



class TrainingInformationForm(forms.ModelForm):
    class Meta:
        model = TrainingInformation
        fields = ['name_of_training', 'training_institute', 'duration']


class ContactInformationForm(forms.ModelForm):
    class Meta:
        model = ContactInformation
        fields = ['contact_number', 'emergency_contact', 'email', 'present_address', 'permanent_address']


class Reference1Form(forms.ModelForm):
    class Meta:
        model = Reference1
        fields = ['name', 'organization', 'designation', 'primary_mobile_number', 'primary_email', 'relation']

class Reference2Form(forms.ModelForm):
    class Meta:
        model = Reference2
        fields = ['name', 'organization', 'designation', 'primary_mobile_number', 'primary_email', 'relation']