from django.contrib import admin
from testApp.models import PuneJobs,HydJobs,BloreJobs,ChennaiJobs

# Register your models here.

class PuneJobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','eligibility','address','email','phoneNumber']

class HydJobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','eligibility','address','email','phoneNumber']

class BloreJobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','eligibility','address','email','phoneNumber']

class ChennaiJobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','eligibility','address','email','phoneNumber']

admin.site.register(PuneJobs,PuneJobsAdmin)
admin.site.register(HydJobs,HydJobsAdmin)
admin.site.register(BloreJobs,BloreJobsAdmin)
admin.site.register(ChennaiJobs,ChennaiJobsAdmin)

