from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from .models import WorkModel, ServiceModel
from .forms import *


class IndexView(TemplateView):
    template_name = 'my_app/index.html'


class LoginView(LoginRequiredMixin, TemplateView):
    template_name = 'my_app/index.html'


def handle_not_found(request, exception=None):
    return render(request, 'my_app/404.html')


class SuccessView(TemplateView):
    template_name = 'my_app/success.html'


class SuccessAccountView(TemplateView):
    template_name = 'my_app/success_account.html'


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('my_app:success-account-page')
    template_name = 'my_app/signup.html'


class HouseView(TemplateView):
    template_name = 'my_app/house.html'


####################################################################################################
# Work
####################################################################################################
class WorkViewBase(ListView):
    def __init__(self, work_type, template_name):
        self.template_name = template_name
        self.work_type = work_type
        self.model = WorkModel
        self.context_object_name = 'jobs'
        self.paginate_by = 10
        self.ordering = ['-id']

        if self.work_type == 0:
            self.queryset = WorkModel.objects.all()
        else:
            self.queryset = WorkModel.objects.filter(type_job=self.work_type)


class WorkItemView(DetailView):
    template_name = 'my_app/work/work_item.html'
    model = WorkModel
    context_object_name = 'job'


class WorkView(WorkViewBase):
    def __init__(self):
        super().__init__(work_type=0, template_name='my_app/work/work.html')


class WorkConstructionView(WorkViewBase):
    def __init__(self):
        super().__init__(work_type=1, template_name='my_app/work/work_construction.html')


class WorkCleaningView(WorkViewBase):
    def __init__(self):
        super().__init__(work_type=2, template_name='my_app/work/work_cleaning.html')


class WorkOtherView(WorkViewBase):
    def __init__(self):
        super().__init__(work_type=3, template_name='my_app/work/work_others.html')


class WorkFormTemplate(LoginRequiredMixin, CreateView):
    success_url = reverse_lazy('my_app:success-page')
    template_name = 'my_app/work/work_form.html'
    model = WorkModel
    def __init__(self, form_class):
        self.form_class = form_class
        

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class WorkConstructionCreateView(WorkFormTemplate):
    def __init__(self):
        super().__init__(form_class=WorkConstructionForm)


class WorkCleaningCreateView(WorkFormTemplate):
    def __init__(self):
        super().__init__(form_class=WorkCleaningForm)


class WorkOtherCreateView(WorkFormTemplate):
    def __init__(self):
        super().__init__(form_class=WorkOtherForm)


class WorkUpdateView(LoginRequiredMixin, UpdateView):
    model = WorkModel
    form_class = WorkOtherForm
    success_url = reverse_lazy('my_app:success-page')
    template_name = 'my_app/work/work_form.html'


class WorkDeleteView(LoginRequiredMixin, DeleteView):
    model = WorkModel
    success_url = reverse_lazy('my_app:work-page')
    template_name = 'my_app/delete_post.html'

    def get_queryset(self):
        # Restrict the queryset to only include objects belonging to the logged-in user
        queryset = super().get_queryset()
        return queryset.filter(author=self.request.user)

    def delete(self, request, *args, **kwargs):
        # Override the delete method to set the author_id field to the logged-in user's ID
        self.object = self.get_object()
        self.object.author_id = request.user.id
        return super().delete(request, *args, **kwargs)
####################################################################################################


####################################################################################################
# Service
####################################################################################################
class ServiceViewBase(ListView):
    def __init__(self, service_type):
        self.template_name = 'my_app/service/service.html'
        self.service_type = service_type
        self.model = ServiceModel
        self.context_object_name = 'services'
        self.paginate_by = 10
        self.ordering = ['-id']

        if self.service_type == 0:
            self.queryset = ServiceModel.objects.all()
        else:
            self.queryset = ServiceModel.objects.filter(service_type=self.service_type)


class ServiceItemView(DetailView):
    template_name = 'my_app/service/service_item.html'
    model = ServiceModel
    context_object_name = 'service'


class ServiceView(ServiceViewBase):
    def __init__(self):
        super().__init__(service_type=0)


class ServiceDomesticView(ServiceViewBase):
    def __init__(self):
        super().__init__(service_type=1)


class ServiceHealthyBeautyView(ServiceViewBase):
    def __init__(self):
        super().__init__(service_type=2)


class ServiceTransportView(ServiceViewBase):
    def __init__(self):
        super().__init__(service_type=3)


class ServiceFoodView(ServiceViewBase):
    def __init__(self):
        super().__init__(service_type=4)


class ServiceClassView(ServiceViewBase):
    def __init__(self):
        super().__init__(service_type=5)


class ServiceTravelView(ServiceViewBase):
    def __init__(self):
        super().__init__(service_type=6)


class ServiceTechnicView(ServiceViewBase):
    def __init__(self):
        super().__init__(service_type=7)


class ServiceOtherView(ServiceViewBase):
    def __init__(self):
        super().__init__(service_type=20)


class ServiceFormView(LoginRequiredMixin, CreateView):
    model = ServiceModel
    template_name = 'my_app/service/service_form.html'
    form_class = ServiceForm
    success_url = reverse_lazy('my_app:success-page')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ServiceUpdateView(LoginRequiredMixin, UpdateView):
    model = ServiceModel
    form_class = ServiceForm
    success_url = reverse_lazy('my_app:success-page')
    template_name = 'my_app/service/service_form.html'


class ServiceDeleteView(LoginRequiredMixin, DeleteView):
    model = ServiceModel
    success_url = reverse_lazy('my_app:service-page')
    template_name = 'my_app/delete_post.html'

    def get_queryset(self):
        # Restrict the queryset to only include objects belonging to the logged-in user
        queryset = super().get_queryset()
        return queryset.filter(author=self.request.user)

    def delete(self, request, *args, **kwargs):
        # Override the delete method to set the author_id field to the logged-in user's ID
        self.object = self.get_object()
        self.object.author_id = request.user.id
        return super().delete(request, *args, **kwargs)
####################################################################################################