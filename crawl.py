import urllib2
from general import*
from bs4 import BeautifulSoup
from urlparse import urljoin
from urlparse import urlparse
from urllib2 import HTTPError
from urllib2 import URLError



def get_all_links(source,domain):
    all_links=[]
    a_tags=source.findAll("a")
    for tags in a_tags:
        link=tags.get("href")
        if link=="#":
            continue
        parse_u=urlparse(link)
        if parse_u.path[:2]=="..":
            valid_link=urljoin(domain,parse_u.path[2:])
        else:
            valid_link=urljoin(domain,link)
        if domain not in valid_link:
            continue
        all_links.append(valid_link)
    return (all_links)

    

def get_content(url):
    try:
        html=urllib2.urlopen(url)
        if html.headers['Content-Type']=='text/html':
            html_bytes = html.read()
            html_string = html_bytes.decode("utf-8")
            source=BeautifulSoup(html_string)
        else:
            source=None
    except urllib2.HTTPError as e:
        source=None
    except URLError as e:
        source=None
    return source

def union(listA,listB):
    for element in listB:
        listA.append(element)
        
def add_links_to_queue(links,to_crawl,crawled):
    for url in links:
        if (url in to_crawl) or (url in crawled):
            continue
        to_crawl.append(url)    

def crawl_web(url,directory):
    parsed_uri = urlparse( url )
    domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
    to_crawl=[url]
    crawled=[]
    while to_crawl:
        page=to_crawl.pop()
        if page not in crawled :
            content=get_content(page)
            if content is None:
                print("html code not found",page)
                crawled.append(page)
                continue
            add_links_to_queue(get_all_links(content,domain),to_crawl,crawled)
            crawled.append(page)
            to_crawl_set=set(to_crawl)
            crawled_set=set(crawled)
            print(str(len(to_crawl_set))+" links in the Queue      |     "+str(len(crawled_set))+" links Crawled" )
            set_to_file(directory+"/"+"queue.txt",to_crawl)
            set_to_file(directory+"/"+"crawled.txt",crawled)
            to_crawl_set=file_to_set(directory+"/"+"queue.txt")
            crawled_set=file_to_set(directory+"/"+"crawled.txt")
            to_crawl=list(to_crawl_set)
            crawled=list(crawled_set)
            
    return to_crawl,crawled    


    

