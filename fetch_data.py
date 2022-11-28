# from app_store.app_store_reviews_reader import AppStoreReviewsReader
# from google_play_scraper import Sort, reviews_all
# import pycountry
# import pandas as pd



### SETUP ###
# loc_path=""
# her_path="dashboard/"
# path=her_path


def get_data():
    x = "hi"
    # top_countries=["es","br","us","co","de", "fr","gn","it","nl","pt"]
    # df=pd.DataFrame()
    # for lan in top_countries:
    #     result_temp = reviews_all(
    #     'meditofoundation.medito',
    #     sleep_milliseconds=0, # defaults to 0
    #     lang=lan,
    #     sort=Sort.MOST_RELEVANT) # defaults to Sort.MOST_RELEVANT
    #     #defaults to None(means all score))
    #     df_temp=pd.DataFrame(result_temp)
    #     df=pd.concat([df,df_temp])
    # df=df.drop_duplicates(["userName","content"])
    # df=df.rename(columns={"score":"Star Rating", "at":"Review Submit Date and Time","content":"Review Text", "reviewCreatedVersion":"App Version Name"})
    # ## appstore
    # ccodes = [country.alpha_2.lower() for country in pycountry.countries]
    # ccodes = list(ccodes)
    # reader_list = []
    # for i in ccodes:
    #     try:
    #         reader = AppStoreReviewsReader(app_id="1500780518", country=i, timeout=120.0)
    #         reader_list.append(reader.fetch_reviews())
    #     except (RuntimeError, AttributeError):
    #         pass

    # reviews_list=[]
    # for x in reader_list:
    #     if len(x)>0:
    #         reviews_list= reviews_list+x
    # data=pd.DataFrame(reviews_list)
    # data_apple =data.rename(columns={"version":"App Version Name","rating": "Star Rating", "title":"Review Title","content": "Review Text","date":"Review Submit Date and Time"})[["App Version Name","Star Rating","Review Title","Review Text", "country", "Review Submit Date and Time", "id"]]
    # data = pd.concat([data_apple, df])
    return(x)
# data.to_csv(path+"data.csv")