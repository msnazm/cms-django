# Generated by Django 4.0.2 on 2022-02-11 09:32

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, help_text='نام عنوان را وارد کنید.', max_length=255, unique=True, verbose_name='عنوان')),
                ('image', models.ImageField(blank=True, help_text='عکس مورد نظر را انتخاب کنید.', unique=True, upload_to='img', verbose_name='عکس')),
                ('body', ckeditor.fields.RichTextField(blank=True, help_text='توضیحات را وارد کنید.', unique=True, verbose_name='توضیحات')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='تاریخ آخرین تغییرات')),
            ],
            options={
                'verbose_name': 'خبرها',
                'verbose_name_plural': 'خبر ها',
            },
        ),
        migrations.CreateModel(
            name='keywords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(help_text='کلمات کلیدی را وارد کنید.', max_length=20, unique=True, verbose_name='کلمات کلیدی')),
                ('keywordes', models.ManyToManyField(help_text='کلمات کلیدی را وارد کنید.', related_name='key', to='news.New', verbose_name='کلمات کلیدی')),
            ],
        ),
    ]