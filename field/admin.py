from django.contrib import admin
from .models import PersonalInfo, CareerApplicationInfo, ExperienceInformationOne, ExperienceInformationTwo, \
    ExperienceInformationThree, TrainingInformation, ContactInformation, Reference1, Reference2

# Register PersonalInfo model
class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'gender', 'marital_status', 'nationality', 'passport', 'nid', 'date_of_birth']
    search_fields = ['full_name', 'passport', 'nid']
    list_filter = ['gender', 'marital_status', 'nationality']

admin.site.register(PersonalInfo, PersonalInfoAdmin)

# Register CareerApplicationInfo model
class CareerApplicationInfoAdmin(admin.ModelAdmin):
    list_display = ['looking_for', 'present_salary', 'expected_salary', 'preferred_job_categor', 'preferred_district',
                    'preferred_ogranization_type']
    search_fields = ['looking_for', 'preferred_job_categor', 'preferred_district', 'preferred_ogranization_type']

admin.site.register(CareerApplicationInfo, CareerApplicationInfoAdmin)

# Register ExperienceInformationOne model
class ExperienceInformationOneAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'position', 'start_date', 'end_date']
    search_fields = ['company_name', 'position']
    list_filter = ['start_date', 'end_date']

admin.site.register(ExperienceInformationOne, ExperienceInformationOneAdmin)

# Register ExperienceInformationTwo model
class ExperienceInformationTwoAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'position', 'start_date', 'end_date']
    search_fields = ['company_name', 'position']
    list_filter = ['start_date', 'end_date']

admin.site.register(ExperienceInformationTwo, ExperienceInformationTwoAdmin)

# Register ExperienceInformationThree model
class ExperienceInformationThreeAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'position', 'start_date', 'end_date']
    search_fields = ['company_name', 'position']
    list_filter = ['start_date', 'end_date']

admin.site.register(ExperienceInformationThree, ExperienceInformationThreeAdmin)

# Register TrainingInformation model
class TrainingInformationAdmin(admin.ModelAdmin):
    list_display = ['name_of_training', 'training_institute', 'duration']
    search_fields = ['name_of_training', 'training_institute']

admin.site.register(TrainingInformation, TrainingInformationAdmin)

# Register ContactInformation model
class ContactInformationAdmin(admin.ModelAdmin):
    list_display = ['contact_number', 'emergency_contact', 'email']
    search_fields = ['contact_number', 'emergency_contact', 'email']

admin.site.register(ContactInformation, ContactInformationAdmin)

# Register Reference1 model
class Reference1Admin(admin.ModelAdmin):
    list_display = ['name', 'organization', 'designation', 'primary_mobile_number', 'primary_email', 'relation']
    search_fields = ['name', 'organization', 'designation', 'primary_mobile_number', 'primary_email', 'relation']

admin.site.register(Reference1, Reference1Admin)

# Register Reference2 model
class Reference2Admin(admin.ModelAdmin):
    list_display = ['name', 'organization', 'designation', 'primary_mobile_number', 'primary_email', 'relation']
    search_fields = ['name', 'organization', 'designation', 'primary_mobile_number', 'primary_email', 'relation']

admin.site.register(Reference2, Reference2Admin)
