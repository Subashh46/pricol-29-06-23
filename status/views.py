from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Machine, Status
from django.urls import reverse_lazy

# Create your views here.


class HomePageView(ListView):
    model = Status
    template_name = 'home.html'


class MachinePageView(ListView):
    model = Machine
    template_name = 'machines.html'


class MachineDetailView(DetailView):
    model = Machine
    template_name = 'machine_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["status"] = Status.objects.all()
        return context


class NewStatusView(CreateView):
    model = Status
    template_name = "new.html"
    fields = ['machine', 'is_working', 'description', 'document', 'document_name']


class UpdateStatusView(UpdateView):
    model = Status
    template_name = "update.html"
    fields = ['machine', 'is_working', 'description', 'document', 'document_name']


class DeleteStatusView(DeleteView):
    model = Status
    template_name = 'delete_status.html'
    success_url = reverse_lazy("home")

class DocumentListView(ListView):
    model = Status
    template_name = 'documents_view.html'
