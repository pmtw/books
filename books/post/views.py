from django.shortcuts import render
from django.shortcuts import render_to_response


from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic import DeleteView
from django.core.urlresolvers import reverse, reverse_lazy
from braces.views import LoginRequiredMixin

from post.models import Post, Comment
from post.forms import PostForm, CommentForm

#from post.models import Post, Comment
#from post.forms import PostForm, CommentForm

# Create your views here.
# get_context_data(None, 'test', 'test', moje=1)



class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'post/add_comment.html'
#    success_url = reverse_lazy('view')

#    @property
#    def success_url(self):
#        return reverse('view')

    def get_success_url(self):
        return reverse_lazy('view', 
            kwargs={'pk': self.object.post.pk})

            
'''
    def get_context_data(self, **kwargs):
        cont_post = Post.objects.get(pk=self.kwargs['post_pk'])
        comments = Comment.objects.filter(post=cont_post)
        return {'object': self.object, 'cont_post': cont_post, 'comments': comments}  
'''
'''
    def get_context_data(self, **kwargs):
        context = super(CommentCreateView, self).get_context_data()
        context['post'] = Post.objects.get(pk=self.kwargs['post_pk'])
        context['comments'] = Comment.objects.filter(post=context['post'])
        return {'object': self.object, 'post': context['post'], 'comments': context['comments']}  
'''      
'''
    def get_form_kwargs(self):
        form_kwargs = super(CommentCreateView, self).get_form_kwargs()
        post = Post.objects.get(pk=self.kwargs['post_pk'])
        instance = Comment(post=post)
        form_kwargs['instance'] = instance
        return form_kwargs

    def get_context_data(self, **kwargs):
        context = super(CommentCreateView, self).get_context_data(**kwargs)
        context['post'] = Post.objects.get(pk=self.kwargs['post_pk'])
        context['comments'] = Comment.objects.filter(
            post=context['post'])
        return context
'''

class CommentDeleteView(DeleteView):
    model = Comment
    template_name = 'post/comment_confirm_delete.html'
    success_url = reverse_lazy('posts')
'''
    def get_success_url(self):
        return reverse_lazy('view', 
            kwargs={'pk': self.kwargs['post_pk']})
'''

class PostDetailView(DetailView):
    model = Post
    template_name = 'post/view.html'
   
    def get_context_data(self, **kwargs):
        comments = Comment.objects.filter(post=self.object)
        return {'object': self.object, 'comments': comments}  
'''
def post_detail(request, pk):
    object = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=object)
    return render(request, 'post/detail.html', {'object': object, 'comments': comments})
'''

class PostListView(ListView):
    model = Post
    template_name = 'post/list.html'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post/add.html'
    success_url = reverse_lazy('posts')
#    @property
#    def success_url(self):
#       return reverse('posts')
'''
    def form_valid(self, form):
    
        f_valid =  super(PostCreateView, self).form_valid(form)
        return f_valid  
        
'''        
class PostEditView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'post/add.html'
    success_url = reverse_lazy('posts')
#    @property
#    def success_url(self):
#        return reverse('posts')
 
 
    
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post/post_confirm_delete.html'
    success_url = reverse_lazy('posts')
    
