import datetime
import random
import string
import zoneinfo

from django.db import migrations


# Ensure all candidates create the same DB records to ensure parity
random.seed(0)  # DO NOT CHANGE!


given_names = [
    "Olivia", "Amelia", "Isla", "Ava", "Ivy", "Freya", "Lily",
    "Florence", "Mia", "Willow", "Rosie", "Sophia", "Isabella",
    "Grace", "Daisy", "Sienna", "Poppy", "Elsie", "Emily", "Ella",
    "Evelyn", "Phoebe", "Sofia", "Evie", "Charlotte", "Harper",
    "Millie", "Matilda", "Maya", "Sophie", "Alice", "Emilia",
    "Isabelle", "Ruby", "Luna", "Maisie", "Aria", "Penelope", "Mila",
    "Bonnie", "Eva", "Hallie", "Eliza", "Ada", "Violet", "Esme",
    "Arabella", "Imogen", "Jessica", "Delilah", "Lottie", "Chloe",
    "Thea", "Layla", "Eleanor", "Aurora", "Margot", "Mabel", "Erin",
    "Elizabeth", "Emma", "Scarlett", "Harriet", "Lola", "Nancy", "Orla",
    "Ayla", "Rose", "Zara", "Iris", "Robyn", "Bella", "Molly", "Olive",
    "Maria", "Lyla", "Maeve", "Ellie", "Gracie", "Lyra",
]
family_names = [
    "Smith", "Jones", "Taylor", "Brown", "Williams", "Wilson",
    "Johnson", "Davies", "Robinson", "Wright", "Thompson", "Evans",
    "Walker", "White", "Roberts", "Green", "Hall", "Wood", "Jackson",
    "Clark", "Satō", "Suzuki", "Takahashi", "Tanaka", "Watanabe",
    "Itō", "Nakamura", "Kobayashi", "Yamamoto", "Katō", "Yoshida",
    "Yamada", "Sasaki", "Yamaguchi", "Matsumoto", "Inoue", "Kimura",
    "Shimizu", "Hayashi", "Saitō",
]


def pick_datetime():
    date_of_no_importance = datetime.datetime(
        2024, 11, 3, 0, 0, 0,
        tzinfo=zoneinfo.ZoneInfo("Europe/London"),
    )
    jitter = datetime.timedelta(minutes=15 * random.randint(-1000, 10_000))

    return date_of_no_importance + jitter


postcode_templates = [
    "AA9A 9AA", "A9A 9AA", "A9 9AA", "A99 9AA", "AA9 9AA", "AA99 9AA",
]


def pick_postcode():
    template = random.choice(postcode_templates)

    out = []
    for char in template:
        if char == "A":
            out.append(random.choice(string.ascii_uppercase))
        elif char == "9":
            out.append(random.choice(string.digits))
        else:
            out.append(char)

    return "".join(out)


def populate_data(apps, schema_editor):
    Instruction = apps.get_model("forensic.Instruction")
    Collection = apps.get_model("forensic.Collection")
    Sample = apps.get_model("forensic.Sample")

    for _ in range(1000):
        ins = Instruction.objects.create(client_name=(
            f"{random.choice(given_names)} {random.choice(family_names)}"
        ))

        for _ in range(random.randint(3, 20)):
            coll = Collection.objects.create(
                instruction=ins,
                when=pick_datetime(),
                postcode=pick_postcode(),
            )

            for _ in range(random.randint(6, 10)):
                Sample.objects.create(
                    collection=coll,
                    sample_type=random.choice(["hair", "blood"]),
                )


def delete_all_data(apps, schema_editor):
    Instruction = apps.get_model("forensic.Instruction")

    Instruction.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('forensic', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_data, delete_all_data),
    ]
