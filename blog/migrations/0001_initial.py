# Generated by Django 4.0.2 on 2022-02-11 09:35

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='keywords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(help_text='کلمات کلیدی را وارد کنید.', max_length=20, unique=True, verbose_name='کلمات کلیدی')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='عنوان پست را وارد کنید.', max_length=255, verbose_name='عنوان')),
                ('image', models.ImageField(help_text='عکس پست را انتخاب کنید.', upload_to='img', verbose_name='عکس')),
                ('body', ckeditor.fields.RichTextField(blank=True, help_text='توضیحات را وارد کنید.', unique=True, verbose_name='توضیحات')),
                ('created_on', models.DateTimeField(auto_now_add=True, help_text='زمان پست', verbose_name='زمان پست')),
                ('last_modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'پست ها',
                'verbose_name_plural': 'پست ها',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(error_messages={'required': 'my required msg..'}, help_text='اسم خود را وارد کنید.', max_length=60, verbose_name='اسم')),
                ('body', models.TextField(help_text='متن را وارد کنید.', verbose_name='متن')),
                ('created_on', models.DateTimeField(auto_now_add=True, help_text='زمان ایجاد پست.', verbose_name='زمان ایجاد')),
                ('post', models.ForeignKey(help_text='پست را انتخاب کنید.', on_delete=django.db.models.deletion.CASCADE, to='blog.post', verbose_name='انتخاب پست')),
            ],
            options={
                'verbose_name': 'نظرها',
                'verbose_name_plural': 'نظرها',
            },
        ),
    ]
