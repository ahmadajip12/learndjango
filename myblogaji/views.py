from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.db.models import Count, Sum, Avg
from .models import Post, Command, Tag
from .forms import PostForm, CommandForm

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date').annotate(num_command=Count('commands'), num_like=Count('like'))
    post_data = Post.objects.aggregate(total_command=Count('commands'), avg_like=Avg('like'))
    tags = Tag.objects.all()
    return render(request, 'myblogaji/post_list.html', {'posts': posts, 'tags': tags, "post_data": post_data})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    command = Command.objects.select_related('post').filter(post=post)
    sum_command = command.count()
    return render(request, 'myblogaji/post_detail.html', {'post': post, "commands": command, 'sum_command': sum_command})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'myblogaji/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'myblogaji/post_edit.html', {'form': form})

def post_command(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommandForm(request.POST)
        # form.validation_title()
        if form.is_valid():
            form.save_form(post)
            # command = Command()
            # command.title_command = form.cleaned_data['title_command']
            # command.command = form.cleaned_data['command']
            # command.post = post
            # command.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommandForm()
    return render(request, 'myblogaji/post_command.html', {'form': form})

def post_tag(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    posts = Post.objects.prefetch_related('tag').filter(tag__id=tag.pk)
    return render(request, 'myblogaji/post_tag.html', {'posts': posts, 'tag': tag})

def post_like(request, pk):
    post = get_object_or_404(Post, pk=pk)
    like = post.like
    post.like = like + 1
    post.save()
    return redirect('/post/'+str(pk)+'/')

def post_dislike(request, pk):
    post = get_object_or_404(Post, pk=pk)
    dislike = post.dislike
    post.dislike = dislike + 1
    post.save()
    return redirect('/post/'+str(pk)+'/')

def post_search(request):
    keyword = request.GET['search']
    posts = Post.objects.filter(title__contains=keyword)
    return render(request, 'myblogaji/post_search.html', {'posts': posts
    })