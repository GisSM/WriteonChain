from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from django.http import JsonResponse
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from .utils import get_ip

def post_all(request):
    posts=Post.objects.filter().order_by('-data_creazione')
    for post in posts:
        if not post.data_pubblicazione:post.pubblished()
    posts = Post.objects.filter().order_by('-data_pubblicazione')
    return render(request,'posts/post_all.html',{'posts':posts})

def post_lastfive(request):
    posts=Post.objects.filter().order_by('-data_creazione')[:5]
    for post in posts:
        if post.txId=='Invio transazione in corso...':post.write_on_chain()
        if not post.data_pubblicazione:post.pubblished()
    posts = Post.objects.filter().order_by('-data_pubblicazione')[:5]
    return render(request, 'homepage/homepage.html', {'posts': posts})

def post_detail(request, id, slug):
    post = get_object_or_404(Post,id=id,slug=slug)
    return render(request,'posts/post_detail.html',{'post':post})

def post_new(request):
    if request.method == 'POST':
      form = PostForm(request.POST)
      post = form.save(commit=False)
      if 'hack' not in post.testo and 'HACK' not in post.testo and 'Hack' not in post.testo  :
         if form.is_valid():
            post.utente = request.user
            post.write_on_chain()
            post.pubblished()
            post.save()
            return redirect('homepage')
      else:
          errore='Non puoi inserire la parola "HACK"'
          form = PostForm()
          return render(request, 'posts/post_new.html', {'form': form,'errore':errore})
    else:
     form= PostForm()
    return render(request,'posts/post_new.html',{'form':form})

def post_edit(request, id, slug):
    post = get_object_or_404(Post, id=id, slug=slug)
    if request.method == "POST":
      form = PostForm(request.POST, instance=post)
      if form.is_valid():
            post = form.save(commit=False)
            post.utente = request.user
            post.write_on_chain()
            post.save()
            return redirect('homepage')
    else:
        form = PostForm(instance=post)
    return render(request, 'posts/post_new.html', {'form': form})

def post_profilo(request,user,id):
    user=get_object_or_404(User,username=user,id=id)
    posts=Post.objects.filter(utente=user)
    return render(request,'account/profilo.html',{'posts':posts})

def api_post(request):
    return render(request,'posts/api_post.html')

def post_api_all(request):
    all_posts=[]
    posts=Post.objects.all()
    for post in posts:
        all_posts.append({
            'utente':post.utente.username,
            'titolo':post.titolo,
            'data_creazione':post.data_creazione,
            'data_pubb':post.data_pubblicazione,
            'hash_testo':post.hash,
            'hash_transazione':post.txId,
            'testo':post.testo,
        })
    return JsonResponse({'all_posts':all_posts},safe=False)

def post_api_1h(request):
    posts_1h=[]
    now = datetime.now()
    hour_before = now - timedelta(hours=1)
    posts=Post.objects.filter(data_pubblicazione__range=(hour_before, now))
    for post in posts:
        posts_1h.append({
            'utente':post.utente.username,
            'titolo':post.titolo,
            'data_creazione':post.data_creazione,
            'data_pubb':post.data_pubblicazione,
             'hash_testo':post.hash,
             'hash_transazione':post.txId,
             'testo':post.testo,
        })
    return JsonResponse({'post_last_1h':posts_1h},safe=False)


