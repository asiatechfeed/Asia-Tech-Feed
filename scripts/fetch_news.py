#!/usr/bin/env python3
"""
Asia Tech News Feed — Daily Scraper
Scrapes 12 news sources, filters for SE Asia + keywords,
summarizes via Claude API, generates Jekyll posts + TSV for Google Sheets.
"""

import os
import sys
import json
import time
import hashlib
import re
import csv
import io
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.parse import urljoin, urlparse

import requests
import feedparser
from bs4 import BeautifulSoup
from dateutil import parser as dateparser
import pytz
import anthropic
import requests
import feedparser
from bs4 import BeautifulSoup
from dateutil import parser as dateparser
import pytz
import anthropic