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
from .models import Issue, Status
from django.urls import reverse_lazy

# Create your views here.


class IssueBoardView(ListView):
    model = Issue
    template_name = 'issues/board.html'

    def get_context_data(self, **kwargs):
        # get 3 lists of issues for the board: todo, in progress, done
        context = super().get_context_data(**kwargs)

        status_todo = Status.objects.get(id=1)
        status_in_progress = Status.objects.get(id=2)
        status_done = Status.objects.get(id=3)

        context['issues_todo'] = Issue.objects.filter(
            status=status_todo,
        ).order_by('created_at').order_by('priority').reverse()

        context['issues_in_progress'] = Issue.objects.filter(
            status=status_in_progress,
        ).order_by('created_at').order_by('priority').reverse()

        context['issues_done'] = Issue.objects.filter(
            status=status_done,
        ).order_by('created_at').order_by('priority').reverse()

        return context


class IssueDetailView(DetailView):
    model = Issue
    template_name = 'issues/detail.html'


class IssueCreateView(LoginRequiredMixin, CreateView):
    model = Issue
    template_name = 'issues/create.html'
    fields = ['summary', 'description', 'status', 'priority', 'assignee']

    def form_valid(self, form):
        form.instance.reporter = self.request.user
        return super().form_valid(form)


class IssueUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Issue
    template_name = 'issues/update.html'
    fields = ['summary', 'description', 'status', 'assignee']

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
