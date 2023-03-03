from datetime import datetime
from django.db import models
from django.template.defaultfilters import slugify

class Category(models.TextChoices):

    WEIGHTLOSS = 'weightloss'
    MUSCLE_GAIN = 'muscle gain'
    GUT_HEALTH = 'gut health'
    HEALTHY_EATING = 'healthy eating'
    EXERCISE = 'exercise'


class WellnessProgram(models.Model):

    name = models.CharField(max_length=60)
    slug = models.CharField(max_length=200, unique=True)
    short_description = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True,null=True)
    thumbnail = models.ImageField()
    is_active = models.BooleanField(default=True)
    category = models.CharField(max_length=60, choices=Category.choices, default=Category.WEIGHTLOSS)
    date_created = models.DateTimeField(default=datetime.now, blank=True)

    def save(self, *args,**kwargs):
        original_slug = slugify(self.name)
        queryset = WellnessProgram.objects.all().filter(slug__iexact=original_slug).count()

        count = 1
        slug = original_slug

        while(queryset):
            slug = original_slug + '_' + str(count)
            count +=1
            queryset = WellnessProgram.objects.all().filter(slug__iexact=slug).count()

        self.slug = slug

        if self.is_active:
            try:
                temp = WellnessProgram.objects.get(is_active=True)
                if self != temp:
                    temp.is_active = False
                    temp.save()

            except WellnessProgram.DoesNotExist:
                pass

        super(WellnessProgram, self).save(*args,**kwargs)

    def __str__(self) -> str:
        return self.name
