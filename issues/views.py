from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
)
from .models import Issue
from django.urls import reverse_lazy

# Create your views here.


class IssueBoardView(ListView):
    model = Issue
    template_name = 'issues/board.html'


class IssueDetailView(DetailView):
    model = Issue
    template_name = 'issues/detail.html'


class IssueCreateView(LoginRequiredMixin, CreateView):
    model = Issue
    template_name = 'issues/create.html'
    fields = ['summary', 'description', 'status', 'priority', 'reporter']

    def form_valid(self, form):
        form.instance.reporter = self.request.user
        return super().form_valid(form)


class IssueUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Issue
    template_name = 'issues/update.html'
    fields = ['summary', 'description', 'status', 'priority', 'reporter']

    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.reporter


class IssueDeleteView(DeleteView):
    model = Issue
    template_name = 'issues/delete.html'
    success_url = reverse_lazy("board")

    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.reporter
