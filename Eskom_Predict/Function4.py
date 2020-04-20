import numpy as np
def extract_municipality_hashtags(df):
    """
    Takes a tweet on electricity and returns the municipality mentioned and any
    hashtags in that tweet.

    A function which takes in a pandas dataframe and returns a modified
    dataframe that includes two new columns that contain information about the
    municipality and hashtag of the tweet, using the municipality dictionary.

    Args:
        df (dataframe): pandas dataframe with tweets

    Returns:
        dataframe: returns a modified dataframe that includes two new columns
                   that contain information about the municipality and hashtag
                   of the tweet (in lowercase).

    Examples:
        >>> extract_municipality_hashtags(twitter_df.copy())

        Tweets	                                                    Date	                municipality	hashtags
    0	@BongaDlulane Please send an email to mediades...	        2019-11-29 12:50:54	    NaN	            NaN
    1	@saucy_mamiie Pls log a call on 0860037566	                2019-11-29 12:46:53	    NaN	            NaN
    2	@BongaDlulane Query escalated to media desk.	            2019-11-29 12:46:10	    NaN	            NaN
    3	Before leaving the office this afternoon, head...	        2019-11-29 12:33:36	    NaN	            NaN
    4	#ESKOMFREESTATE #MEDIASTATEMENT : ESKOM SUSPEN...	        2019-11-29 12:17:43	    NaN	            [#eskomfreestate, #mediastatement]

    """

    mun_dict ={ '@CityofCTAlerts' : 'Cape Town',
                '@CityPowerJhb' : 'Johannesburg',
                '@eThekwiniM' : 'eThekwini' ,
                '@EMMInfo' : 'Ekurhuleni',
                '@centlecutility' : 'Mangaung',
                '@NMBmunicipality' : 'Nelson Mandela Bay',
                '@CityTshwane' : 'Tshwane' }

    #Create two new columns and input default values "NaN"
    df['municipality'] = np.nan
    df['hashtags'] = np.nan

    #Create intermediate dataframe omitting colons from df
    df1 = df['Tweets'].str.replace(':', '')

    for keys,values in mun_dict.items():
        for i in range(200):
            #if key (from dictionary) is found in the tweet, then:
            if keys in df1.str.split()[i]:
                #output corresponding value (from dictionary) into 'municipality' column
                df['municipality'][i] = values

    #extracting all hashtags from tweets and displaying them in 'hashtags' column as lowercase
    df['hashtags'] = list(map(lambda token: [x for x in token if x.startswith('#')], df['Tweets'].str.lower().str.split()))
    for i in range(200):
        #if tweet has no hashtag, then:
        if df['hashtags'][i] == []:
            #output 'NaN'
            df['hashtags'][i] = np.nan
    #return dataframe with new columns
    return df
