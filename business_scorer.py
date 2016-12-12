import sys
import numpy
import src.google_scorer
import src.wiki_scorer

def main(argv):
    arguments = "".join(argv).split("|")
    business_name = str.strip(arguments[0])
    business_address = str.strip(arguments[1])
    return run(business_name, business_address)

def run(business_name, business_address):
    google_score = src.google_scorer.run(business_name, business_address)
    wiki_score = src.wiki_scorer.run(business_name)
    return str(numpy.mean([google_score, wiki_score]))

if __name__ == '__main__':
    print "The business's score is " + main(sys.argv[1:])
