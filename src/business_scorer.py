from lxml import html
import re
import requests
import sys

from facebook_score import FacebookScorer

class BusinessScorer(object):
    business_name = ''
    owner_name = ''
    url = ''

    def run(self, number):
        print FacebookScorer().run()
        return number;


if __name__ == "__main__":
    scorer = BusinessScorer()
    scorer.run(int(sys.argv[1]))
