from lxml import html
import re
import requests
import sys

class BusinessScorer(object) :

    def run(self, number):
        return number;


scorer = BusinessScorer()
scorer.run(int(sys.argv[1]))
