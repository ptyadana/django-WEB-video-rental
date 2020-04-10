# Vidly Video Rental Application and API

Vidly Video Rental Application which displays the list of movie information, details movie information in both as App or JSON for API integration.

+ Python 3
+ Django 3
+ bootstrap 4

[Visit Vidly Video Rental App on heroku](https://vidly-movie-rental-by-ptyadana.herokuapp.com/)

-----

[For Videly API end points](https://vidly-movie-rental-by-ptyadana.herokuapp.com/api/movies/)

#### Sample JSON
```javascript
{
  "meta": {
    "limit": 20,
    "next": null,
    "offset": 0,
    "previous": null,
    "total_count": 3
  },
  "objects": [
    {
      "daily_rental_rate": 2.5,
      "id": 1,
      "number_in_stock": 30,
      "released_year": 2019,
      "resource_uri": "/api/movies/1/",
      "title": "Spiderman Far From Home"
    },
    {
      "daily_rental_rate": 1.5,
      "id": 2,
      "number_in_stock": 10,
      "released_year": 2012,
      "resource_uri": "/api/movies/2/",
      "title": "Man In Black 3"
    },
    {
      "daily_rental_rate": 2.5,
      "id": 3,
      "number_in_stock": 15,
      "released_year": 1990,
      "resource_uri": "/api/movies/3/",
      "title": "Home Alone"
    }
  ]
}