from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from bootstrap_datepicker_plus.widgets import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField
from .models import *


class RegisterTeacherForm(ModelForm, forms.Form):
	class Meta:
		model = Teacher
		fields = ['last_name', 'first_name', 'middle_name', 'employee_id_no']
		

	def __init__(self, *args, **kwargs):
		super(RegisterTeacherForm, self).__init__(*args, **kwargs)
		self.fields['last_name'].widget.attrs['class'] = 'form-control'
		self.fields['first_name'].widget.attrs['class'] = 'form-control'
		self.fields['middle_name'].widget.attrs['class'] = 'form-control'
		self.fields['employee_id_no'].widget.attrs['class'] = 'form-control'

class RegisterTeacherForm01(UserCreationForm):
	email = forms.EmailField(required=True)
	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")


	def __init__(self, *args, **kwargs):
		super(RegisterTeacherForm01, self).__init__(*args, **kwargs)
		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['email'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['maxlength'] = '13'
		self.fields['password2'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['maxlength'] = '13'

class RegisterStudentForm(ModelForm):
	class Meta:
		model = Student
		fields = ['last_name', 'first_name', 'middle_name', 'lrn', 'grade_level', 'section']
	def __init__(self, *args, **kwargs):
		super(RegisterStudentForm, self).__init__(*args, **kwargs)
		self.fields['last_name'].widget.attrs['class'] = 'form-control'
		self.fields['first_name'].widget.attrs['class'] = 'form-control'
		self.fields['middle_name'].widget.attrs['class'] = 'form-control'
		self.fields['lrn'].widget.attrs['class'] = 'form-control'
		self.fields['grade_level'].widget.attrs['class'] = 'form-control'
		self.fields['section'].widget.attrs['class'] = 'form-control'


class EconomyForm(forms.Form):
	teacher = forms.ModelChoiceField(queryset=Teacher.objects.all().order_by('last_name'))
	student = forms.ModelMultipleChoiceField(Student.objects.all().order_by('last_name'), required=False ,widget=forms.CheckboxSelectMultiple)

	def __init__(self, *args, **kwargs):
		super(EconomyForm, self).__init__(*args, **kwargs)
		self.fields['teacher'].widget.attrs['class'] = 'form-control'

class SchoolSettingsForm(ModelForm):
	class Meta:
		model = Teacher
		fields = ['school_name','school_logo']
	def __init__(self, *args, **kwargs):
		super(SchoolSettingsForm, self).__init__(*args, **kwargs)
		self.fields['school_name'].widget.attrs['class'] = 'form-control'
		self.fields['school_logo'].widget.attrs['class'] = 'form-control'

class CreateJobsForm(ModelForm):
	class Meta:
		model = Job
		fields = '__all__'
		exclude = ['teacher', 'date_created']
	
	def __init__(self, teacher, *args, **kwargs):
		super(CreateJobsForm, self).__init__(*args, **kwargs)
		self.fields['job'].widget.attrs['class'] = 'form-control'
		self.fields['suggested_per_class'].widget.attrs['class'] = 'form-control'
		self.fields['job_description'].widget.attrs['class'] = 'form-control'
		self.fields['salary'].widget.attrs['class'] = 'form-control'
		self.fields['student_assigned'] = forms.ModelChoiceField(queryset=StudentEconomy.objects.filter(teacher=teacher, status='Active'))
		self.fields['student_assigned'].widget.attrs['class'] = 'form-control'

class UpdateJobsForm(ModelForm):
	class Meta:
		model = Job
		fields = ['job', 'suggested_per_class', 'job_description', 'salary']

	def __init__(self, *args, **kwargs):
		super(UpdateJobsForm, self).__init__(*args, **kwargs)
		self.fields['job'].widget.attrs['class'] = 'form-control'
		self.fields['suggested_per_class'].widget.attrs['class'] = 'form-control'
		self.fields['job_description'].widget.attrs['class'] = 'form-control'
		self.fields['salary'].widget.attrs['class'] = 'form-control'

class CreateOpportunitiesForm(ModelForm):
	class Meta:
		model = Opportunitie
		fields = ['activity', 'amount']

	def __init__(self, *args, **kwargs):
		super(CreateOpportunitiesForm, self).__init__(*args, **kwargs)
		self.fields['activity'].widget.attrs['class'] = 'form-control'
		self.fields['amount'].widget.attrs['class'] = 'form-control'

class CreateHouseRulesForm(ModelForm):
	class Meta:
		model = HouseRule
		fields = ['rule', 'fine']

	def __init__(self, *args, **kwargs):
		super(CreateHouseRulesForm, self).__init__(*args, **kwargs)
		self.fields['rule'].widget.attrs['class'] = 'form-control'
		self.fields['fine'].widget.attrs['class'] = 'form-control'

from django.forms.widgets import NumberInput
class RentForm(forms.ModelForm):
	sdate = forms.DateTimeField(label="Date", required=True, widget=NumberInput(attrs={'type':'date'}))
	edate = forms.DateTimeField(label="Date", required=True, widget=NumberInput(attrs={'type':'date'}))
	class Meta:
		
		model = Rent
		fields = ['sdate', 'edate', 'posting', 'amount']

	def __init__(self, *args, **kwargs):
		super(RentForm, self).__init__(*args, **kwargs)
		self.fields['sdate'].widget.attrs['class'] = 'form-control'
		self.fields['edate'].widget.attrs['class'] = 'form-control'
		self.fields['posting'].widget.attrs['class'] = 'form-control'
		self.fields['amount'].widget.attrs['class'] = 'form-control'
