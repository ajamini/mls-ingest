login_url = 'http://rets.torontomls.net:6103/rets-treb3pv/server/login'
#login_url = 'http://data.crea.ca/Login.svc/Login'
username = 'D18ais'
password = 'M64#a85'

s3_reader = False #Enable S3, if Disabled Local file System will be used.

SESSION_LISTINGS_COUNT=100

SECONDS_IN_DAY = 86400

MAX_UPDATE_TIME = 10 * SECONDS_IN_DAY #10 Days maximum limit for update time.

PHOTOS_DOWNLOAD_RETRIES = 3

MEDIA_DIR = 'media'
LISTING_DIR = MEDIA_DIR + '/' + 'listings'
AGENTS_DIR = MEDIA_DIR + '/' + 'agents'

LOG_FILENAME='ddf_task.log'






