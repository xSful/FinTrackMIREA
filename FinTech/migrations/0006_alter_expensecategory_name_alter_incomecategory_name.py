# Generated by Django 4.2.5 on 2023-09-20 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FinTech', '0005_expensecategory_user_incomecategory_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expensecategory',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='incomecategory',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
