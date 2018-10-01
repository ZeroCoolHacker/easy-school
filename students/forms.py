from calendar import month_name

from django import forms

from .models import StudentFee


class StudentFeeAdd(forms.ModelForm):
    """ The form class for fee submission """

    def clean(self):
        """Checks if the fee for this month has been submitted"""
        month = self.cleaned_data['date'].month
        year = self.cleaned_data['date'].year
        qs = StudentFee.objects.filter(
            month__iexact=month,
            year__iexact=year,
            student=self.cleaned_data['student'])

        if len(qs) is not 0:
            raise forms.ValidationError("Fee for {} has been submitted".
                                        format(month_name[int(month)]))
        return self.cleaned_data

    class Meta:
        model = StudentFee
        fields = (
            'student',
            'date',
            'amount',
        )
