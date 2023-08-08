# import django
# from datetime import timedelta
# from os import environ
# from airflow import DAG
# from airflow.models import TaskInstance
# from airflow.models.baseoperator import chain
# from airflow.models.dag import dag
# from airflow.operators.python import PythonOperator, task
# from datetime import datetime
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
# default_args = {
#     'owner': 'airflow',
#     'depends_on_past': False,
#     'email': ['airflow@example.com'],
#     'email_on_failure': False,
#     'email_on_retry': False,
#     'retries': 0,
#     'start_date': datetime(2023, 8, 4)
# }
#
#
# def retsClient(account_type: str = None):
#     rets_session = RetsHttpClient(
#         login_url=login_url,
#         username=username_all if account_type == "all" else username,
#         password=password,
#         rets_version='1.7',
#         send_rets_ua_authorization=False
#     )
#
#     rets_session.login()
#     return rets_session
#
#
# #
# # def get_updates():
# #     with open('../search_active.xml', 'r') as f:
# #         data = f.read()
# #     result = parse_search(None, data.replace("\\r\\n", ""))
# #     # result = rets_session.search(resource='Property', class_='ResidentialProperty', query='(Status=|A)',
# #     #                              standard_names=True)
# #
# #     def _ingest():
# #         pass
# #
# #     print("Fetched %s" % result.count)
# #
# #     if result.count:
# #         chunk_size = 50
# #         for j in range(0, result.count, chunk_size):
# #             print("queueing %s %s" % (j, j + chunk_size))
# #             queue.enqueue('_ingest', result.data[j: j + chunk_size])
# #
# #     return True
#
# @dag(
#     schedule=timedelta(hours=1),
#     catchup=False,
#     tags=["example"],
#     start_date=datetime(2021, 1, 1),
# )
# def idx_updates():
#     @task()
#     def update_db():
#         rets = retsClient()
#         try:
#             with open('../search_active.xml', 'r') as f:
#                 data = f.read()
#             result = parse_search(None, data.replace("\\r\\n", ""))
#             # result = rets.search(
#             #     resource='Property', class_='ResidentialProperty',
#             #     query='(Status=|A)', standard_names=True)
#         except Exception as e:
#             print("get_all_update: search failed (%s)" % e)
#             return False
#
#         print("get_all_update: fetched %s" % result.count)
#
#         try:
#             for listing in result.data:
#                 # listing_object = update_or_insert(listing)
#                 # print("Insert or updated %s %s" % (listing['MLS'], listing_object.id))
#                 print("Insert or updated %s %s" % (listing['MLS'], 1))
#         except Exception as e:
#             rets.dump()
#             print("get_all_update: insert failed (%s)" % e)
#             return False
#
#         return True
#
#     update_db()
#
#
# @dag(
#     schedule=None,
#     catchup=False,
#     tags=["example"],
#     start_date=datetime(2021, 1, 1),
# )
# def idx_active():
#     # with open('../search_active.xml', 'r') as f:
#     #     data = f.read()
#     # result = parse_search(None, data.replace("\\r\\n", ""))
#     rets = retsClient(account_type='all')
#     try:
#         result = rets.search(
#             resource='Property', class_='ResidentialProperty',
#             query='(Status=|A)', standard_names=True, parse_format='active')
#     except Exception as e:
#         print("get_all_active: search failed (%s)" % e)
#         return False
#
#     print("get_all_active: fetched %s" % result.count)
#
#     try:
#         for listing in result.data:
#             db_listing = Listing.objects.filter(mls__exact=listing["MLS"]).first()
#             if not db_listing:
#                 print("update_all_active: %s not found in database" % listing["MLS"])
#                 continue
#
#             db_listing.status = listing['Status']
#             db_listing.save()
#
#             print("Update states fos %s" % listing['MLS'])
#     except Exception as e:
#         rets.dump()
#         print("get_all_active: insert failed (%s)" % e)
#         return False
#
#     return True
#
#     # @task()
#     # def update_images():
#     #     rets = retsClient()
#     #     media = S3Handler(media_dir='media', rets_session=rets)
#     #     listings = Listing.objects.filter(media_updated=True)
#     #     failed_objects = {}
#     #     for listing in listings:
#     #         Photo.objects.filter(listing=listing).delete()
#     #
#     #         images = media.get_photos(listing.mls, failed_objects)
#     #         print("downloading image %s %s" % (listing.mls, listing.id))
#     #
#     #         for image_key in images.keys():
#     #             Photo(
#     #                 listing=listing,
#     #                 sequence=image_key,
#     #                 path=images[image_key],
#     #                 mime_type='image/jpeg'
#     #             ).save()
#     #
#     #         listing.media_updated = False
#     #         listing.save()
#     #
#     #         print("Listing updated %s" % listing.mls)
#     #
#     #
#     # def update_or_insert(listing):
#     #     db_listing = Listing.objects.filter(mls__exact=listing['MLS']).first()
#     #     if db_listing:
#     #         Room.objects.filter(listing_id=db_listing.id).delete()
#     #         Washroom.objects.filter(listing_id=db_listing.id).delete()
#     #
#     #     listing_object = Listing(
#     #         id=db_listing.id if db_listing else None,
#     #         source=Source(id=1),
#     #         type=listing['SaleLease'],
#     #         # created_at=listing[''],
#     #         # last_updated=listing[''],
#     #         mls=listing['MLS'],
#     #         status=listing['Status'],
#     #         price=listing['ListPrice'],
#     #         description=listing['RemarksForClients'],
#     #         extra_description=listing['Extras'],
#     #         possession_notes=listing['PossessionRemarks'],
#     #         media_updated_at=listing['PixUpdtedDt']
#     #     )
#     #
#     #     if db_listing and listing['PixUpdtedDt'] != db_listing.media_updated_at:
#     #         listing_object.media_updated_at = listing['PixUpdtedDt']
#     #         listing_object.media_updated = True
#     #
#     #     listing_object.save()
#     #
#     #     Agent(
#     #         id=db_listing.agent.id if db_listing else None,
#     #         listing=listing_object,
#     #         brokerage=listing['ListBrokerage'],
#     #         # name=listing['']
#     #     ).save()
#     #
#     #     Location(
#     #         id=db_listing.location.id if db_listing else None,
#     #         listing=listing_object,
#     #         fronting_on=listing['FrontingOnNSEW'],
#     #         # full_address=listing[''],
#     #         street_name=listing['StreetName'],
#     #         street_number=listing['Street'],
#     #         street_abbrev=listing['StreetAbbreviation'],
#     #         street_direction=listing['StreetDirection'],
#     #         apt_num=listing['AptUnit'],
#     #         province=listing['Province'],
#     #         postal_code=listing['PostalCode'],
#     #         area=listing['Area'],
#     #         municipality=listing['Municipality'],
#     #         community=listing['Community'],
#     #         district=listing['MunicipalityDistrict'],
#     #     ).save()
#     #
#     #     Building(
#     #         id=db_listing.building.id if db_listing else None,
#     #         listing=listing_object,
#     #         linked=listing['Link'] == 'Y',
#     #         # bathrooms=listing['Washrooms'],
#     #         # bathrooms_plus=listing['Washrooms'],
#     #         bedrooms=int(listing['Bedrooms']) if listing['Bedrooms'] else None,
#     #         bedrooms_plus=int(listing['BedroomsPlus']) if listing['BedroomsPlus'] else None,
#     #         kitchens=int(listing['Kitchens']) if listing['Kitchens'] else None,
#     #         kitchens_plus=int(listing['KitchensPlus']) if listing['KitchensPlus'] else None,
#     #         washrooms=int(listing['Washrooms']) if listing['Washrooms'] else None,
#     #         # washrooms_plus=listing[''],
#     #         style=listing['Style'],
#     #         approx_age=listing['ApproxAge'],
#     #         square_ft=listing['ApproxSquareFootage'],
#     #         garage_type=listing['GarageType'],
#     #         garage_spaces=listing['GarageSpaces'],
#     #         parking_spaces=listing['TotalParkingSpaces']
#     #     ).save()
#     #
#     #     Land(
#     #         id=db_listing.land.id if db_listing else None,
#     #         listing=listing_object,
#     #         acreage=listing['Acreage'],
#     #         access_type=list(filter(None, [listing['AccessToProperty1'], listing['AccessToProperty2']])),
#     #         zoning=listing['Zoning'],
#     #         lot_depth=listing['LotDepth'],
#     #         lot_length=listing['LotFront']
#     #     ).save()
#     #
#     #     for index in range(1, 12):
#     #         if not listing['Room%s' % index]:
#     #             continue
#     #
#     #         Room(
#     #             listing=listing_object,
#     #             sequence=index,
#     #             level=listing['Level%s' % index],
#     #             width=listing['Room%sWidth' % index],
#     #             length=listing['Room%sLength' % index],
#     #             features=list(filter(None, [listing['Room%sDesc1' % index],listing['Room%sDesc2' % index],listing['Room%sDesc3' % index]])),
#     #         ).save()
#     #
#     #     for washroom_index in range(1, 5):
#     #         if not listing['WashroomsType%s' % washroom_index]:
#     #             continue
#     #
#     #         Washroom(
#     #             listing=listing_object,
#     #             sequence=washroom_index,
#     #             level=listing['WashroomsType%sLevel' % washroom_index],
#     #             pieces=listing['WashroomsType%sPcs' % washroom_index]
#     #         ).save()
#     #
#     #     return listing_object
#     #
#     #
#     # update()
#
#
# idx_updates()
# idx_active()
