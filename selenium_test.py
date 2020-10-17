#!/usr/bin/env python3
import sys
import time
from selenium import webdriver
import chromedriver_binary

if len(sys.argv) != 2:
	print("Usage: selenium.py PHP_SITE_URL")
	sys.exit(1)

PHP_TEST_URL = sys.argv[1]

print("Fetching url", PHP_TEST_URL)

opts = webdriver.ChromeOptions()
opts.add_argument("--headless")

browser = webdriver.Chrome(options=opts)
browser.get(PHP_TEST_URL)

about_us = browser.find_element_by_id("About Us")
about_us.click()

test_str = browser.find_element_by_id('PID-ab2-pg').text
print("Recived from PHP site", test_str)

compare_str = """
This is about page. Lorem Ipsum Dipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.

It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).
"""

if test_str != compare_str:
	print("String doesn't match")
	sys.exit(1)
else:
	print("String matched")
	sys.exit(0)

