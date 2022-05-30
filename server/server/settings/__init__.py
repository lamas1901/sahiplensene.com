import environ

from .common import *

env = environ.Env()
env.read_env(BASE_DIR/'.env')

DEBUG = int(env('DEBUG')) 
 
if DEBUG:
	from .development import *
else:
	from .production import *
