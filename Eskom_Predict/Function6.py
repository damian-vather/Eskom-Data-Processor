def word_splitter(df):
    """
    Tokenizing a tweet.

    A function which splits the sentences (of the tweet) in a dataframe's
    column into a list of the separate (lowercase) words.

    Args:
        df (dataframe): pandas dataframe with tweets

    Returns:
        dataframe: returns a modified dataframe that includes a new column
                   that contains the tokenized tweets (in lowercase).

    Examples:
        >>> word_splitter(twitter_df.copy())


        Tweets	                                                Date	        Split Tweets
    0	@BongaDlulane Please send an email to mediades...	    2019-11-29	    [@bongadlulane, please, send, an, email, to, m...
    1	@saucy_mamiie Pls log a call on 0860037566	            2019-11-29	    [@saucy_mamiie, pls, log, a, call, on, 0860037...
    2	@BongaDlulane Query escalated to media desk.	        2019-11-29	    [@bongadlulane, query, escalated, to, media, d...
    3	Before leaving the office this afternoon, head...       2019-11-29    	[before, leaving, the, office, this, afternoon...
    4	#ESKOMFREESTATE #MEDIASTATEMENT : ESKOM SUSPEN...	    2019-11-29	    [#eskomfreestate, #mediastatement, :, eskom, s...

    """

    #Tokenize lowercase tweets
    df['Split Tweets'] = df['Tweets'].str.lower().str.split()
    #Return modified dataframe
    return df
