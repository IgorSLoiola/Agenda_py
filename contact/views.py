from django.shortcuts import get_object_or_404, render
from django.http import Http404
from contact.models import Contact
# from contact import models


# Create your views here.
def index(request):
    # contacts = models.Contact.objects.all().order_by('id')
    contacts = Contact.objects.filter(show=True).order_by('id')[0:10]

    # print(contacts.query)

    context = {
        'contacts' : contacts,
    }
    return render(
        request,
        'contact/pages/index.html',
        context,
                )
def contact(request, id):
    #oneContact = Contact.objects.filter(pk=id).first()
    #oneContact = get_object_or_404(Contact.objects.filter(pk=id))
    oneContact = get_object_or_404(Contact, pk=id, show=True)

    # if oneContact is None:
    #     raise Http404()

    # print(contacts.query)

    context = {
        'contact' : oneContact,
    }
    return render(
        request,
        'contact/pages/contact.html',
        context,
                )