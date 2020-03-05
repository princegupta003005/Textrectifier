from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    #return HttpResponse('''<h1>hello</h>''')
    return render (request,'home.html')



def analyze(request):
    djtext=request.POST.get('text','default')
    removepunc = request.POST.get('removepunc', 'off')
    capfirst = request.POST.get('capfirst', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')

    print(removepunc)
    print(djtext)
    #analyzed=djtext
    if removepunc=="on":

        analyzed=""
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
                params={'purpose':'removepunc','analyzed_text':analyzed}
        return render(request,'analyze2.html',params)
    elif capfirst=="on":
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params={'purpose':'capitalise','analyzed_text':analyzed}
        return render(request,'analyze2.html',params)
    elif (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                  analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # Analyze the text
        return render(request, 'analyze2.html', params)

    elif (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
            else:
                print("no")
        print("pre", analyzed)
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        print(params)
        # Analyze the text
        return render(request, 'analyze2.html', params)
    else:
        return HttpResponse("Errors")







    #return HttpResponse('''<h1>remove punc</h1><a href="http://127.0.0.1:8000">backkk to home</a>''')
#def index1(request):
 #   file = open("one.txt", 'r')
  #  return HttpResponse(file.read())

#def capfirst(request):
    #return HttpResponse ('''<h1>capfijjst</h1><a href="/">back to home</a>''')
#def newlineremove(request):
  #  return HttpResponse ('''<h1>newlineremove</h1><a href="http://127.0.0.1:8000/capfirst">back to capfirst</a>''')
#def spaceremover(request):
    #return HttpResponse ('''<h1>spaceremover</h1><a href="http://127.0.0.1:8000/newlineremove">back to removepunc</a>''')
#def charcount(request):
   # return HttpResponse ('''<h1>charcount</h1><a href="http://127.0.0.1:8000/spaceremover">back to spaceremover</a>''')'''
