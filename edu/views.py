from django.views.generic import View
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
class Index(View):
    template_name = "index.html"
    
    def get(self, request):
        return render(request, self.template_name)
    
class TagStudy(View):
    template_name = "tag_study.html"
    
    def get(self, request):
        return render(request, self.template_name)
    
class palgong(View):
    template_name = "palgong.html"
    
    def get(self, request):
        return render(request,self.template_name)
    def post(self, request):
        param = request.POST.get('tea','')
        print(f"param = {param}")
        return redirect("edu:tag_study")