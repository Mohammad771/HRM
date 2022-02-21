from django.db import models

from job_management.models import job_titles, departments


class attachment_types(models.Model):
    attachment_type_id = models.AutoField(max_length=24, primary_key=True)
    attachment_type_name = models.CharField(max_length=24)
    attachment_type_status = models.IntegerField()
    attachment_type_created_at = models.DateTimeField()
    attachment_type_updated_at = models.DateTimeField()
    attachment_type_deleted_at = models.DateTimeField()


class attachments(models.Model):
    attachment_id = models.AutoField(max_length=24, primary_key=True)
    attachment_attachment_type_id = models.ForeignKey(attachment_types, default=None, on_delete=models.CASCADE, related_name="+")
    attachment_name = models.CharField(max_length=50)
    attachment_type = models.CharField(max_length=24)
    attachment_path = models.TextField()
    attachment_created_at = models.DateTimeField()
    attachment_updated_at = models.DateTimeField()
    attachment_deleted_at = models.DateTimeField()


class attachments_users(models.Model):
    attachment_user_id = models.AutoField(max_length=24, primary_key=True)
    attachment_user_user_id = models.ForeignKey('users', on_delete=models.CASCADE, related_name="+")
    attachment_user_attachment_id = models.ForeignKey(attachments, default=None, on_delete=models.CASCADE, related_name="+")
    attachment_user_created_at = models.DateTimeField()
    attachment_user_updated_at = models.DateTimeField()
    attachment_user_deleted_at = models.DateTimeField()


class countries(models.Model):
    country_id = models.AutoField(max_length=24, primary_key=True)
    country_ISO3 = models.IntegerField()
    country_ISO2 = models.IntegerField()
    country_arabic_name = models.CharField(max_length=264)
    country_english_name = models.CharField(max_length=264)
    country_nationality_arabic = models.CharField(max_length=264)
    country_nationality_english = models.CharField(max_length=264)
    country_flag = models.CharField(max_length=6)
    country_currency_name = models.CharField(max_length=50)
    country_code = models.CharField(max_length=5)
    country_currency_symbol = models.CharField(max_length=5)
    country_domain = models.CharField(max_length=10)
    country_dial_code = models.CharField(max_length=10)


class addresses(models.Model):
    address_id = models.AutoField(max_length=24, primary_key=True)
    address_building_number = models.IntegerField()
    address_street_name = models.CharField(max_length=24)
    address_district_name = models.CharField(max_length=24)
    address_city_name = models.CharField(max_length=24)
    address_zip_code = models.IntegerField()
    address_additional_number = models.IntegerField()
    address_unit_number = models.IntegerField()
    address_created_by = models.ForeignKey('users', on_delete=models.CASCADE, related_name="+")
    address_country_id = models.ForeignKey(countries, on_delete=models.CASCADE, related_name="+")
    address_created_at = models.DateTimeField()
    address_updated_at = models.DateTimeField()
    address_deleted_at = models.DateTimeField()


class users(models.Model):
    user_id = models.AutoField(max_length=24, primary_key=True)
    user_attachment_id = models.ForeignKey(attachments, default=None, on_delete=models.CASCADE, related_name="+")
    user_address_id = models.ForeignKey(addresses, default=None, on_delete=models.CASCADE, related_name="+")
    user_job_title_id = models.ForeignKey(job_titles, on_delete=models.CASCADE, related_name="+")
    user_type_id = models.ForeignKey('user_types', default=None, on_delete=models.CASCADE, related_name="+")
    user_employee_department = models.ForeignKey(departments, on_delete=models.CASCADE, related_name="+")
    user_first_name = models.CharField(max_length=24)
    user_middle_name = models.CharField(max_length=24)
    user_last_name = models.CharField(max_length=24)
    user_email = models.CharField(max_length=50, unique=True)
    user_mobile = models.IntegerField(unique=True)
    user_password_hash = models.TextField()
    user_activation_hash = models.TextField()
    user_is_active = models.BooleanField()
    user_status = models.BooleanField()
    user_education_degree = models.CharField(max_length=24)
    user_DOB = models.DateField()
    user_nationality_ID = models.IntegerField()
    user_created_at = models.DateTimeField()
    user_updated_at = models.DateTimeField()
    user_deleted_at = models.DateTimeField()


class user_types(models.Model):
    user_type_id = models.AutoField(max_length=24, primary_key=True)
    user_type_user_id = models.ForeignKey(users, on_delete=models.CASCADE, related_name="+")
    user_type_created_at = models.DateTimeField()
    user_type_updated_at = models.DateTimeField()
    user_type_deleted_at = models.DateTimeField()


class roles(models.Model):
    role_id = models.AutoField(max_length=24, primary_key=True)
    role_name = models.CharField(max_length=50)
    roles_created_at = models.DateTimeField()
    role_updated_at = models.DateTimeField()
    role_deleted_at = models.DateTimeField()


class permissions(models.Model):
    permission_id = models.AutoField(max_length=24, primary_key=True)
    permission_name = models.CharField(max_length=50)
    permission_created_at = models.DateTimeField()
    permission_updated_at = models.DateTimeField()
    permission_deleted_at = models.DateTimeField()


class roles_and_permissions(models.Model):
    role_and_permission_id = models.AutoField(max_length=24, primary_key=True)
    role_and_permission_role_id = models.ForeignKey(roles, on_delete=models.CASCADE)
    role_and_permission_permissions_id = models.ForeignKey(permissions, on_delete=models.CASCADE, related_name="+")
    role_and_permission_name = models.CharField(max_length=50)
    role_and_permission_level = models.IntegerField()
    role_and_permission_created_at = models.DateTimeField()
    role_and_permission_updated_at = models.DateTimeField()
    role_and_permission_name_deleted_at = models.DateTimeField()


class courses(models.Model):
    course_id = models.AutoField(max_length=24, primary_key=True)
    course_attachments_id = models.ForeignKey(attachments, on_delete=models.CASCADE, related_name="+")
    course_user_id = models.ForeignKey(users, on_delete=models.CASCADE, related_name="+")
    course_title = models.CharField(max_length=264)
    course_DOC = models.DateField()
    course_length = models.IntegerField()
    course_provider = models.CharField(max_length=264)
    course_created_at = models.DateTimeField()
    course_updated_at = models.DateTimeField()
    course_deleted_at = models.DateTimeField()


class skills(models.Model):
    skill_id = models.AutoField(max_length=24, primary_key=True)
    skill_user_id = models.ForeignKey(users, on_delete=models.CASCADE, related_name="+")
    skill_name = models.CharField(max_length=50)
    skill_rating = models.IntegerField()
    skill_created_at = models.DateTimeField()
    skill_updated_at = models.DateTimeField()
    skill_deleted_at = models.DateTimeField()


''' class spoken_languages(models.Model):
    spoken_language_id = models.IntegerField(max_length=24,primary_key=True, autoincrement=True)
    user_id = models.ForeignKey(users, on_delete=models.CASCADE)
    rating = models.IntegerField(max_length=2)
    spoken_language_created_at = models.DateTimeField()
    spoken_language_updated_at = models.DateTimeField()
    spoken_language_deleted_at = models.DateTimeField()
    '''
