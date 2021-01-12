from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    params = {'name':'satish','place':'earth'}
    return render(request,'index.html',params)





def analyze(request):
    djtext = request.GET.get('text','default')
    removepunc = request.GET.get('removepunc','off')
    capall = request.GET.get('capall','off')
    newlinerem = request.GET.get('newlinerem', 'off')
    exspacerem = request.GET.get('exspacerem', 'off')
    charcount = request.GET.get('charcount', 'off')
    
    if removepunc == 'on':
        punc = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzedString = ""
        for char in djtext:
            if char=='\n':
                analyzedString = analyzedString + '\n'
            elif char not in punc:
                analyzedString = analyzedString + char
        params = {'purpose':'remove punctuation','analyzedText':analyzedString}
        return render(request,'analyze.html',params)
    elif capall=='on':
        analyzedString=djtext
        analyzedString = analyzedString.upper()
        params = {'purpose': 'capitalize all',
                  'analyzedText': analyzedString}
        return render(request, 'analyze.html', params)
    elif newlinerem == "on":
        analyzedString=""
        for char in djtext:
            if char!='\n':
                analyzedString=analyzedString+char
        params = {'purpose': 'Newline Remover',
                  'analyzedText': analyzedString}
        return render(request, 'analyze.html', params)
    elif exspacerem=="on":
        analyzedString = ""
        for index,char in enumerate(djtext):
            if index==' ' and index+1==' ':
                analyzedString = analyzedString+char
            else:
                analyzedString = analyzedString+char
        params = {'purpose': 'Extra Space Remover',
                  'analyzedText': analyzedString}
        return render(request, 'analyze.html', params)
    elif charcount == "on":
        count = len(djtext)
        params = {'purpose': 'Character Counter',
                  'analyzedText': count}
        return render(request, 'analyze.html', params)
    else:
         return HttpResponse('Error')
