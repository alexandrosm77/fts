from django.db import models
from django.urls import reverse


class Instruction(models.Model):
    client_name = models.CharField(max_length=255)

    def __str__(self):
        return f"instruction for {self.client_name}"

    def get_absolute_url(self):
        return reverse("forensic:instruction_detail", kwargs={"pk": self.pk})

    def hair_sample_count(self):
        count = 0
        for collection in self.collection_set.all():
            for sample in collection.sample_set.all():
                if sample.sample_type == sample.SampleType.HAIR:
                    count += 1

        return count


class Collection(models.Model):
    instruction = models.ForeignKey(
        "forensic.Instruction",
        on_delete=models.CASCADE,
    )

    when = models.DateTimeField()
    postcode = models.CharField(max_length=8)

    def __str__(self):
        return f"collection at {self.postcode}"

    def get_absolute_url(self):
        return reverse("forensic:collection_detail", kwargs={"pk": self.pk})


class Sample(models.Model):
    collection = models.ForeignKey(
        "forensic.Collection",
        on_delete=models.CASCADE,
    )

    class SampleType(models.TextChoices):
        HAIR = "hair", "Hair"
        BLOOD = "blood", "Blood"

    sample_type = models.CharField(max_length=5, choices=SampleType)

    def __str__(self):
        return f"{self.sample_type} sample"

    def get_absolute_url(self):
        return reverse("forensic:sample_detail", kwargs={"pk": self.pk})
