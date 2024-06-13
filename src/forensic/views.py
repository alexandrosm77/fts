from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Collection, Instruction, Sample, InstructionGroup


class InstructionList(ListView):
    model = Instruction


class InstructionDetail(DetailView):
    model = Instruction


class InstructionGroupList(ListView):
    model = InstructionGroup


class InstructionGroupDetail(DetailView):
    model = InstructionGroup


class CollectionDetail(DetailView):
    model = Collection


class SampleDetail(DetailView):
    model = Sample


def too_many_hair_samples(request):
    instructions = []
    for instruction in Instruction.objects.all():
        if instruction.hair_sample_count() > 70:
            instructions.append(instruction)

    return render(
        request,
        "forensic/instruction_list.html",
        {
            "object_list": instructions,
            "too_many_hair_samples_view": True,
        },
    )
