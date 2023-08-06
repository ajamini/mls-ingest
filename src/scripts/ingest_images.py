# from libs.ddf_client import DDFClient
# from libs.ddf_s3 import S3Handler
# from libs.settings import *
# import redis
# from rq import Queue
# from datetime import datetime
#
# r = redis.Redis()
# queue = Queue(name='property_ingest', connection=redis.Redis())
#
# ddf_c = DDFClient(MEDIA_DIR, format_type='STANDARD-XML', s3_reader=s3_reader)
# ddf_c.login()
# listings, count = ddf_c.streamer.retrieve_active_records(last_update=datetime.now())
#
# media = S3Handler(media_dir='media', rets_session=ddf_c.rets_session)
# for listing in listings:
#     media.download_photos([listing], {})
#     print(listing['MLS'])
