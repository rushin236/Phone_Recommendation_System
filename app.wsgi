import site
import sys

# Add the site-packages of the chosen virtualenv to work with
site.addsitedir('/var/www/html/Phone_recommendation_system/venv/lib/python3.10/site-packages')

sys.path.insert(0, "/var/www/html/Phone_recommendation_system/")

from app import app as application
