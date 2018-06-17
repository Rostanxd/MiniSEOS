# Generated by Django 2.0.5 on 2018-06-10 17:04

from django.db import migrations, models


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        ('inventario', '0007_auto_20180608_1424'),
    ]

    operations = [
        migrations.RenameField(
            model_name='grupo',
            old_name='fechaCreacion',
            new_name='dtm_fecha_creacion',
        ),
        migrations.RenameField(
            model_name='grupo',
            old_name='fechaModificacion',
            new_name='dtm_fecha_modificacion',
        ),
        migrations.RenameField(
            model_name='grupo',
            old_name='id',
            new_name='int_id',
        ),
        migrations.RenameField(
            model_name='grupo',
            old_name='estado',
            new_name='str_estado',
        ),
        migrations.RenameField(
            model_name='grupo',
            old_name='nombre',
            new_name='str_nombre',
        ),
        migrations.RenameField(
            model_name='grupo',
            old_name='usuarioCreacion',
            new_name='str_usuario_creacion',
        ),
        migrations.RenameField(
            model_name='grupo',
            old_name='usuarioModificacion',
            new_name='str_usuario_modificacion',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='fechaCreacion',
            new_name='dtm_fecha_creacion',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='fechaModificacion',
            new_name='dtm_fecha_modificacion',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='id',
            new_name='int_id',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='grupo',
            new_name='mod_grupo',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='marca',
            new_name='mod_marca',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='codigo',
            new_name='str_codigo',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='estado',
            new_name='str_estado',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='nombre',
            new_name='str_nombre',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='usuarioCreacion',
            new_name='str_usuario_creacion',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='usuarioModificacion',
            new_name='str_usuario_modificacion',
        ),
        migrations.RenameField(
            model_name='itemprecios',
            old_name='precio',
            new_name='dec_precio',
        ),
        migrations.RenameField(
            model_name='itemprecios',
            old_name='fecVigencia',
            new_name='dtm_fecha_vigencia',
        ),
        migrations.RenameField(
            model_name='itemprecios',
            old_name='item',
            new_name='mod_item',
        ),
        migrations.RenameField(
            model_name='marca',
            old_name='fechaCreacion',
            new_name='dtm_fecha_creacion',
        ),
        migrations.RenameField(
            model_name='marca',
            old_name='fechaModificacion',
            new_name='dtm_fecha_modificacion',
        ),
        migrations.RenameField(
            model_name='marca',
            old_name='id',
            new_name='int_id',
        ),
        migrations.RenameField(
            model_name='marca',
            old_name='estado',
            new_name='str_estado',
        ),
        migrations.RenameField(
            model_name='marca',
            old_name='nombre',
            new_name='str_nombre',
        ),
        migrations.RenameField(
            model_name='marca',
            old_name='usuarioCreacion',
            new_name='str_usuario_creacion',
        ),
        migrations.RenameField(
            model_name='marca',
            old_name='usuarioModificacion',
            new_name='str_usuario_modificacion',
        ),
        migrations.AddField(
            model_name='itemprecios',
            name='dtm_fecha_creacion',
            field=models.DateTimeField(auto_now=True, db_column='itmPreFecCreacion'),
        ),
        migrations.AddField(
            model_name='itemprecios',
            name='str_usuario_creacion',
            field=models.CharField(db_column='itmPreUsrCreacion', default='', max_length=10),
        ),
        migrations.RemoveField(
            model_name='itemprecios',
            name='fechaCreacion',
        ),
        migrations.RemoveField(
            model_name='itemprecios',
            name='usuarioCreacion',
        ),
        migrations.AlterUniqueTogether(
            name='itemprecios',
            unique_together={('mod_item', 'dtm_fecha_vigencia')},
        ),
    ]