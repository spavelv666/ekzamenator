from  django.forms import  ModelForm
from  django import forms
from  .models import Users,Pp, Shu, Prof, Uch
from django.contrib.auth.models import User

class UsersForm(ModelForm):

    name = forms.CharField(label="Ф.И.О.", max_length=150)
    nomer = forms.IntegerField(label="Таб.№")
    prof = forms.ModelChoiceField(queryset= Prof.objects.all(),
                                   label="Профессия")
    uch = forms.ModelChoiceField(queryset=Uch.objects.all(),
                                  label="Участок")

    shu = forms.ModelChoiceField(queryset= Shu.objects.all(),
                                 label='Шахто управление', help_text='Не забудьту задать шахтоуправление!',
                                 initial = 1, widget=forms.widgets.Select(attrs={'size': 1}))
    pp = forms.ModelChoiceField(queryset=Pp.objects.all(),
                                 label="Шахта")

    name.widget.attrs.update({'class': 'form-control'})
    nomer.widget.attrs.update({'class': 'form-control'})
    prof.widget.attrs.update({'class': 'form-control'})
    shu.widget.attrs.update({'class': 'form-control'})
    pp.widget.attrs.update({'class': 'form-control'})
    uch.widget.attrs.update({'class': 'form-control'})
    
    def __init__(self,  *args, **kwargs):
        user = kwargs.pop('user')
        super(UsersForm, self).__init__(*args, **kwargs)

        self.fields['pp'].queryset = Pp.objects.filter(user = user)
       #user = User.objects.get(id=1)
        ppp = Pp.objects.filter(user=user)

        self.fields['uch'].queryset = Uch.objects.filter(pp = ppp[0])
        #self.fields['shu'].queryset = Shu.objects.filter(pp=ppp[0])
    class Meta:
        model = Users
        fields = ('name', 'nomer', 'prof','shu', 'pp', 'uch')

class UpdateForm(forms.ModelForm):
    """ Форма добавления тикетов
    """
    name = forms.CharField(label="Ф.И.О.", max_length=150)
    nomer = forms.IntegerField(label="Таб.№")
    prof = forms.ModelChoiceField(queryset=Prof.objects.all(),
                                  label="Профессия")
    shu = forms.ModelChoiceField(queryset=Shu.objects.all(),
                                 label='Шахто управление', widget=forms.widgets.Select(
            attrs={'class': 'disabled', 'readonly': 'readonly'}))
    uch = forms.ModelChoiceField(queryset=Uch.objects.all(),
                                 label="Участок")
    name.widget.attrs.update({'class': 'form-control flex-fill'})
    nomer.widget.attrs.update({'class': 'form-control flex-fill'})
    prof.widget.attrs.update({'class': 'form-control flex-fill'})
    uch.widget.attrs.update({'class': 'form-control flex-fill'})


    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(UpdateForm, self).__init__(*args, **kwargs)
        self.fields['pp'].queryset = Pp.objects.filter(user=self.user)
    # user = User.objects.get(id=1)
        ppp = Pp.objects.filter(user=self.user)

        self.fields['uch'].queryset = Uch.objects.filter(pp=ppp[0])

    # self.fields['shu'].queryset = Shu.objects.filter(pp=ppp[0])
    class Meta:
        model = Users
        fields = ('name', 'nomer', 'prof', 'shu', 'pp', 'uch')


class UchForm(ModelForm):
    name = forms.CharField(label="Введите название участка", max_length=150)
    shu = forms.ModelChoiceField(queryset=Shu.objects.all(),
                                 label='Шахто управление', help_text='Не забудьту задать шахтоуправление!',
                                 initial=1, widget=forms.widgets.Select(attrs={'size': 1}))
    pp = forms.ModelChoiceField(queryset=Pp.objects.all(),
                                label="Шахта")
    name.widget.attrs.update({'class': 'form-control flex-fill'})
    class Meta:
        model = Uch
        fields = ('name', 'shu', 'pp',)

    #def __init__(self, *args, **kwargs):
    #    user = kwargs.pop('user')
   #     super(UchForm, self).__init__(*args, **kwargs)

       # self.fields['pp'].queryset = Pp.objects.filter(user=user)
        # user = User.objects.get(id=1)
        #ppp = Pp.objects.filter(user=user)

        #self.fields['uch'].queryset = Uch.objects.filter(pp=ppp[0])
        # self.fields['shu'].queryset = Shu.objects.filter(pp=ppp[0])