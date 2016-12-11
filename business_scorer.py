import numpy
import src.google_scorer
import src.wiki_scorer

#  business_name = 'Asanda Aveda Spa Lounge'
business_name = 'Sinatraa'
#  business_name = 'Tim Jones'
business_address = '598 Broadway, New York, NY'
owner_name = ''
url = ''

class BusinessScorer(object):

    def run(self):
        google_score = src.google_scorer.run(business_name, business_address)
        wiki_score = src.wiki_scorer.run(business_name)
        return numpy.mean([google_score, wiki_score])

if __name__ == '__main__':
    scorer = BusinessScorer()
    print scorer.run()
