from django.db import models

# Create your models here.



# class College(models.Model):
#     college_name=models.CharField(max_length=100)

class NewCollegeBasicInfo(models.Model):
    college_name = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    phone_number = models.CharField(max_length=200, blank=True, null=True)
    country_id = models.CharField(max_length=200, blank=True, null=True)
    state_id = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    university_id = models.CharField(max_length=200, blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    accredited_by = models.CharField(max_length=200, blank=True, null=True)
    approved_by = models.CharField(max_length=200, blank=True, null=True)
    campuz_size = models.CharField(max_length=200, blank=True, null=True)
    established_on = models.CharField(max_length=200, blank=True, null=True)
    genders_accepted = models.CharField(max_length=200, blank=True, null=True)
    image = models.CharField(max_length=100, blank=True, null=True)
    logo = models.CharField(max_length=1000, blank=True, null=True)
    ownership = models.CharField(max_length=200, blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    type = models.CharField(max_length=200, blank=True, null=True)
    course_types = models.CharField(max_length=200, blank=True, null=True)
    degrees = models.CharField(max_length=200, blank=True, null=True)
    colg_type = models.CharField(max_length=200, blank=True, null=True)
    created_date = models.CharField(max_length=200, blank=True, null=True)
    created_time = models.CharField(max_length=200, blank=True, null=True)
    affiliation = models.CharField(max_length=200, blank=True, null=True)
    banner = models.TextField(blank=True, null=True)
    facilities = models.CharField(max_length=200, blank=True, null=True)
    modification_time = models.CharField(max_length=200, blank=True, null=True)
    placement = models.CharField(max_length=200, blank=True, null=True)
    placement_average = models.CharField(max_length=200, blank=True, null=True)
    placement_high = models.CharField(max_length=200, blank=True, null=True)
    short_desc = models.TextField(blank=True, null=True)
    scholarship_providing_college = models.CharField(max_length=10)
    college_website = models.CharField(max_length=200)
    banner_alt_text = models.CharField(max_length=200)
    logo_alt_text = models.CharField(max_length=200)
    college_name_slug = models.CharField(max_length=200)
    top_courses = models.CharField(max_length=200)
    placement_description = models.TextField()
    keywords = models.CharField(max_length=200)
    verified_by_college_partner = models.CharField(max_length=45)
    college_partner_id = models.CharField(max_length=200)
    commission = models.CharField(max_length=200)
    approved_by_admin = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'new_college_basic_info'

    def __str__(self):
        return self.college_name




class NewCollegeCollegeCities(models.Model):
    country_id = models.CharField(max_length=200, blank=True, null=True)
    state_id = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    created_at = models.CharField(max_length=200, blank=True, null=True)
    updated_at = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'new_college_college_cities'  
        
    def __str__(self):
        return self.city
