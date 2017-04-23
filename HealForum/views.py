from django.shortcuts import HttpResponseRedirect, redirect
from django.shortcuts import render

from HealUsers.models import Doctor
from .models import Comment
from .models import Post


# Create your views here.
def table_department(request):
    if not request.user.is_anonymous:
        c = {
            "user": request.user,
            "posts": Post.objects.all(),
            "comments": Comment.objects.all(),
        }
        c["doctors"] = Doctor.objects.all()
        if request.method == "POST" and "post_btn" in request.POST:
            title = request.user.username
            context = request.POST.get("post")
            Post.objects.create(title=title, description=context, created_by=c["user"])
            c["posts"] = Post.objects.all()
            return HttpResponseRedirect("Forum/table_department.html", c)
        return render(request, "Forum/table_department.html", c)
    else:
        return render(request, "auth/login.html")


# @login_required
def create_comment(request, id):
    if request.method == "POST" and 'comment_btn' in request.POST:
        desc = request.POST.get("description_comment")
        commented_by = request.user
        comment = Post.objects.get(pk=id)
        if str(desc).count(desc) != 0:
            Comment.objects.create(comment=comment, description_comment=desc, commented_by=commented_by)
            return redirect(to='forum2')
    return redirect('index')
