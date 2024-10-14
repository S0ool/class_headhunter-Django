from django.db import models
from django.contrib.auth.models import User

class Skill(models.Model):
    name = models.CharField(max_length=255)
    percent = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Resume(models.Model):
    dream_job = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255, blank=True,null=True)
    birth_date = models.DateField(blank=True,null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    skills = models.ManyToManyField(Skill, related_name='resume')
    experience = models.TextField(blank=True,default='No experience')
    education = models.TextField(blank=True,default='No education')
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('none', 'Prefer not to say'),
    )
    gender = models.CharField(max_length=255, blank=True, null=True, choices=GENDER_CHOICES)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='resume')

    def __str__(self):
        return self.name

class Company(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    address = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Vacancy(models.Model):
    title = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    skills = models.ManyToManyField(Skill, related_name='vacancy_skills')
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='vacancy')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Request(models.Model):
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE)
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    )
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"{self.vacancy} - {self.resume}"
