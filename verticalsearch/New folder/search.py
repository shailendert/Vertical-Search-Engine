'''
@author: shailender
'''

from django.db import connection
from django.db.models import Sum
from tokenize_docs import get_term_freq_dict
from models import Document, DocFrequency, TermFrequency
import math

def process_query(data):
    # Return term
    print get_term_freq_dict(data).keys()
    return get_term_freq_dict(data).keys()

def is_all_terms_matched(doc_terms, terms):
    matched_terms = doc_terms.split(",")
    if len(matched_terms) == len(terms):
        return True
    
    return False
    

def rank(query):
    # Filter when term is inside searched query string
    # terms = process_query(query)
    terms = query.lower().split()
    
    
    
    rows = TermFrequency.objects.filter(term__in=terms)\
                                .values('document')\
                                .annotate(total_score=Sum('score'))\
                                .order_by('-total_score')[:100]
        
#    doc_ids = [x[0] for x in rows if is_all_terms_matched(x[1], terms)]
    doc_ids = [x['document'] for x in rows]
    # Retrieve document
    docs = Document.objects.filter(id__in=doc_ids)
    for i in xrange(len(docs)):
        doc = docs[i]
        doc.score = math.ceil(rows[i]['total_score']*100)/100 
    return docs
    

def search_term(term):
    print term
    
    doc_freqs = DocFrequency.objects.filter(term__startswith=term).order_by('-num_docs')[:10]
    suggested_terms = [x.term for x in doc_freqs]
    return suggested_terms

# Execute
if __name__ == '__main__':
    rank(q.get())
