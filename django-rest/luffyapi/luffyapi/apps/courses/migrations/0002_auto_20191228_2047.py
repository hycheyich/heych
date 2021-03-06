# Generated by Django 2.2 on 2019-12-28 12:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='teacher', verbose_name='讲师封面'),
        ),
        migrations.CreateModel(
            name='CourseExpire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orders', models.IntegerField(verbose_name='显示顺序')),
                ('is_show', models.BooleanField(default=False, verbose_name='是否上架')),
                ('is_delete', models.BooleanField(default=False, verbose_name='逻辑删除')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('expire', models.CharField(help_text='课程有效期', max_length=100, verbose_name='课程有效期(月)')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='课程价格')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courseexpire', to='courses.Course', verbose_name='课程ID')),
            ],
            options={
                'verbose_name': '课程与有效期',
                'verbose_name_plural': '课程与有效期',
                'db_table': 'ly_course_expire',
            },
        ),
    ]
