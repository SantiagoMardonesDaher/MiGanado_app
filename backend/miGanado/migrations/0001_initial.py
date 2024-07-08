# Generated by Django 5.0.6 on 2024-07-08 18:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numeroCaravana', models.CharField(max_length=100)),
                ('raza', models.CharField(max_length=100)),
                ('peso', models.FloatField(blank=True, null=True)),
                ('fechaNacimiento', models.DateField(blank=True, null=True)),
                ('fechaFallecimiento', models.DateField(blank=True, null=True)),
                ('preniada', models.BooleanField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sangrado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_lote', models.IntegerField()),
                ('numero_animal', models.IntegerField()),
                ('numero_tubo', models.IntegerField()),
                ('fecha', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Tratamiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('medicacion', models.CharField(max_length=100)),
                ('fecha_inicio', models.DateField()),
                ('duracion', models.IntegerField()),
                ('repeticion', models.IntegerField()),
                ('tipo', models.CharField(choices=[('tratamiento', 'Tratamiento'), ('vacunacion', 'Vacunación')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('nombre_campo', models.CharField(max_length=100)),
                ('correo_electronico', models.EmailField(max_length=254)),
                ('contrasenia', models.CharField(max_length=100)),
                ('tipo', models.CharField(choices=[('cliente', 'Cliente'), ('admin', 'Administrador')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Lote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('capacidad', models.IntegerField()),
                ('capacidad_max', models.IntegerField()),
                ('tipo_animal', models.CharField(choices=[('toro', 'Toro'), ('vaca', 'Vaca')], default='toro', max_length=20)),
                ('animales', models.ManyToManyField(blank=True, default=1, related_name='lotes_asociados', to='miGanado.animal')),
                ('usuario', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='lotes', to='miGanado.usuario')),
            ],
        ),
        migrations.AddField(
            model_name='animal',
            name='lote',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='animales_asociados', to='miGanado.lote'),
        ),
        migrations.AddField(
            model_name='animal',
            name='sangrado',
            field=models.ManyToManyField(to='miGanado.sangrado'),
        ),
        migrations.AddField(
            model_name='animal',
            name='tratamientos',
            field=models.ManyToManyField(to='miGanado.tratamiento'),
        ),
        migrations.CreateModel(
            name='Notificacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('lote', 'Lote'), ('tratamiento', 'Tratamiento'), ('tacto', 'Tacto'), ('sangrado', 'Sangrado'), ('estadísticas', 'Estadísticas')], max_length=20)),
                ('mensaje', models.CharField(max_length=255)),
                ('fecha', models.DateTimeField()),
                ('usuario', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='notificaciones', to='miGanado.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='ConfigNotificaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recibir_notificaciones_lote', models.BooleanField(default=False)),
                ('recibir_notificaciones_tratamiento', models.BooleanField(default=False)),
                ('recibir_notificaciones_tacto', models.BooleanField(default=False)),
                ('recibir_notificaciones_sangrado', models.BooleanField(default=False)),
                ('recibir_notificaciones_estadisticas', models.BooleanField(default=False)),
                ('usuario', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='config_notificaciones', to='miGanado.usuario')),
            ],
        ),
    ]