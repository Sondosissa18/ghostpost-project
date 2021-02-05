from django.shortcuts import render
from ghostpost_app.models import GhostPost
from django.shortcuts import render, HttpResponseRedirect, reverse, redirect


from ghostpost_app.forms import CreatePostForm 


def index(request):
    posts = GhostPost.objects.all().order_by('-created_at')
    return render(
        request,
        "index.html",
        {'posts': posts},
    )


def sort_by_votes(request):
    # posts = GhostPost.objects.all().order_by('-upvote')
    posts= sorted(GhostPost.objects.all(), key=lambda item: item.upvote - item.downvote, reverse=True)
    return render(
        request,
        "index.html",
        {'posts': posts},
    )


def boasts(request):
    posts = GhostPost.objects.filter(ghostpost=True)
    return render(
        request,
        "index.html",
        {'posts': posts},
    )


def roasts(request):
    posts = GhostPost.objects.filter(ghostpost=False)
    return render(
        request,
        "index.html",
        {'posts': posts},
    )



def like_view(request, post_id):
    post = GhostPost.objects.filter(id=post_id).first()
    post.upvote += 1 
    post.save()
    return redirect('/')



def dislike_view(request, post_id):
    post = GhostPost.objects.filter(id=post_id).first()
    post.downvote += 1
    post.save()
    return redirect('/')


def create_post(request):
    html = "createpost.html"
    if request.method == "POST":
        form = CreatePostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_post = GhostPost.objects.create(
                    ghostpost=data["ghostpost"],
                    text = data['text']
                )
            return HttpResponseRedirect(reverse("homepage"))
    form = CreatePostForm()
    return render(request, html, {"form": form})


