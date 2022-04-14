# Generated by Django 4.0.3 on 2022-04-07 21:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('store', '0002_alter_product_category_alter_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('available', models.IntegerField()),
                ('reserved', models.IntegerField()),
                ('on_order', models.IntegerField()),
                ('damaged', models.IntegerField()),
                ('value', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='product', to='store.product')),
            ],
        ),
    ]