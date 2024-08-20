from django.shortcuts import render, get_object_or_404, redirect
from .models import Quote
from .forms import QuoteForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Функція для відображення списку цитат
def quote_list(request):
    quotes = Quote.objects.all()
    return render(request, 'quotes/quote_list.html', {'quotes': quotes})

# Функція для відображення детальної інформації про цитату
def quote_detail(request, pk):
    quote = get_object_or_404(Quote, pk=pk)
    return render(request, 'quotes/quote_detail.html', {'quote': quote})

# Функція для створення нової цитати
def quote_new(request):
    if request.method == "POST":
        form = QuoteForm(request.POST)
        if form.is_valid():
            quote = form.save(commit=False)
            quote.save()
            return redirect('quotes:quote_detail', pk=quote.pk)
    else:
        form = QuoteForm()
    return render(request, 'quotes/quote_edit.html', {'form': form})

# Функція для редагування існуючої цитати
def quote_edit(request, pk):
    quote = get_object_or_404(Quote, pk=pk)
    if request.method == "POST":
        form = QuoteForm(request.POST, instance=quote)
        if form.is_valid():
            quote = form.save(commit=False)
            quote.save()
            return redirect('quotes:quote_detail', pk=quote.pk)
    else:
        form = QuoteForm(instance=quote)
    return render(request, 'quotes/quote_edit.html', {'form': form})

# Функція для видалення цитати
def quote_delete(request, pk):
    quote = get_object_or_404(Quote, pk=pk)
    quote.delete()
    return redirect('quotes:index')

# Функція для відображення цитат за тегом
def quotes_by_tag(request, tag):
    quotes = Quote.objects.filter(tags__name__in=[tag])
    return render(request, 'quotes/quote_list.html', {'quotes': quotes})

# Функція для реєстрації нового користувача
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('quotes:index')  # Redirect to the quotes list after registration
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
