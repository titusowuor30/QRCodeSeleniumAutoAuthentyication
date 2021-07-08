from django import forms

class OtpForm(forms.Form):
      otp=forms.CharField(max_length=6,widget=forms.TextInput(
          attrs={
              'class':'form-control form-control-sm',
              'name':'otp','type':'password','placeholder':'Enter OTP Code','id':'otp'
      }
      ))