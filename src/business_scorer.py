from lxml import html
import re
import requests
import sys

import google_score

business_name = 'Asanda Aveda Spa Lounge'
business_address = '598 Broadway, New York, NY'
owner_name = ''
url = ''

class BusinessScorer(object):

    def run(self):
        google_score.run(business_name, business_address)

if __name__ == "__main__":
    scorer = BusinessScorer()
    scorer.run()
