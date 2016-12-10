from lxml import html
import re
import requests
import sys

import facebook_score

class BusinessScorer(object):
    business_name = ''
    owner_name = ''
    url = ''

    def run(self, number):
        print facebook_score.run()
        return number;

if __name__ == "__main__":
    scorer = BusinessScorer()
    scorer.run(int(sys.argv[1]))
