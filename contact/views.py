from typing import Any
from django import forms
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.http import Http404, HttpResponse
from contact.models import Contact
from django.contrib import messages, auth
from contact.forms import contactForm, RegisterForm, loginUser, registerUpdateForm
from django.db.models import Q
from django.core.paginator import Paginator
from django.core.exceptions import ValidationError

#Application DEFAULT page#
def index(request):
    contacts = Contact.objects.filter(show=True).order_by('id')

    paginator = Paginator(contacts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj' : page_obj,
        'title_page': 'Contacts',
    }
    return render(
        request,
        'contact/pages/index.html',
        context,
                )

#DETAIL page of the app's contacts#
def contact(request, id):
    oneContact = get_object_or_404(Contact, pk=id, show=True)

    name_contact = f'{oneContact.name}'

    context = {
        'contact' : oneContact,
        'title_page': name_contact,
    }
    return render(
        request,
        'contact/pages/contact.html',
        context,
                )

#App contact SEARCH filter#
def search(request):
    search_value = request.GET.get('q', '').strip()
    contacts = Contact.objects.filter(show=True).filter(Q(name__icontains=search_value) | Q(email__icontains=search_value) ).order_by('id')

    paginator = Paginator(contacts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if search_value == '':
        return redirect('index')
    

    context = {
        'page_obj' : page_obj,
        'title_page': 'search ',
    }
    return render(
        request,
        'contact/pages/index.html',
        context,
                )

#Contact Creation Crud#
def create(request):
    form_action = reverse('create')
    if request.method == 'POST':
        form = contactForm(request.POST, request.FILES)
        context = {
            'form': form,
            'form_action': form_action,
        }

        if form.is_valid():
            contato = form.save()
            messages.success(request, "Contato criando com sucesso!")
            return redirect('update', id=contato.pk)

        return render(
            request,
            'contact/pages/create.html',
            context
        )

    context = {
        'form': contactForm(),
        'form_action': form_action,
    }

    return render(
            request,
            'contact/pages/create.html',
            context
        )

#Contact update CRUD#
def update(request, id):
    contact = get_object_or_404(Contact, pk=id, show=True)
    form_action = reverse('update', args=(id,))
    if request.method == 'POST':
        form = contactForm(request.POST, request.FILES, instance=contact)
        context = {
            'form': form,
            'form_action': form_action,
        }

        if form.is_valid():
            contato = form.save()
            messages.info(request, "Contato editado com sucesso!")
            return redirect('update', id=contato.pk)

        return render(
            request,
            'contact/pages/create.html',
            context
        )

    context = {
        'form': contactForm(instance=contact),
        'form_action': form_action,
    }

    return render(
            request,
            'contact/pages/create.html',
            context
        )

#CRUD of deleting contact#
def delete(request, id):
    contact = get_object_or_404(Contact, pk=id, show=True)
    confirmation = request.POST.get('confirmation', 'no')
    confirmation_del = request.POST.get('confirmation_del')
    messages.info(request, "Deseja realmente deleta o contato?")
    if confirmation_del == 'del':
        contact.delete()
        messages.success(request, 'Contato deletado com sucesso!')
        return redirect('index')
    
    if confirmation_del == 'cancel':
        return redirect ('contact', id=contact.pk)

    
    return render(request, 'contact/pages/contact.html',{
        'contact': contact,
        'confirmation': confirmation,
    })

#application user registration#
def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request,'Usuário registrado com sucesso!')
            return redirect('login')
    return render(request, 'contact/pages/register.html', {
        'form': form,
        'text': 'Create User',
    })

#application user login#
def login(request):
    form = loginUser(request)
    if request.method == 'POST':
        form = loginUser(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.success(request,'Logado com sucesso!')
        else:
            messages.error(request, 'Login inválido.')

    return render(request, 'contact/pages/login.html', {
        'form': form
    })

#application user logout#
def logoff(request):
    auth.logout(request)
    messages.info(request, "Logout feito com sucesso!")
    return redirect('login')

##
def updateuser(request):
    form = registerUpdateForm(instance=request.user)
    if request.method == 'POST':
        form = registerUpdateForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
    return render(request, 'contact/pages/register.html', {'form': form, 'text': 'Update User',})

#show logged in user's contacts#
def users(request):
    ...