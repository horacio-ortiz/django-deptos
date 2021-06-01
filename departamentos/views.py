from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import ListView, UpdateView
from django.http import HttpResponse

from departamentos.forms import DeptoForm, form_validation_error
from departamentos.models import Depto


class listaDeptoView(ListView):
    model = Depto
    template_name = 'depto_list.html'


def edit_Depto(request, depto_id):
    depto = get_object_or_404(Depto, pk=depto_id)

    if request.method == 'POST':
        modelform = DeptoForm(request.POST, request.FILES, instance=depto)
        if modelform.is_valid():
            modelform.save()
            messages.success(request, 'Departamento Actualizado con exito')
        else:
            messages.error(request, form_validation_error(modelform))
            modelform = DeptoForm(instance=depto)
        return redirect('listadepto')

    return render(request, 'departamentos/depto_update_form.html', {'form': DeptoForm, 'depto': depto})


@method_decorator(login_required(login_url='login'), name='dispatch')
class DeptoView(View):
    depto = None
    """
    def dispatch(self, request, *args, **kwargs):
        self.depto, __ = Depto.objects.get_or_create(user=request.user)
        return super(DeptoView, self).dispatch(request, *args, **kwargs)
    """

    def get(self, request):
        context = {'depto': self.depto, 'segment': 'depto'}
        return render(request, 'departamentos/deptos.html', context)

    def post(self, request):
        form = DeptoForm(request.POST, request.FILES, instance=self.depto)
        depto = form.save()
        depto.save()

        if form.is_valid():
            

            messages.success(request, 'Departamento grabado con exito')
        else:
            messages.error(request, form_validation_error(form))
        

        return redirect('listadepto')
