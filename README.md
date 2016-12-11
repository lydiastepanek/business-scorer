# Wiki-path-finder

## To run
```
python wiki_path_finder.py N
```
(where N is the sample size/number of random sites being tested)

## About

Inspired by https://en.wikipedia.org/wiki/Wikipedia:Getting_to_Philosophy
"As of February 2016, 97% of all articles in Wikipedia eventually lead to the article Philosophy."
I wanted to see if this was true so I wrote this script using xpath. As an example, I ran it on 100 articles:
```
python wiki_path_finder.py 100
```
My script uses the "Random Article" link on Wikipedia to select 100 random articles. In this example, the output was the following:
```
{5: 2, 6: 1, 7: 3, 8: 8, 9: 8, 10: 7, 11: 11, 12: 9, 13: 5, 14: 8, 15: 7, 16: 8, 17: 3, 18: 5, 19: 1, 20: 2, 21: 3, 22: 3, None: 4, 24: 2}
```
This hash represents counts of each path length. A path length of "None" means that the article did not lead to the Philosophy page. As the output shows, 96% of those articles led to the Philosophy page.

## Notes:

If any of the following were the first link in the main article body, I skipped over it so that I had working links:
* Anchor tags that linked to an element within the current page i.e. `<a href="#section-1">`
* Red links (to dead pages) i.e. a link that led to https://en.wikipedia.org/wiki/New_Shiloh_Baptist_Church

Discarded paths that led to pages with the following problem:
* Pages that entered a never ending loop, such as `/Internal_migration` and  `/Human_migration`
* Pages with no viable links such as https://en.wikipedia.org/wiki/Association_for_Theatre_in_Higher_Education
