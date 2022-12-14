from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import TemplateView
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.hashers import make_password
from datetime import datetime

from .models import AppUser
from .forms import CollectInfoForm
from .matching_files import collect_users_data

AppUser = get_user_model()


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'users/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['app_users'] = AppUser.objects.filter(is_staff=False)
        return context


class CollectInfoView(LoginRequiredMixin, View):
    form_class = CollectInfoForm
    template_name = 'users/upload_files.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            uploaded_csv_file = form.cleaned_data['csv_file']
            uploaded_xml_file = form.cleaned_data['xml_file']
            if (not uploaded_csv_file.name.endswith('.csv')) or (not uploaded_xml_file.name.endswith('.xml')):
                messages.error(request, 'One of the files is wrong type!')
                return render(request, self.template_name, {'form': form})
            else:
                fs = FileSystemStorage()
                csv_file = fs.save(uploaded_csv_file.name, uploaded_csv_file)
                xml_file = fs.save(uploaded_xml_file.name, uploaded_xml_file)
                users_data = collect_users_data(uploaded_csv_file.name, uploaded_xml_file.name)
                load_users_to_db(users_data)
            messages.success(request, "Users info collected!")
            return redirect(reverse('home'))
        messages.info(request, form.errors)
        return render(request, self.template_name, {'form': form})


def load_users_to_db(users_data):
    obj = [AppUser(username=user['username'],
                   password=make_password(user['password']),
                   date_joined=(
                       datetime.fromtimestamp(int(user['date_joined'])) if user['date_joined'] != '' else None),
                   first_name=user['first_name'],
                   last_name=user['last_name'],
                   avatar=user['avatar'])
           for user in users_data
           ]
    AppUser.objects.bulk_create(obj)
