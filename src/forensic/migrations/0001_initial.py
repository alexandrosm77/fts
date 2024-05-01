from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instruction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('when', models.DateTimeField()),
                ('postcode', models.CharField(max_length=8)),
                ('instruction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forensic.instruction')),
            ],
        ),
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sample_type', models.CharField(choices=[('hair', 'Hair'), ('blood', 'Blood')], max_length=5)),
                ('collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forensic.collection')),
            ],
        ),
    ]
