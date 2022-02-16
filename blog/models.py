from django.db import models
from ckeditor.fields import RichTextField

class keywords(models.Model):

    keyword = models.CharField(max_length=20,unique=True,help_text=('کلمات کلیدی را وارد کنید.'),verbose_name=('کلمات کلیدی'))

class Post(models.Model):

    title = models.CharField(max_length=255,help_text=('عنوان پست را وارد کنید.'),verbose_name=('عنوان'))

    image = models.ImageField(upload_to='img',help_text=('عکس پست را انتخاب کنید.'),verbose_name=('عکس'))
    
    body = RichTextField(unique=True,blank=True,help_text=('توضیحات را وارد کنید.'),verbose_name=('توضیحات'))
    
    created_on = models.DateTimeField(auto_now_add=True,help_text=('زمان پست'),verbose_name=('زمان پست'))

    last_modified = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = "پست ها"
        verbose_name_plural ="پست ها"
    def __str__(self):
        return self.title
        
class Comment(models.Model):

    author = models.CharField(max_length=60,help_text=('اسم خود را وارد کنید.'),verbose_name=('اسم'),error_messages={
            'required': 'my required msg..',
        })

    body = models.TextField(help_text=('متن را وارد کنید.'),verbose_name=('متن'))

    created_on = models.DateTimeField(auto_now_add=True,help_text=('زمان ایجاد پست.'),verbose_name=('زمان ایجاد'))

    post = models.ForeignKey('Post', on_delete=models.CASCADE,help_text=('پست را انتخاب کنید.'),verbose_name=('انتخاب پست'))
    
    class Meta:
        verbose_name = "نظرها"
        verbose_name_plural ="نظرها"
    def __str__(self):
        return self.author