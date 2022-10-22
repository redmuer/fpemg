import requests
import cloudscraper

scraper = cloudscraper.create_scraper(browser={'browser': 'firefox', 'platform': 'windows', 'mobile': False})
resp = scraper.get("https://public-wax-on.wax.io/wam/sign")
print(resp.text)
