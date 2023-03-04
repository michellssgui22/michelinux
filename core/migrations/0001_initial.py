# Generated by Django 4.1.7 on 2023-02-26 17:56

from django.db import migrations, models
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BoasVindas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Criado')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Modificado')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('imagem', stdimage.models.StdImageField(force_min_size=False, upload_to='icons', variations={'thumb': {'height': 1000, 'width': 1000}}, verbose_name='Imagem')),
                ('mensagem', models.TextField(max_length=5000, verbose_name='Mensagem')),
            ],
            options={
                'verbose_name': 'Boas Vindas',
                'verbose_name_plural': 'Boas Vindas',
            },
        ),
        migrations.CreateModel(
            name='Certificado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Criado')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Modificado')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('imagem', stdimage.models.StdImageField(force_min_size=False, upload_to='icons', variations={'thumb': {'height': 100, 'width': 100}}, verbose_name='Imagem')),
                ('titulo', models.CharField(max_length=100, verbose_name='Título')),
                ('instituicao', models.CharField(max_length=200, verbose_name='Instituição')),
                ('conclusao', models.DateField(verbose_name='Conclusão')),
                ('linkvalida', models.URLField(verbose_name='Link Validação')),
                ('horas', models.IntegerField(verbose_name='Total Horas')),
            ],
            options={
                'verbose_name': 'Certificado',
                'verbose_name_plural': 'Certificados',
            },
        ),
        migrations.CreateModel(
            name='FormacaoAcademica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Criado')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Modificado')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('titulo', models.CharField(max_length=200, verbose_name='Titulo')),
                ('instituicao', models.CharField(max_length=100, verbose_name='Instituição')),
                ('conclusao', models.DateField(verbose_name='Conclusão')),
                ('descricao', models.TextField(max_length=5000, verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Formação Acadêmica',
                'verbose_name_plural': 'Formação Acadêmica',
            },
        ),
        migrations.CreateModel(
            name='HardSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Criado')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Modificado')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('icon', stdimage.models.StdImageField(force_min_size=False, upload_to='icons', variations={'thumb': {'height': 100, 'width': 100}}, verbose_name='Imagem')),
                ('titulo', models.CharField(max_length=100, verbose_name='Título')),
            ],
            options={
                'verbose_name': 'Hard Skill',
                'verbose_name_plural': 'Hard Skills',
            },
        ),
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Criado')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Modificado')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('imagem', stdimage.models.StdImageField(force_min_size=False, upload_to='icons', variations={'thumb': {'height': 225, 'width': 350}}, verbose_name='Imagem')),
                ('titulo', models.CharField(max_length=100, verbose_name='Título')),
                ('descricao', models.TextField(max_length=500, verbose_name='Descricao')),
                ('linksite', models.URLField(verbose_name='Link do Site')),
                ('linkgithub', models.URLField(verbose_name='Link GitHub')),
                ('horas', models.IntegerField(verbose_name='Total Horas')),
            ],
            options={
                'verbose_name': 'Projeto',
                'verbose_name_plural': 'Projetos',
            },
        ),
    ]