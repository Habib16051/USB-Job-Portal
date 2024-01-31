from django.db import models

# Create your models here.

class PersonalInfo(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ]
    
    MARITAL_STATUS_CHOICES = [
        ('Single', 'Single'),
        ('Married', 'Married'),
        ('Separated', 'Separated'),
        ]
    NATIONALITY_CHOICES = [
        ('Bangladeshi', 'Bangladeshi'),
        ('Other', 'Other Country'),]
    
    full_name = models.CharField(max_length=100)
    father_name     = models.CharField(max_length=100)
    Mother_Name     = models.CharField(max_length=100)
    gender          = models.CharField(max_length=100, choices=GENDER_CHOICES)
    marital_status  = models.CharField(max_length=100, choices=MARITAL_STATUS_CHOICES)
    nationality     = models.CharField(max_length=40, choices=NATIONALITY_CHOICES)
    passport        = models.CharField(max_length=20)
    nid             = models.CharField(max_length=20)
    date_of_birth   = models.DateField()
    cv              = models.FileField(upload_to='cv_pdfs/', null=True, blank=True)


    def __str__(self):
        return f"{self.full_name}"
    


class CareerApplicationInfo(models.Model):
    LOOKING_FOR_CHOICES = [
        ('Entry Level', 'Entry Level'),
        ('Mid Level', 'Mid Level'),
        ('Top Level', 'Top Level'),
    ]

    looking_for                          = models.CharField(max_length=20, choices=LOOKING_FOR_CHOICES)
    present_salary                       = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    expected_salary                      = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    preferred_job_categor                = models.CharField(max_length=100)
    preferred_district                   = models.CharField(max_length=100)
    preferred_ogranization_type          = models.CharField(max_length=100)



class ExperienceInformationOne(models.Model):
    company_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.company_name} - {self.position}"


class ExperienceInformationTwo(models.Model):
    company_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.company_name} - {self.position}"

class ExperienceInformationThree(models.Model):
    company_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.company_name} - {self.position}"


class TrainingInformation(models.Model):
    name_of_training = models.CharField(max_length=100)
    training_institute = models.TextField(max_length=100)
    duration = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name_of_training} at {self.training_institute}"
    


class ContactInformation(models.Model):
    contact_number = models.CharField(max_length=15)
    emergency_contact = models.CharField(max_length=15)
    email = models.EmailField()
    present_address = models.TextField()
    permanent_address = models.TextField()

    def __str__(self):
        return f"Contact Information - {self.contact_number}"
    



class Reference1(models.Model):
    name = models.CharField(max_length=100)
    organization = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    primary_mobile_number = models.CharField(max_length=15)
    primary_email = models.EmailField()
    relation = models.CharField(max_length=50)

    def __str__(self):
        return f"Reference: {self.name} ({self.organization})"


class Reference2(models.Model):
    name = models.CharField(max_length=100)
    organization = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    primary_mobile_number = models.CharField(max_length=15)
    primary_email = models.EmailField()
    relation = models.CharField(max_length=50)

    def __str__(self):
        return f"Reference: {self.name} ({self.organization})"