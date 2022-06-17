from django.views import generic
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .forms import PostForm
from django.shortcuts import render

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

class SignUpView(generic.CreateView):
    print("ssinging you in")
    success_url = reverse_lazy("login")
    form_class = UserCreationForm
    template_name = "signup.html"
def contact(request):
    if request.method == 'POST':
        # POST, generate form with data from the request
        form = PostForm(request.POST)
        if form.is_valid():
            dweet = form.save(commit=False)
            dweet.author = request.user
            dweet.save()
        # Reference is now a bound instance with user data sent in POST 
        # process data, insert into DB, generate email, redirect to a new URL,etc
    else:
        # GET, generate blank form
        form = PostForm()
        # Reference is now an unbound (empty) form
    # Reference form instance (bound/unbound) is sent to template for rendering
    return render(request,'post.html',{'form':form})