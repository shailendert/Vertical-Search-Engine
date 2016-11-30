from google import search
import csv

try:
    term=getQueryFromUser()
    docs=[posting[0] for posting in index[term]]
except:
    #term is not in index
    docs=[]


