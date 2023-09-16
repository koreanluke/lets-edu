from django.views.generic import View
from django.shortcuts import render, get_object_or_404

# Create your views here.
class Index(View):
    template = "index.html"
    def get(self, request):
        return render(request, self.template)