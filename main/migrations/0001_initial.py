# Generated by Django 4.0.2 on 2022-02-11 09:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='about',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namepage', models.CharField(blank=True, help_text='نام صفحه را وارد کنید.', max_length=70, unique=True, verbose_name='نام صفحه')),
                ('title', models.CharField(blank=True, help_text='عنوان صفحه را وارد کنید.', max_length=70, unique=True, verbose_name='عنوان')),
                ('description', models.TextField(blank=True, help_text='توضیحات را وارد کنید.', null=True, unique=True, verbose_name='توضیحات')),
            ],
            options={
                'verbose_name': 'درباره ما',
                'verbose_name_plural': 'درباره ما',
            },
        ),
        migrations.CreateModel(
            name='AdMain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, help_text='عنوان آگهی را وارد کنید.', max_length=200, unique=True, verbose_name='عنوان آگهی')),
                ('servicetopic', models.CharField(blank=True, help_text='توضیحات را وارد کنید.', max_length=70, unique=True, verbose_name='توضیحات')),
                ('image', models.ImageField(help_text='عکس آگهی را انتخاب کنید.', upload_to='images/', verbose_name='عکس آگهی')),
            ],
            options={
                'verbose_name': 'آگهی ها',
                'verbose_name_plural': 'آگهی ها',
            },
        ),
        migrations.CreateModel(
            name='CategoryNew',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='نام دسته بندی اخبار را وارد کنید.', max_length=20, verbose_name='نام دسته بندی')),
            ],
            options={
                'verbose_name': 'دسته بندی اخبار',
                'verbose_name_plural': 'دسته بندی اخبار',
            },
        ),
        migrations.CreateModel(
            name='comment_center',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='عنوان را وارد کنید.', max_length=50, unique=True, verbose_name='عنوان')),
                ('description', models.TextField(help_text='توضیحات را وارد کنید.', verbose_name='توضیحات')),
            ],
            options={
                'verbose_name': 'توضیحات قسمت وسط',
                'verbose_name_plural': 'توضیحات قسمت وسط',
            },
        ),
        migrations.CreateModel(
            name='CommentCenterButton',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, help_text='توضیحات را وارد کنید.', null=True, unique=True, verbose_name='توضیحات')),
                ('button_link', models.CharField(blank=True, help_text='پیوند دکمه را وارد کنید.', max_length=200, null=True, unique=True, verbose_name='پیوند دکمه')),
            ],
            options={
                'verbose_name': 'متن صفحه همراه دکمه',
                'verbose_name_plural': 'متن صفحه همراه دکمه',
            },
        ),
        migrations.CreateModel(
            name='contact_us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='عنوان را وارد کنید.', max_length=50, unique=True, verbose_name='عنوان')),
                ('tell', models.CharField(help_text='تلفن را وارد کنید.', max_length=20, unique=True, verbose_name='تلفن')),
                ('email', models.EmailField(help_text='ایمیل را وارد کنید.', max_length=254, unique=True, verbose_name='ایمیل')),
                ('adress', models.CharField(help_text='آدرس را وارد کنید.', max_length=200, verbose_name='آدرس')),
                ('description', models.TextField(help_text='توضیحات را وارد کنید.', verbose_name='توضیحات')),
            ],
            options={
                'verbose_name': 'تماس با ما',
                'verbose_name_plural': 'تماس با ما',
            },
        ),
        migrations.CreateModel(
            name='footer_comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='عنوان را وارد کنید.', max_length=50, unique=True, verbose_name='عنوان')),
                ('description', models.TextField(help_text='توضیحات را وارد کنید.', verbose_name='توضیحات')),
            ],
            options={
                'verbose_name': 'توضیحات پایین',
                'verbose_name_plural': 'توضیحات پایین',
            },
        ),
        migrations.CreateModel(
            name='navbar_basic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_name', models.CharField(blank=True, help_text='نام منو را وارد کنید.', max_length=120, unique=True, verbose_name='نام منو')),
                ('menu_link', models.CharField(blank=True, help_text='پیوند منو را وارد کنید.', max_length=200, null=True, unique=True, verbose_name='پیوند منو')),
            ],
            options={
                'verbose_name': 'منواصلی',
                'verbose_name_plural': 'منوهای اصلی',
            },
        ),
        migrations.CreateModel(
            name='navbar_up',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_name', models.CharField(blank=True, help_text='نام منو را وارد کنید.', max_length=120, unique=True, verbose_name='نام منو')),
                ('menu_link', models.CharField(blank=True, help_text='پیوند منو را وارد کنید.', max_length=200, null=True, unique=True, verbose_name='پیوند منو')),
            ],
            options={
                'verbose_name': 'منو بالا',
                'verbose_name_plural': 'منوهای بالا',
            },
        ),
        migrations.CreateModel(
            name='service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, help_text='تیتر خذملت را وارد کنید.', max_length=200, unique=True, verbose_name='تیتر خدمات')),
                ('description', models.TextField(blank=True, help_text='توضیحات خدمات را وارد کنید.', unique=True, verbose_name='توضیحات')),
                ('image', models.ImageField(help_text='عکس را انتخاب کنید.', upload_to='images/', verbose_name='عکس')),
            ],
            options={
                'verbose_name': 'خدمات',
                'verbose_name_plural': 'خدمات',
            },
        ),
        migrations.CreateModel(
            name='slider_up',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(help_text='عکس را انتخاب کنید.', upload_to='images/', verbose_name='عکس')),
            ],
            options={
                'verbose_name': 'اسلایدر',
                'verbose_name_plural': 'اسلایدر اصلی',
            },
        ),
        migrations.CreateModel(
            name='serviceitem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servicetopics', models.CharField(blank=True, help_text='خدمات را وارد کنید.', max_length=70, unique=True, verbose_name='خدمات')),
                ('service', models.ForeignKey(help_text='نام دسته بندی خدمات را انتخاب کنید.', on_delete=django.db.models.deletion.CASCADE, to='main.service', verbose_name='نام دسته بندی')),
            ],
            options={
                'verbose_name': 'موارد خدمات',
                'verbose_name_plural': 'موارد خدمات',
            },
        ),
        migrations.CreateModel(
            name='PartsCommentCenter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, help_text='توضیحات را وارد کنید.', null=True, unique=True, verbose_name='توضیحات')),
                ('service', models.ForeignKey(help_text='نام دسته بندی خدمات را انتخاب کنید.', on_delete=django.db.models.deletion.CASCADE, to='main.service', verbose_name='نام دسته بندی')),
            ],
            options={
                'verbose_name': 'توضیحات خدمات',
                'verbose_name_plural': 'توضیحات خدمات',
            },
        ),
        migrations.CreateModel(
            name='NewMain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='عنوان اخبار را وارد کنید.', max_length=255, verbose_name='عنوان')),
                ('image', models.ImageField(help_text='عکس اخبار را انتخاب کنید.', upload_to='img', verbose_name='عکس')),
                ('body', models.TextField(help_text='توضیحات اخبار را وارد کنید.', verbose_name='توضیحات')),
                ('created_on', models.DateTimeField(auto_now_add=True, help_text='زمان ایجاد اخبار', verbose_name='زمان ایجاد اخبار')),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('categories', models.ManyToManyField(help_text='نام دسته بندی اخبار را انتخاب کنید.', related_name='NewMain', to='main.CategoryNew', verbose_name='نام دسته بندی')),
            ],
            options={
                'verbose_name': 'ایجاد اخبار',
                'verbose_name_plural': 'ایجاد اخبار',
            },
        ),
        migrations.CreateModel(
            name='NavbarUnder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_name_u', models.CharField(blank=True, help_text='نام منو را وارد کنید.', max_length=120, unique=True, verbose_name='نام منو')),
                ('menu_link_u', models.CharField(blank=True, help_text='پیوند منو را وارد کنید.', max_length=200, null=True, unique=True, verbose_name='پیوند منو')),
                ('ids', models.ManyToManyField(related_name='NavbarUnders', to='main.navbar_basic')),
            ],
            options={
                'verbose_name': 'زیر منو',
                'verbose_name_plural': 'زیر منو',
            },
        ),
    ]
