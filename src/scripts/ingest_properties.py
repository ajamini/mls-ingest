# import gzip
# import io
# import pickle
# import zlib
# from os import environ
# import django
# import rq
# from redis import Redis
# from rq.job import Job, unpickle
#
# from libs.ddf_s3 import S3Handler
# from libs.rets import RetsHttpClient
# from libs.rets.http.parsers import parse_search
# from libs.settings import *
#
# environ.setdefault('DJANGO_SETTINGS_MODULE', 'web_app.settings')
# django.setup()
#
# from web_app.models import *
#
#
# def fetch_properties(queue):
#
#     rets_session = RetsHttpClient(
#         login_url=login_url,
#         username=username,
#         password=password,
#         rets_version='1.7',
#         send_rets_ua_authorization=False
#     )
#
#     rets_session.login()
#
#     print("Logged")
#     with open('/opt/retsmanager/search_active.xml', 'r') as f:
#         data = f.read()
#     result = parse_search(None, data.replace("\\r\\n", ""))
#     # result = rets_session.search(resource='Property', class_='ResidentialProperty', query='(Status=|A)',
#     #                              standard_names=True)
#
#     def _ingest(properties):
#         pass
#
#     print("Fetched %s" % result.count)
#
#     if result.count:
#         chunk_size = 50
#         for i in range(0, result.count, chunk_size):
#             queue.enqueue(_ingest, result.data[i: i + chunk_size])
#
#     return True
#
#
# def ingest_image(listings):
#     rets_session = RetsHttpClient(
#         login_url=login_url,
#         username=username,
#         password=password,
#         rets_version='1.7',
#         send_rets_ua_authorization=False
#     )
#
#     rets_session.login()
#     print("RETS connected")
#     print(listings)
#
#     media = S3Handler(media_dir='media', rets_session=rets_session)
#     # media.download_photos(listings, {})
#     for listing in listings:
#         print(listing)
#         print("done")
#
#
# def ingest_properties(queue):
#
#
#
#     # Location(
#     #     listing=listing,
#     #     fronting_on=property[''],
#     #     full_address=property[''],
#     #     street_name=property[''],
#     #     street_number=property[''],
#     #     street_abbrev=property[''],
#     #     street_direction=property[''],
#     #     apt_num=property[''],
#     #     province=property[''],
#     #     postal_code=property[''],
#     #     area=property[''],
#     #     municipality=property[''],
#     #     community=property[''],
#     #     district=property[''],
#     # ).save()
#     #
#     # Building(
#     #     listing=listing,
#     #     linked=property[''],
#     #     bathrooms=property[''],
#     #     bathrooms_plus=property[''],
#     #     bedrooms=property[''],
#     #     bedrooms_plus=property[''],
#     #     kitchens=property[''],
#     #     kitchens_plus=property[''],
#     #     washrooms=property[''],
#     #     washrooms_plus=property[''],
#     #     style=property[''],
#     #     approx_age=property[''],
#     #     square_ft=property[''],
#     #     garage_type=property[''],
#     #     garage_spaces=property[''],
#     #     parking_spaces=property[''],
#     # ).save()
#     #
#     # Land(
#     #     listing=listing,
#     #     acreage=property[''],
#     #     access_type=property[''],
#     #     zoning=property[''],
#     #     lot_depth=property[''],
#     #     lot_length=property['']
#     # ).save()
#     #
#     # for j in range(1, 12):
#     #     if property['Rooms%s' % j]:
#     #         pass
#     #
#     #     Room(
#     #         listing=listing,
#     #         level=property[''],
#     #         width=property[''],
#     #         length=property[''],
#     #         features=property[''],
#     #     )
#     #
#     # for j in range(1, 5):
#     #     if property['Washrooms%s' % j]:
#     #         pass
#     #
#     #     Washroom(
#     #         listing=listing,
#     #         level=property[''],
#     #         pieces=property['']
#     #     )
