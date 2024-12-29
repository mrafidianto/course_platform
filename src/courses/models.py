from django.db import models
from django.utils.text import slugify

"""
- Courses:
	- Title
	- Description
	- Thumbnail/Image
	- Access:
		- Anyone
		- Email required
        - Purchase required
		- User required (n/a)
	- Status: 
		- Published
		- Coming Soon
		- Draft
"""
class AccessRequirements(models.TextChoices):
    ANYONE = 'any', 'Anyone'
    EMAIL_REQUIRED = 'email_required', 'Email Required'

class PublishStatus(models.TextChoices):
    PUBLISHED = 'pub', 'Published'
    COMING_SOON = 'soon', 'Coming Soon'
    DRAFT = 'draft', 'Draft'

def handle_upload(instance, filename):
    slug_title = slugify(instance.title)
    return f'course_image/{slug_title}/{filename}'

class Courses(models.Model):

    class Meta:
        db_table = 'courses'
        verbose_name = 'Courses'
        verbose_name_plural = 'Courses'

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to=handle_upload, null=True)
    access = models.CharField(max_length=14, choices=AccessRequirements.choices, default=AccessRequirements.EMAIL_REQUIRED)
    status = models.CharField(max_length=10, choices=PublishStatus.choices, default=PublishStatus.DRAFT)

    @property
    def is_published(self):
        return self.status == PublishStatus.PUBLISHED
"""
- Lessons
		- Title
		- Description
		- Video
		- Status: Published, Coming Soon, Draft
"""
