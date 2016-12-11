import numpy
import google_scorer
import wiki_scorer

# GOOGLE
business_name = 'Asanda Aveda Spa Lounge'
business_address = '598 Broadway, New York, NY'
owner_name = ''
url = ''
# WIKI
#  business_name = 'Asanda Aveda Spa Lounge'
#  business_name = 'Sinatraa'
#  business_name = 'Tim Jones'

class BusinessScorer(object):

    def run(self):
        google_score = google_scorer.run(business_name, business_address)
        wiki_score = wiki_scorer.run(business_name)
        print google_score
        print wiki_score
        return numpy.mean([google_score, wiki_score])

if __name__ == "__main__":
    scorer = BusinessScorer()
    print scorer.run()
