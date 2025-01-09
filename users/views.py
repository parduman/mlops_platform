# users/views.py
from django.shortcuts import render, redirect
from .models import InviteCode, CustomUser
from .forms import RegistrationForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            invite_code = form.cleaned_data['invite_code']
            try:
                code = InviteCode.objects.get(code=invite_code, is_active=True)
                user = form.save(commit=False)
                user.organization = code.organization
                user.save()
                code.is_active = False  # Invalidate the invite code after use
                code.save()
                return redirect('login')
            except InviteCode.DoesNotExist:
                form.add_error('invite_code', 'Invalid or inactive invite code.')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})
