from calendar import month_name

from django import forms

from .models import StudentFee


class StudentFeeAdd(forms.ModelForm):
    """ The form class for fee submission """

    def clean(self):
        """Checks if the fee for this month has been submitted"""
        student = self.cleaned_data['student']
        fee_group=self.cleaned_data['fee_group']
        valid_until=self.cleaned_data['valid_until']
        qs = StudentFee.objects.filter(
            student__iexact=student,
            fee_group__iexact=fee_group,
            valid_until = valid_until,
            )

        if len(qs) is not 0:
            raise forms.ValidationError("Fee for this month has been submitted.")
        return self.cleaned_data

    class Meta:
        model = StudentFee
        fields = (
            'student',
            'fee_group',
            'valid_until',
        )
