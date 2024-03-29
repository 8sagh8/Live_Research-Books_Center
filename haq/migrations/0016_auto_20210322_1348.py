# Generated by Django 3.1.4 on 2021-03-22 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('haq', '0015_auto_20210322_1341'),
    ]

    operations = [
        migrations.CreateModel(
            name='Authorized_Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auth_name', models.CharField(max_length=10)),
                ('data_status', models.CharField(default='P', max_length=1)),
                ('data_user', models.CharField(default='Admin', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('data_status', models.CharField(default='P', max_length=1)),
                ('data_user', models.CharField(default='Admin', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_category', models.CharField(max_length=22)),
                ('data_status', models.CharField(default='P', max_length=1)),
                ('data_user', models.CharField(default='Admin', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_language', models.CharField(max_length=7)),
                ('data_status', models.CharField(default='P', max_length=1)),
                ('data_user', models.CharField(default='Admin', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Need',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_need', models.CharField(max_length=9)),
                ('data_status', models.CharField(default='P', max_length=1)),
                ('data_user', models.CharField(default='Admin', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_p_name', models.CharField(max_length=40)),
                ('_birth_year', models.CharField(max_length=4)),
                ('_death_year', models.CharField(max_length=4)),
                ('data_status', models.CharField(default='P', max_length=1)),
                ('data_user', models.CharField(default='Admin', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Religion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_sect', models.CharField(max_length=20)),
                ('data_status', models.CharField(default='P', max_length=1)),
                ('data_user', models.CharField(default='Admin', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_status', models.CharField(max_length=16)),
                ('data_status', models.CharField(default='P', max_length=1)),
                ('data_user', models.CharField(default='Admin', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_topic', models.CharField(max_length=50)),
                ('data_status', models.CharField(default='P', max_length=1)),
                ('data_user', models.CharField(default='Admin', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vol_para', models.IntegerField()),
                ('page_chapter', models.IntegerField()),
                ('hadees_verse', models.IntegerField()),
                ('description', models.TextField(max_length=500, null=True)),
                ('data_status', models.CharField(default='P', max_length=1)),
                ('data_user', models.CharField(default='Admin', max_length=10)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='haq.book')),
                ('personFor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='personFor', to='haq.person')),
                ('speaker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='speaker', to='haq.person')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='haq.topic')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='haq.person'),
        ),
        migrations.AddField(
            model_name='book',
            name='cat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='haq.category'),
        ),
        migrations.AddField(
            model_name='book',
            name='lang',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='haq.language'),
        ),
        migrations.AddField(
            model_name='book',
            name='need',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='haq.need'),
        ),
        migrations.AddField(
            model_name='book',
            name='sect',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='haq.religion'),
        ),
        migrations.AddField(
            model_name='book',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='haq.status'),
        ),
    ]
