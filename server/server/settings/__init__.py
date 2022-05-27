import os

from .common import *

DEBUG = int(os.environ.get('DJANGO_DEBUG')) 
 
if DEBUG:
	from .development import *
else:
	from .production import *
