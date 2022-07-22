from django.forms import ModelForm
from .models import QarzModel


class QarzForm(ModelForm):
    class Meta:
        model=QarzModel
        fields='__all__'
        labels={
            'condition':'Holat',
            'name':'Shaxs (Ism*)',
            'amount':'Qarz miqdori',
            'date':'Berilgan sana',
            'currency':'Pul birligi',
        }
        ordering=['-date']
    def __init__(self, *args, **kwargs):
        super(QarzForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
        