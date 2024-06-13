from django.db import models
from django.urls import reverse


class Instruction(models.Model):
    client_name = models.CharField(max_length=255)
    instruction_group = models.ForeignKey('InstructionGroup', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"instruction for {self.client_name}"

    def get_absolute_url(self):
        return reverse("forensic:instruction_detail", kwargs={"pk": self.pk})

    def hair_sample_count(self):
        count = 0
        for collection in self.collections.all():
            count += collection.samples.hair().count()

        return count

    def get_absolute_group_url(self):
        if self.instruction_group:
            return reverse("forensic:instruction_group_detail", kwargs={"pk": self.instruction_group.pk})


class InstructionGroup(models.Model):
    name = models.TextField(null=False, blank=False)

    def get_absolute_url(self):
        return reverse("forensic:instruction_group_detail", kwargs={"pk": self.pk})

    @property
    def instruction_count(self):
        return self.instruction_set.count()


class Collection(models.Model):
    instruction = models.ForeignKey(
        "forensic.Instruction",
        on_delete=models.CASCADE,
        related_name="collections",
    )

    when = models.DateTimeField()
    postcode = models.CharField(max_length=8)

    def __str__(self):
        return f"collection at {self.postcode}"

    def get_absolute_url(self):
        return reverse("forensic:collection_detail", kwargs={"pk": self.pk})


class SampleQuerySet(models.QuerySet):
    def hair(self):
        return self.filter(sample_type=Sample.SampleType.HAIR)


class Sample(models.Model):
    collection = models.ForeignKey(
        "forensic.Collection",
        on_delete=models.CASCADE,
        related_name="samples",
    )

    objects = SampleQuerySet.as_manager()

    class SampleType(models.TextChoices):
        HAIR = "hair", "Hair"
        BLOOD = "blood", "Blood"

    sample_type = models.CharField(max_length=5, choices=SampleType)

    def __str__(self):
        return f"{self.sample_type} sample"

    def get_absolute_url(self):
        return reverse("forensic:sample_detail", kwargs={"pk": self.pk})
