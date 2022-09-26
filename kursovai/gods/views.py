from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import Gs
from .models import Rubric
from .forms import GgForm


class GgCreateView(CreateView):
    template_name = 'gods/create.html'
    form_class = GgForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context


def index(request):
    ggs = Gs.objects.all()
    rubrics = Rubric.objects.all()
    context = {'ggs': ggs, 'rubrics': rubrics}
    return render(request, 'gods/index.html', context)


def by_rubric(request, rubric_id):
    ggs = Gs.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {'ggs': ggs, 'rubrics': rubrics, 'current_rubric': current_rubric}
    return render(request, 'gods/by_rubric.html', context)
