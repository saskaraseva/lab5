from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.
def function_view(request):
    return HttpResponse('Response :)')


class ExampleClassBased(View):
	def get(self, request):
		return HttpResponse('response from class based view')


def Example_template(request):
	print('Hello')
	return render(request, 'asd.html')