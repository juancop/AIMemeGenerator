TRACK_WORDS = ['covid']
TABLE_NAME = "downloaded_tweets.csv"
TABLE_COLUMNS = ["id_str", "created_at" , "text" , \
            "polarity" , "subjectivity" , "user_created_at" , "user_location" , \
            "user_description" , "user_followers_count" , "longitude" , "latitude" , \
            "retweet_count" , "favorite_count"]
TABLE_DTYPES  = [object, str ,str, float , float , str , str , str , int , float , float , int , int]