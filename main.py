from general import*
from crawl import*

directory=raw_input('Enter the project name: ')
url=raw_input('Enter the Url to crawl: ')


#creating Project
create_project_dir(directory)
create_data_files(directory,url)

to_crawl,crawled=crawl_web(url,directory)
queue_set,crawled_set=set(to_crawl),set(crawled)

set_to_file(queue_set, directory+"/"+"queue.txt")
set_to_file(crawled_set, directory+"/"+"crawled.txt")



print("END")
