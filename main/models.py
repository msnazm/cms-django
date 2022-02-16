from django.db import models

# Create your models here.

class navbar_up(models.Model):
    menu_name = models.CharField(max_length=120,unique=True,blank=True,help_text=('نام منو را وارد کنید.'),verbose_name=('نام منو'))
    menu_link = models.CharField(max_length=200,null=True,unique=True,blank=True,help_text=('پیوند منو را وارد کنید.'),verbose_name=('پیوند منو'))
    class Meta:
        verbose_name = "منو بالا"
        verbose_name_plural ="منوهای بالا"
    def __str__(self):
        return self.menu_name       
class navbar_basic(models.Model):
    menu_name = models.CharField(max_length=120,unique=True,blank=True,help_text=('نام منو را وارد کنید.'),verbose_name=('نام منو'))
    menu_link = models.CharField(max_length=200,null=True,unique=True,blank=True,help_text=('پیوند منو را وارد کنید.'),verbose_name=('پیوند منو'))
    class Meta:
        verbose_name = "منواصلی"
        verbose_name_plural ="منوهای اصلی"
    def __str__(self):
        return self.menu_name        
class NavbarUnder(models.Model):
    menu_name_u = models.CharField(max_length=120,unique=True,blank=True,help_text=('نام منو را وارد کنید.'),verbose_name=('نام منو'))
    menu_link_u = models.CharField(max_length=200,null=True,unique=True,blank=True,help_text=('پیوند منو را وارد کنید.'),verbose_name=('پیوند منو'))
    ids = models.ManyToManyField('navbar_basic', related_name='NavbarUnders')
    class Meta:
        verbose_name = "زیر منو"
        verbose_name_plural ="زیر منو"        
class slider_up(models.Model):
    image = models.ImageField(upload_to='images/',help_text=('عکس را انتخاب کنید.'),verbose_name=('عکس'))
    class Meta:
        verbose_name = "اسلایدر"
        verbose_name_plural ="اسلایدر اصلی"
class contact_us(models.Model):
    limits = 1
    title = models.CharField(max_length=50,unique=True,blank=False,help_text=('عنوان را وارد کنید.'),verbose_name=('عنوان'))
    tell = models.CharField(max_length=20,unique=True,blank=False,help_text=('تلفن را وارد کنید.'),verbose_name=('تلفن'))
    email = models.EmailField(max_length=254,unique=True,help_text=('ایمیل را وارد کنید.'),verbose_name=('ایمیل'))
    adress = models.CharField(max_length=200,help_text=('آدرس را وارد کنید.'),verbose_name=('آدرس'))
    description = models.TextField(help_text=('توضیحات را وارد کنید.'),verbose_name=('توضیحات'))
    class Meta:
        verbose_name = "تماس با ما"
        verbose_name_plural ="تماس با ما"
    def __str__(self):
        return self.tell
class footer_comment(models.Model):
    title = models.CharField(max_length=50,unique=True,blank=False,help_text=('عنوان را وارد کنید.'),verbose_name=('عنوان'))
    description = models.TextField(help_text=('توضیحات را وارد کنید.'),verbose_name=('توضیحات'))
    class Meta:
        verbose_name = "توضیحات پایین"
        verbose_name_plural ="توضیحات پایین"
    def __str__(self):
        return self.title  
class CategoryNew(models.Model):
    name = models.CharField(max_length=20,help_text=('نام دسته بندی اخبار را وارد کنید.'),verbose_name=('نام دسته بندی'))
    class Meta:
        verbose_name = "دسته بندی اخبار"
        verbose_name_plural ="دسته بندی اخبار"
    def __str__(self):
        return self.name

class NewMain(models.Model):
    title = models.CharField(max_length=255,help_text=('عنوان اخبار را وارد کنید.'),verbose_name=('عنوان'))
    image = models.ImageField(upload_to='img',help_text=('عکس اخبار را انتخاب کنید.'),verbose_name=('عکس'))   
    body = models.TextField(help_text=('توضیحات اخبار را وارد کنید.'),verbose_name=('توضیحات'))
    created_on = models.DateTimeField(auto_now_add=True,help_text=('زمان ایجاد اخبار'),verbose_name=('زمان ایجاد اخبار'))
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('CategoryNew', related_name='NewMain',help_text=('نام دسته بندی اخبار را انتخاب کنید.'),verbose_name=('نام دسته بندی'))
    class Meta:
        verbose_name = "ایجاد اخبار"
        verbose_name_plural ="ایجاد اخبار"
    def __str__(self):
        return self.title 

