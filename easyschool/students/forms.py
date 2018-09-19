from django import forms
from .models import StudentFee


class StudentFeeAdd(forms.ModelForm):
    """ The form class for fee submission """

    def clean(self):
        """Checks if the fee for this month has been submitted"""
        print("clean_month called")
        month = self.cleaned_data['month']
        year = self.cleaned_data['year']
        qs = StudentFee.objects.filter(month__iexact=month, year__iexact=year)
        if qs is not None:
            raise forms.ValidationError("Fee for {} has been submitted".format(month))
        return self.cleaned_data

    class Meta:
        model = StudentFee
        fields = (
            'student',
            'month',
            'year',
            'amount',
        )