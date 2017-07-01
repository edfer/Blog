from django import forms
from django.forms.utils import ErrorList 

class FormUserNeededMixin(object):
    def form_valid(self, form):
        if self.request.user.is_authenticated():
            form.instance.user = self.request.user
            return super(FormUserNeededMixin, self).form_valid(form)
        else:
            form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(["You're not logged in"])
            return self.form_invalid(form)

class OwnerMixin(object):
    def form_valid(self, form):
        if form.instance.user == self.request.user:
            return super(OwnerMixin , self).form_valid(form)
        else:
            form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(["Not allwed, sorry."])
            return self.form_invalid(form)