
def number_of_tweets_per_day(df):
    """
    Returns the number of tweets that were posted per day.

    Args:
        df (dataframe): Dataframe containing atleast a "Date" column and "Tweets"
                        column.

    Returns:
        (dataframe): Dataframe grouped by day, with the number of tweets for
                     that day.

    Examples:
        >>> number_of_tweets_per_day(Twitter_dataframe)

        Date
        2019-11-20	18
        2019-11-21	11
        2019-11-22	25
        2019-11-23	19
        2019-11-24	14
        2019-11-25	20
        2019-11-26	32
        2019-11-27	13
        2019-11-28	32
        2019-11-29	16

    """
    #Extract the 'Date' column from the input twitter dataframe
    twitter_df['Date'] = twitter_df['Date'].str[:10]
    #Group by date and count the number of tweets per date
    df_out = twitter_df.groupby('Date').count()
    #Return dataframe containing the date and number of tweets per day
    return df_out
