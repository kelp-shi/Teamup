from typing import Any, Optional
from django.db import models
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import PostProject, workTag, CustomUser
from .forms import WorkTagForm

# Create your views here.

class index(LoginRequiredMixin, ListView):
    model = PostProject
    model = CustomUser
    template_name = 'common/index.html'

    def get_queryset(self):
        return PostProject.objects.exclude()

class ProjectList(ListView):
    model = PostProject
    template_name = 'common/projectlist.html'
    paginate_by = 20

    def get_queryset(self):
        return PostProject.objects.exclude()
    
    def get_user(self, request, **kwargs):
        ctx = {
            'user': self.request.user
        }

        return self.render_to_response(ctx)

# post project ---------------------------------

class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = PostProject
    template_name = 'common/project.html'
    fields = ['PPtitle', 'PPcontext']
    success_url = reverse_lazy('teamupweb:index')

    def form_valid(self, form):
        form.instance.PPuser = self.request.user
        return super().form_valid(form)

def ProjectDetail(request, pk):
    detail = get_object_or_404(PostProject, pk=pk)
    return render(request, 'common/detail.html', {'detail': detail})

# detail peoject --------------------------------未実装
#class base view
class ProjectDetails(DetailView):
    template_name = 'common/detail.html'
    model = PostProject
    usermodel = CustomUser
    queryset = PostProject.objects.all()
    user_query = CustomUser.objects.all()
    
#function base view
class ProjectDelete(LoginRequiredMixin, DeleteView):
    model = PostProject
    template_name = 'common/delete.html'
    success_url = reverse_lazy('teamupweb:index')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, '削除しました')
        return super().delete(request, *args, **kwargs)

# test render ------------------------------
def test(request):
    form = WorkTagForm(request.POST or None)
    if form.is_valid():
        tag = workTag()
        tag.name = form.cleaned_data['name']

        workTag.objects.create(
            name = tag.name,
        )
    return render(request, 'common/test.html', {'form': form})

# profile ----------------------------------
class ProfileView(DetailView):
    template_name = 'common/profile.html'
    model = CustomUser
    slug_field = 'username'
    slug_url_kwarg = 'username'
    queryset = CustomUser.objects.all()
    context_object_name = 'profile'

# help -------------------------------------
def Help(request):
    return render(request, 'common/help.html')



