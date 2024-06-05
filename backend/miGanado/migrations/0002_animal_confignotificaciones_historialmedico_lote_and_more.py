# Generated by Django 5.0.6 on 2024-06-05 00:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miGanado', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numeroCaravana', models.CharField(max_length=100)),
                ('raza', models.CharField(max_length=100)),
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
            ],
        ),
        migrations.CreateModel(
            name='HistorialMedico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('peso', models.FloatField()),
                ('fechaNacimiento', models.DateField()),
                ('fechaFallecimiento', models.DateField(blank=True, null=True)),
                ('preniada', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Lote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('capacidad', models.IntegerField()),
                ('capacidadMax', models.IntegerField()),
                ('idTipoAnimal', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Notificacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IdTipo', models.CharField(choices=[('lote', 'Lote'), ('tratamiento', 'Tratamiento'), ('tacto', 'Tacto'), ('sangrado', 'Sangrado'), ('estadísticas', 'Estadísticas')], max_length=20)),
                ('mensaje', models.CharField(max_length=255)),
                ('fecha', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Sangrado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numeroLote', models.IntegerField()),
                ('numeroAnimal', models.IntegerField()),
                ('numeroTubo', models.IntegerField()),
                ('fecha', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Tratamiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numeroAnimal', models.IntegerField()),
                ('nombre', models.CharField(max_length=100)),
                ('medicacion', models.CharField(max_length=100)),
                ('fechaInicio', models.DateField()),
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
                ('nombreCampo', models.CharField(max_length=100)),
                ('correoElectronico', models.EmailField(max_length=254)),
                ('contrasenia', models.CharField(max_length=100)),
                ('idTipo', models.CharField(choices=[('cliente', 'Cliente'), ('admin', 'Administrador')], max_length=20)),
                ('configNotificaciones', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='miGanado.confignotificaciones')),
            ],
        ),
        migrations.DeleteModel(
            name='Ganado',
        ),
        migrations.AddField(
            model_name='animal',
            name='HistorialMedico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='miGanado.historialmedico'),
        ),
        migrations.AddField(
            model_name='lote',
            name='Animales',
            field=models.ManyToManyField(to='miGanado.animal'),
        ),
        migrations.AddField(
            model_name='historialmedico',
            name='sangrado',
            field=models.ManyToManyField(to='miGanado.sangrado'),
        ),
        migrations.AddField(
            model_name='historialmedico',
            name='tratamientos',
            field=models.ManyToManyField(to='miGanado.tratamiento'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='lotes',
            field=models.ManyToManyField(blank=True, to='miGanado.lote'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='notificaciones',
            field=models.ManyToManyField(blank=True, to='miGanado.notificacion'),
        ),
        migrations.AddField(
            model_name='confignotificaciones',
            name='usuario_config',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='miGanado.usuario'),
        ),
    ]
