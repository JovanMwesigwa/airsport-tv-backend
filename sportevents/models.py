from django.db import models

# Create your models here.


class SportEvent(models.Model):
    STATUS_CHOICES = (
        ('upcoming', 'upcoming'),
        ('live', 'live'),
        ('finished', 'finished'),
    )
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    country = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    country_flag = models.CharField(max_length=200, blank=True, null=True)
    # create the event media file with a proper named folder structure
    isSport = models.BooleanField(default=True)
    event_media = models.FileField(
        upload_to='event_media/%Y/%m/%d/', blank=True, null=True)
    thumbnail = models.ImageField(
        upload_to='event_media/thumbnail/%Y/%m/%d/', blank=True, null=True)
    category = models.ForeignKey(
        'Category', on_delete=models.CASCADE, null=True)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='upcoming')
    main = models.BooleanField(default=False)


    # order the events by start date
    class Meta:
        ordering = ['-start_date']

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name
