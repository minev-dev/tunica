import tunica
from tunica import migration


class Migration(migration.Migration):
    operations = [
        migration.CreateTable(
            name="my_table",
            columns=[
                tunica.String(name="id", primary_key=True, max_length=32),
                tunica.String(name="name", primary_key=False, max_length=128),
            ],
        )
    ]
