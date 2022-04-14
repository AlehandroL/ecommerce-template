from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import FormView

from stock.models import Stock
from stock.forms import ContactForm


def stock_list(request):
    stock = Stock.objects.all()
    return render(request, 'stock/home.html', {'stock': stock})

def stock_detail(request, product):
    pass

class ContactFormView(FormView):
    template_name = 'stock/contact.html'
    form_class = ContactForm
    success_url = 'success'
    
    def form_valid(self, form):
        # This methos is called when valid form data has been POSTed
        # It should return an HttpResponse.
        form.send_email()
        return super().form_valid(form)

