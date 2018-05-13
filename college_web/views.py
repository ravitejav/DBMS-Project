from django.http import Http404, HttpResponseRedirect

def redirect(request):
    return HttpResponseRedirect('/log')