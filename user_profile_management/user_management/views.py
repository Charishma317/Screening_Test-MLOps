# from django.shortcuts import render

# Create your views here.
# views.py
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import UserProfile, Interest

class UserListView(ListView):
    model = UserProfile
    template_name = 'user_list.html'
    context_object_name = 'users'

class UserDetailView(DetailView):
    model = UserProfile
    template_name = 'user_detail.html'
    context_object_name = 'user'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        # Generate 'about' section based on interests using NLP (you need to implement this)
        obj.about = generate_about_text(obj.interests.all())
        return obj

# views.py (contd.)
from django.http import JsonResponse

def generate_about_text(interests):
    # Use OpenAI API or other NLP techniques to generate 'about' text
    # This is a placeholder, replace it with actual implementation
    about_text = " ".join([interest.name for interest in interests])
    return about_text

def delete_user(request, pk):
    user = get_object_or_404(UserProfile, pk=pk)
    user.delete()
    return JsonResponse({'message': 'User deleted successfully'})
