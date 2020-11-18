from  django.forms import  ModelForm
from  django import forms
from  .models import Users,Pp, Shu, Prof, Uch

class UsersForm(ModelForm):
    name = forms.CharField(label="Фамилия И.О.", max_length=150)
    nomer = forms.IntegerField(label="Номер")
    prof = forms.ModelChoiceField(queryset= Prof.objects.all(),
                                   label="Проффесия")
    uch = forms.ModelChoiceField(queryset=Uch.objects.all(),
                                  label="Участок")

    shu = forms.ModelChoiceField(queryset= Shu.objects.all(),
                                 label='Шахто управление', help_text='Не забудьту задать шахтоуправление!',
                                 initial = 1, widget=forms.widgets.Select(attrs={'size': 1}))
    pp = forms.ModelChoiceField(queryset=Pp.objects.all(),
                                 label="Производственое подраздилени")

    name.widget.attrs.update({'class': 'form-control'})
    nomer.widget.attrs.update({'class': 'form-control'})
    prof.widget.attrs.update({'class': 'form-control'})
    shu.widget.attrs.update({'class': 'form-control'})
    pp.widget.attrs.update({'class': 'form-control'})
    uch.widget.attrs.update({'class': 'form-control'})
    
    def __init__(self, *args, **kwargs):
        super(UsersForm, self).__init__(*args, **kwargs)
        self.fields['pp'].queryset = Pp.objects.filter(shu_id=1)

    class Meta:
        model = Users
        fields = ('name', 'nomer', 'prof','shu', 'pp', 'uch')
