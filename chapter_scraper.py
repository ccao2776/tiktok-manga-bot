from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import sys
import os
import time

start = time.time()
with sync_playwright() as p:
    browser = p.chromium.launch()

    page = browser.new_page()
    page.goto('https://kissmanga.org/chapter/manga-iw985379/chapter-1')
    page.wait_for_load_state()


    html_content = page.content()

    soup = BeautifulSoup(html_content, 'html.parser')


    target_div = soup.find('div', id="centerDivVideo")

    img_elements = target_div.find_all('img')
    img_urls = [img_element.get('src') for img_element in img_elements]

    # TODO: Add Understandable Name
    chapter_directory = 'fillInHere'
    # os.mkdir(chapter_directory)
    for idx, img_url in enumerate(img_urls):
        page.goto(img_url)
        page.screenshot(path=os.path.join(chapter_directory, str(idx) + ".jpg"))

    page.close()

finish = time.time()
print(f"Total Seconds Elapsed: {finish - start}")