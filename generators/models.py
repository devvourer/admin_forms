from django.db import models


text = 'text'
email = 'email'
file_field = 'file'

FIELDS_CHOICES = (
    (text, 'text'),
    (email, 'email'),
    (file_field, 'file')
)


class Generator(models.Model):
    template_name = models.CharField(max_length=150)
    identifier = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150)
    preview = models.ImageField(upload_to='images/', null=True, blank=True)
    image_one = models.ImageField(upload_to='images/%y/%m', null=True, blank=True)
    image_two = models.ImageField(upload_to='images/%y/%m', null=True, blank=True)
    image_three = models.ImageField(upload_to='images/%y/%m', null=True, blank=True)
    image_four = models.ImageField(upload_to='images/%y/%m', null=True, blank=True)
    name = models.CharField(max_length=150)
    icon = models.ImageField(upload_to='icons/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description_title = models.CharField(max_length=150)
    description = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Step(models.Model):
    generator = models.ForeignKey(Generator, related_name='steps', on_delete=models.CASCADE)
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Field(models.Model):
    step = models.ForeignKey(Step, related_name='fields', on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    placeholder = models.CharField(max_length=100)
    input_name = models.CharField(max_length=100)
    field = models.CharField(choices=FIELDS_CHOICES, max_length=30)
    require = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class FieldData(models.Model):
    data = models.JSONField()
