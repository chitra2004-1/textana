# my page build by me
from django.http import HttpResponse
from django.shortcuts import render
def index(request):

        dict={'name':'chitra','age':21}
        return render(request,'index.html',dict)
def analyze(request):
    text=request.GET.get('text','default')
    removp=request.GET.get('check','off')
    analyzed=""
    punctli='''! @ # $ % ^ & * ( ) _ + - = { } [ ] | \ : ; " ' < > , . ? / ~'''
    for i in text:
        if i not in punctli:
            analyzed=analyzed+i
    para={'perpose':'remove punc','anal_txt':analyzed}
    return render(request,'analyze.html',para)

# def removepunc(request):
#     text=request.GET.get('text','default')
#     print(text)
#     return HttpResponse("aa")
#
# def capital(request):
#     print(request.GET.get('text','default'))
#     return HttpResponse("capi")



