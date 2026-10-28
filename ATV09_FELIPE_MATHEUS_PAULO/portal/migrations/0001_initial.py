from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name="Conteudo",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("titulo", models.CharField(max_length=120, verbose_name="título")),
                ("slug", models.SlugField(max_length=140, unique=True, verbose_name="slug")),
                ("html", models.TextField(help_text="Informe apenas o HTML interno da página, sem html, head, body, header, nav ou footer.", verbose_name="conteúdo HTML")),
                ("ativo", models.BooleanField(default=True, verbose_name="ativo")),
            ],
            options={"verbose_name": "conteúdo", "verbose_name_plural": "conteúdos", "ordering": ["titulo"]},
        ),
        migrations.CreateModel(
            name="Menu",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("titulo", models.CharField(max_length=120, verbose_name="título")),
                ("tipo_destino", models.CharField(choices=[("interno", "Conteúdo interno"), ("externo", "Link externo")], max_length=10, verbose_name="tipo de destino")),
                ("ordem", models.PositiveIntegerField(default=0, verbose_name="ordem")),
                ("ativo", models.BooleanField(default=True, verbose_name="ativo")),
                ("url_externa", models.URLField(blank=True, verbose_name="URL externa")),
                ("conteudo", models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name="itens_menu", to="portal.conteudo", verbose_name="conteúdo relacionado")),
            ],
            options={"verbose_name": "item do menu", "verbose_name_plural": "itens do menu", "ordering": ["ordem", "id"]},
        ),
    ]
