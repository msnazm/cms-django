from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class keywords(models.Model):

    keyword = models.CharField(max_length=20,unique=True,help_text=('کلمات کلیدی را وارد کنید.'),verbose_name=('کلمات کلیدی'))

    keywordes = models.ManyToManyField('New', related_name='key',help_text=('کلمات کلیدی را وارد کنید.'),verbose_name=('کلمات کلیدی'))
        

class New(models.Model):

    title = models.CharField(max_length=255,unique=True,blank=True,help_text=('نام عنوان را وارد کنید.'),verbose_name=('عنوان'))

    image = models.ImageField(upload_to='img',unique=True,blank=True,help_text=('عکس مورد نظر را انتخاب کنید.'),verbose_name=('عکس'))
    
    body = RichTextField(unique=True,blank=True,help_text=('توضیحات را وارد کنید.'),verbose_name=('توضیحات'))

    created_on = models.DateTimeField(auto_now_add=True,verbose_name=('تاریخ ایجاد'))

    last_modified = models.DateTimeField(auto_now=True,verbose_name=('تاریخ آخرین تغییرات'))


    
    class Meta:
        verbose_name = "خبرها"
        verbose_name_plural ="خبر ها"
    def __str__(self):
        return self.title
        