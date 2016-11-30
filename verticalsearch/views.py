from django.shortcuts import render_to_response
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.template import RequestContext
import sqlitedb
import datetime

# Create your views here.

title=("SELECT Title from db_table WHERE Keyword=mobile")
price=("SELECT Price from db_table WHERE Keyword=mobile")
availability=("SELECT Availability from db_table WHERE Keyword=mobile")
info=("SELECT Info from db_table WHERE Keyword=mobile")
url=("SELECT URL from db_table WHERE Keyword=mobile")


def wrapStringInHTMLWindows(title,price,availability,info,url):
    filename = 'result.html'
    f = open(filename,'w')

    wrapper = """<html>
    <head>
    <title>SRS Vertical Search Engine-Results</title>
    </head>
    <body><a href="%"><h2>%</h2></a>
	<a href="%" class="url"><p>%</p></a>
	<span class="Pr-Av"><b>Price: </b></span>
	<span class="values">%</span>
	<span class="Pr-Av"><b>|  Availability:</b></span>
	<span class="values">%</span>
	<p class="info">%</p></body>
    </html>"""

    whole = wrapper % (url,title,url,url,price,availability,info)
    f.write(whole)
    f.close()


def search(request):
    if not request.method == 'GET':
        HttpResponseRedirect('search.html')

    parameter = request.GET
    if len(parameter)!= 0 and parameter.get('query') != 'mobile':
        return render_to_response('no_result.html')

    elif parameter.get('query') == 'mobile':
        return render_to_response('result.html')

    else:
        return render_to_response('search.html') 
