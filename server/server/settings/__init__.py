from .common import *

if DEBUG:
	from .development import *
else:
	from .production import *