class comment_center(models.Model):
    title = models.CharField(max_length=50,unique=True,blank=False,help_text=('عنوان را وارد کنید.'),verbose_name=('عنوان'))
    description = models.TextField(help_text=('توضیحات را وارد کنید.'),verbose_name=('توضیحات'))
    class Meta:
        verbose_name = "توضیحات قسمت وسط"
        verbose_name_plural ="توضیحات قسمت وسط"
    def __str__(self):
        return self.title			
		
class PartsCommentCenter(models.Model):
    service = models.ForeignKey('service', on_delete=models.CASCADE,help_text=('نام دسته بندی خدمات را انتخاب کنید.'),verbose_name=('نام دسته بندی'))
    description = models.TextField(null=True,unique=True,blank=True,help_text=('توضیحات را وارد کنید.'),verbose_name=('توضیحات'))
    class Meta:
        verbose_name = "توضیحات خدمات"
        verbose_name_plural ="توضیحات خدمات"
    def __str__(self):
        return self.description     

class service(models.Model):
    title = models.CharField(max_length=200,unique=True,blank=True,help_text=('تیتر خذملت را وارد کنید.'),verbose_name=('تیتر خدمات'))
    description = models.TextField(unique=True,blank=True,help_text=('توضیحات خدمات را وارد کنید.'),verbose_name=('توضیحات'))
    image = models.ImageField(upload_to='images/',help_text=('عکس را انتخاب کنید.'),verbose_name=('عکس'))
    class Meta:
        verbose_name = "خدمات"
        verbose_name_plural ="خدمات"
    def __str__(self):
        return self.title

class serviceitem(models.Model):
    servicetopics = models.CharField(max_length=70,unique=True,blank=True,help_text=('خدمات را وارد کنید.'),verbose_name=('خدمات'))
    service = models.ForeignKey('service', on_delete=models.CASCADE,help_text=('نام دسته بندی خدمات را انتخاب کنید.'),verbose_name=('نام دسته بندی'))
    class Meta:
        verbose_name = "موارد خدمات"
        verbose_name_plural ="موارد خدمات"
    def __str__(self):
        return self.servicetopics 

class about(models.Model):
    namepage = models.CharField(max_length=70,unique=True,blank=True,help_text=('نام صفحه را وارد کنید.'),verbose_name=('نام صفحه'))
    title = models.CharField(max_length=70,unique=True,blank=True,help_text=('عنوان صفحه را وارد کنید.'),verbose_name=('عنوان'))
    description = models.TextField(null=True,unique=True,blank=True,help_text=('توضیحات را وارد کنید.'),verbose_name=('توضیحات'))
    class Meta:
        verbose_name = "درباره ما"
        verbose_name_plural ="درباره ما"
    def __str__(self):
        return self.namepage    

class AdMain(models.Model):
    title = models.CharField(max_length=200,unique=True,blank=True,help_text=('عنوان آگهی را وارد کنید.'),verbose_name=('عنوان آگهی'))
    servicetopic = models.CharField(max_length=70,unique=True,blank=True,help_text=('توضیحات را وارد کنید.'),verbose_name=('توضیحات'))
    image = models.ImageField(upload_to='images/',help_text=('عکس آگهی را انتخاب کنید.'),verbose_name=('عکس آگهی'))
    class Meta:
        verbose_name = "آگهی ها"
        verbose_name_plural ="آگهی ها"
    def __str__(self):
        return self.title 
        
class CommentCenterButton(models.Model):
    description = models.TextField(null=True,unique=True,blank=True,help_text=('توضیحات را وارد کنید.'),verbose_name=('توضیحات'))
    button_link = models.CharField(max_length=200,null=True,unique=True,blank=True,help_text=('پیوند دکمه را وارد کنید.'),verbose_name=('پیوند دکمه'))
    class Meta:
        verbose_name = "متن صفحه همراه دکمه"
        verbose_name_plural ="متن صفحه همراه دکمه"
    def __str__(self):
        return self.description