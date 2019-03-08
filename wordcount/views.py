from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request,'home.html')

def count(request):
    data = request.GET['fulltextarea']
    #print(data)
    word_list = data.split()

    #print(word_list)

    length_list = len(word_list)
    
    worddictionary = {}
    
    for word in word_list:
        if word in worddictionary:
            worddictionary[word] +=1
        else:
            worddictionary[word] = 1



    sort_list=sorted(worddictionary.items(), key=operator.itemgetter(1),reverse=True)


    return render(request,'count.html',{'textarea':data , 'word':length_list, 'worddictionary':sort_list})



def about(request):
    return render(request,'about.html')