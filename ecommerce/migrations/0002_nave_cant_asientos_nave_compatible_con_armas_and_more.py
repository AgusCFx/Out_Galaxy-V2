# Generated by Django 4.2.3 on 2023-07-27 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='nave',
            name='cant_asientos',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='nave',
            name='compatible_con_armas',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='nave',
            name='descripcion',
            field=models.TextField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='nave',
            name='precio',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='nave',
            name='tipo',
            field=models.CharField(choices=[('Empresarial', 'Empresarial'), ('Deportivo', 'Deportivo'), ('Familiar', 'Familiar'), ('Utilitario', 'Utilitario'), ('Mineria', 'Mineria')], default='Familiar', max_length=20),
        ),
        migrations.CreateModel(
            name='Arma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=20)),
                ('modelo', models.CharField(max_length=20)),
                ('tipo_municion', models.CharField(max_length=20)),
                ('dpm', models.FloatField()),
                ('descripcion', models.TextField(default='')),
                ('naves_compatibles', models.ManyToManyField(blank=True, to='ecommerce.nave')),
            ],
        ),
    ]