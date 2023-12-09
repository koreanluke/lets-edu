from django.views.generic import View, DetailView
from django.shortcuts import render, get_object_or_404, redirect
from .models import Feed
# Create your views here.
class Index(View):
    template_name = "index.html"
    
    def get(self, request):
        return render(request, self.template_name)
    
class TagStudy(View):
    template_name = "tag_study.html"
    
    def get(self, request):
        feeds = Feed.objects.all().order_by('id')

        return render(request, self.template_name,
                      {'feed_list':feeds})
    
class NewContent(View):
    template_name = "upload_form.html"
    
    def get(self, request):

        return render(request,self.template_name)
    def post(self, request):
        param = request.POST.get('content','')
        param2= request.FILES.get('up_photo' , False)
        print(f"param2:{param2}")
        feed = Feed(content=param, photo=param2)
        feed.save()
        return redirect("edu:tag_study")
    
class FeedDetail(DetailView):
    model = Feed
    template_name = "feed/detail.html"
    
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        feed = get_object_or_404(Feed, pk = self.kwargs['pk'])
        context['feed'] = feed
        
        return context