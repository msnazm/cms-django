from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100,help_text=('عنوان پروژه را وارد کنید.'),verbose_name=('عنوان'))
    description = models.TextField(help_text=('توضیحات پروژه را وارد کنید.'),verbose_name=('توضیحات'))
    technology = models.CharField(max_length=20,help_text=('تکنولوژی را وارد کنید.'),verbose_name=('تکنولوژی'))
    image = models.ImageField(upload_to='img',help_text=('عکس را انتخاب کنید.'),verbose_name=('عکس'))
    class Meta:
        verbose_name = "پروژه"
        verbose_name_plural ="پروژه ها"
    def __str__(self):
        return self.title