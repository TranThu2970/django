from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
class Radar(models.Model):
    FREQUENCY = (
        ('Sóng m', 'Sóng m'),
        ('Sóng dm', 'Sóng dm'),
        ('Sóng cm', 'Sóng cm')
    )
    name = models.CharField(max_length=255)
    avatar = models.ImageField(null=True, blank=True, upload_to="images", default="/images/placeholder.png")
    freq = models.CharField(max_length=200, null=True, choices=FREQUENCY)
    display = models.BooleanField(default=True)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
	    return self.name
	#create URL
    def save(self, *args, **kwargs):
	    if self.slug == None:
		    slug = slugify(self.name)

		    has_slug = Radar.objects.filter(slug=slug).exists()
		    count = 1
		    while has_slug:
			    count += 1
			    slug = slugify(self.name) + '-' + str(count) 
			    has_slug = Radar.objects.filter(slug=slug).exists()

		    self.slug = slug

	    super().save(*args, **kwargs)


class Content(models.Model):
    radar = models.ForeignKey(Radar, null= True, on_delete= models.SET_NULL)
    name = models.CharField(max_length=255)

    def __str__(self):
	    return f'{self.radar.name + " - " + self.name}'


class ContentA(models.Model):
    radar = models.ForeignKey(Radar, null= True, on_delete= models.SET_NULL)
    content = models.ForeignKey(Content, null= True, on_delete= models.SET_NULL)
    name = models.CharField(max_length=255)
    
    def __str__(self):
	    return f'{self.content.name + " - " + self.name}'


class ContentB(models.Model):
    radar = models.ForeignKey(Radar, null= True, on_delete= models.SET_NULL)
    content = models.ForeignKey(Content, null= True, on_delete= models.SET_NULL)
    contentA = models.ForeignKey(ContentA, null= True, on_delete= models.SET_NULL)
    name = models.CharField(max_length=255)
    description = RichTextUploadingField(null=True, blank=True)
    
    def __str__(self):
	    return f'{self.content.name + " - " + self.contentA.name + " - " + self.name}'