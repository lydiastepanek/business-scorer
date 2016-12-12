import sys
import numpy
import src.google_scorer
import src.wiki_scorer

def main(argv):
    arguments = "".join(argv).split("|")
    google_api_key = str.strip(arguments[0])
    business_name = str.strip(arguments[1])
    business_address = str.strip(arguments[2])
    return run(business_name, business_address, google_api_key)

def run(business_name, business_address, google_api_key):
    google_score = src.google_scorer.run(business_name, business_address, google_api_key)
    wiki_score = src.wiki_scorer.run(business_name)
    return str(numpy.mean([google_score, wiki_score]))

if __name__ == '__main__':
    print "P score: " + main(sys.argv[1:])
