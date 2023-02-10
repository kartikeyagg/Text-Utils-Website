## I have created this file - Kartikey

# code for video 6

from django.http import HttpResponse
from django.shortcuts import render

# def index(request):

#     # return HttpResponse("hello Kartikey ")
#     return HttpResponse(

#         '''<h1> Kartikey <h1> <a href = "https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7">
#          Django codewithharry</a> 
#          <h1> \n <h1>
         
#          <a href = "https://stackoverflow.com/questions/6468397/how-to-check-django-version">
#          Stack overflow </a> 
#          <h1> \n <h1>
#          <a href = "https://www.codingninjas.com/codestudio/home">
#          Code Studio </a> 
#          <h1> \n <h1>

#          <a href = "https://mail.google.com/mail/u/0/#inbox">
#          Gmail </a> 
#         <h1> \n <h1>
#          <a href = "https://twitter.com/explore">
#          Twitter </a> 
#          <h1> \n <h1>

         
         
#          '''


# #     )





# def about(request):

#     return HttpResponse("about kartikey ")


def index(request):

    params = {

        'name': "Larry",
        'age': "22",


    }

    return render(request , 'index.html',params)

def removepunc(request):
    
    #get the text
    djtext = request.POST.get('text', 'default')
    ## check boxes
    rmvpunct = request.POST.get('remove_punctuation','off')
    fullcaps = request.POST.get('full_caps','off')
    lrmv = request.POST.get('line_remove','off')
    sprmv = request.POST.get('space_remove','off')

    counter = request.GET.get('char_count','off')

    djtext = str(djtext)

    #analyze the text,
    # print(djtext)
    # print(rmvpunct)

    pntuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    analyzed = djtext
    p1= ""

    # check for check boxes which are on

    flag = 0

    if(rmvpunct == "on"):
        flag = 1
        s = ""

        p1 = "remove puctuation"

        for i in analyzed:
            if(i not in pntuation):
                s =  s + i
        analyzed =s

    if(fullcaps == "on"):
        flag = 1


        p1 = "convert to upper case"        
        
        analyzed = (analyzed).upper()

        analyzed = str(analyzed)


    if(lrmv == "on"):
        flag = 1

        p1 = "line remover"
        s = ""
        for i in analyzed :
            if(i != "\n"):
                s +=i
        analyzed = s

    if(sprmv == "on"):
        flag = 1

        p1 = "space remover "
        s = ""
        prev = ""

        for i in analyzed:
            if(i == " " and prev==" "):
                continue
            else:
                s +=i
            prev = i
        analyzed = s
    if(counter == "on"):
        flag = 1

        p1 = "char counter "
        count = 0
        for i in djtext:
            count+=1

        analyzed = count
    
    
    if(flag == 0):
        analyzed = djtext
        

    params = {

        'purpose' : p1,

        'analyzed_text': analyzed,


    }

    return render(request, 'analyze.html', params)
    

    # return HttpResponse("remover p \n <button onclick='history.back()'>Go Back</button>")

def capfirst(request):

    return HttpResponse("capitilize first \n <button onclick='history.back()'>Go Back</button>")

def new_line_remove(request):

    return HttpResponse('''new_line_remove \n <button onclick="history.back()">Go Back</button>''')



def space_remove(request):

    return HttpResponse("space_remove \n <button onclick='history.back()'>Go Back</button>")

def char_count(request):

    return HttpResponse("char_count \n <button onclick='history.back()'>Go Back</button>")



# def capfirst(request):

#     return HttpResponse("capitilize first")