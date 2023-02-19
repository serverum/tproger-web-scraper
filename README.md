# tproger-web-scraper
Simple tproger.ru articles web-scraper (request + bs + csv)

### Usage of the web scraper
1. settings.py - first you should fill it with desired data to scrape, BASE_URL & PAGES_NAME, insert desired pages names of the tproger to scrape

```
BASE_URL = "https://tproger.ru/{tag}/page/{page_number}/" # Put any page you want to scrape

PAGES_NAMES = [
    "python", 
] 
```

2. main.py - adjust main() as you want, how many pages you would like to scrape & so on. parse_request(name, 1, []) as it goes
3. python.csv - example of the web-scraper results you should get.
