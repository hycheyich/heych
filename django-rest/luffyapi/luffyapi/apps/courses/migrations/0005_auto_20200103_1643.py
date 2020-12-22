# Generated by Django 2.2 on 2020-01-03 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_activity_courseactivity_pricediscount_pricediscounttype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricediscount',
            name='sale',
            field=models.TextField(help_text='\n    0表示免费；<br>\n    *号开头加上浮点数表示折扣价，例如*0.82表示八二折；<br>\n    -号开头加上整数表示减免价格，例如-50表示减免50元；<br>\n    如果要表示限时满减,则需要使用 原价-优惠价格,例如表示,课程价格大于100,优惠10;大于200,优惠20,格式如下:<br>\n    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;满100-10<br>\n    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;满200-20<br>\n    ', verbose_name='优惠公式'),
        ),
    ]