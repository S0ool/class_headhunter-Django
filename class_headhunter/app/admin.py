from django.contrib import admin

from app.models import Request, Resume, Vacancy, Skill, Company

# Register your models here.


admin.site.register([Vacancy, Resume, Request,Skill,Company])