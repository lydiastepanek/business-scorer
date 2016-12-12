#Business P Score Calculator

##About

This program takes a business name, and uses publicly available data from the Google Places API and the Wikipedia API to construct a “P score” for any given small business, which represents how likely the business is to default on a 3‐year loan we extend to the business.

APIs used:
* Google Places
* Wikipedia

I used APIs that dont require OAUTH because I wanted to avoid any manual intervention on the part of the user running the script.

I really wanted to use the Facebook Graph API and looked at such modules as python-sdk and facebook-sdk. See [To Do](##To Do) section for more details.

##How the P Score is Calculated

The P Score is an average of two scores, the Google Places score (the score calculated by metrics provided by the Google Places API) and the Wikipedia Score.

The Google Places score is between 0 and 1 depending on these factors:
* rating - the average rating that customers give the business (if not available
  then 0)
* business_categories - the number of categories this business falls under (i.e.
  restaurant, airport, etc -- see
  https://developers.google.com/places/web-service/supported_types). My
  assumption here was that if the business has many products and industries,
  then it is less likely to default given that if one of its products is not
  successful, it can pivot.

The Wikipedia score is between 0 and 1 depending on these factors:
* total_hits - the number of Wikipedia page results when you search the business
  name
* updated_recently - whether the first page result has been updated within the
  past year (I used this metric to measure whether the business was still
  in business)

##To run
```
python business_scorer.py "[Business Name]|[Business Address]"
```

##To Do
I wanted to use the Facebook Graph API Page endpoint so that, given a business's Facebook page ID (the id in the url of its Facebook page, i.e. cocacola), I could access the business's following information:
* is_permanently_closed
* can_checkin && checkins - Number of checkins at the business
* fan_count
* founded
* rating_count
* app_links (app ids for mobile apps)

Given the downsides of oauth, I decided not to use the API, but may add this functionality in the future.

I also need to add tests.
