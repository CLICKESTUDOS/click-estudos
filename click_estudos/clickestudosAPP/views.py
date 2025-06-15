from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Material
from .forms import MaterialForm

def index(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  # Redirecionar para dashboard após login
        else:
            messages.error(request, 'Usuário ou senha incorretos.')

    return render(request, 'clickestudosAPP/index.html')

@login_required
def dashboard(request):
    materiais = Material.objects.filter(usuario=request.user).order_by('-data_envio')
    return render(request, 'clickestudosAPP/dashboard.html', {'materiais': materiais})

@login_required
def upload_material(request):
    if request.method == 'POST':
        form = MaterialForm(request.POST, request.FILES)
        if form.is_valid():
            material = form.save(commit=False)
            material.usuario = request.user
            material.save()
            messages.success(request, 'Material enviado com sucesso!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Erro no envio. Verifique os dados e tente novamente.')
    else:
        form = MaterialForm()
    return render(request, 'upload.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    messages.info(request, 'Você saiu da sua conta.')
    return redirect('login')

def cadastro(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, 'As senhas não conferem.')
            return redirect('cadastro')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Usuário já cadastrado.')
            return redirect('cadastro')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'E-mail já cadastrado.')
            return redirect('cadastro')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, 'Usuário cadastrado com sucesso!')
        return redirect('login')

    return render(request, 'clickestudosAPP/cadastro.html')

def home(request):
    return render(request, 'clickestudosAPP/home.html')

def deletar_material(request, pk):
    material = get_object_or_404(Material, pk=pk)

    if material.usuario != request.user:
        messages.error(request, 'Você não tem permissão para deletar este material.')
        return redirect('dashboard')

    if request.method == 'POST':
        material.delete()
        messages.success(request, 'Material deletado com sucesso.')
        return redirect('dashboard')

    return render(request, 'clickestudosAPP/confirmar_delecao.html', {'material': material})
