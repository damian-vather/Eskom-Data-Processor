# dictionary_of_metrics(items) function test cases
dictionary_of_metrics([1,1,1,1,1,2]) == {'mean': 1.17,
                                         'median': 1.0,
                                         'var': 0.17,
                                         'std': 0.41,
                                         'min': 1,
                                         'max': 2}

dictionary_of_metrics([200,254,263,255,223,295,224,254,236]) == {'mean': 244.89,
                                                                 'median': 254,
                                                                 'var': 764.61,
                                                                 'std': 27.65,
                                                                 'min': 200,
                                                                 'max': 295}



# five_num_summary(items) function test cases
five_num_summary([1,1,1,1,1,2]) == {'max': 2,
                                    'median': 1.0,
                                    'min': 1,
                                    'q1': 1.0,
                                    'q3': 1.0}

five_num_summary([200,254,263,255,223,295,224,254,236]) == {'max': 295,
                                                            'median': 254.0,
                                                            'min': 200,
                                                            'q1': 224.0,
                                                            'q3': 255.0}



# date_parser(list_dates) function test cases
date_parser(['2019-11-29 12:50:54', '2019-11-29 12:46:53', '2019-11-29 12:46:10']) == ['2019-11-29',
                                                                                       '2019-11-29',
                                                                                       '2019-11-29']

date_parser(['2019-11-27 10:55:14','2019-11-30 12:50:23']) == ['2019-11-27',
                                                               '2019-11-30']



#############################################
 #Twitter data
 import pandas as pd
 
 twitter_url = 'https://raw.githubusercontent.com/Explore-AI/Public-Data/master/Data/twitter_nov_2019.csv'
 twitter_df = pd.read_csv(twitter_url)
 twitter_df.head()
#############################################



# extract_municipality_hashtags(df) function test cases
extract_municipality_hashtags(twitter_df.copy()).loc[4, "hashtags"] == ['#eskomfreestate',
                                                                        '#mediastatement']

extract_municipality_hashtags(twitter_df.copy()).loc[196, "hashtags"] == ['#eskom',
                                                                          '#eskom',
                                                                          '#poweringyourworld']



# number_of_tweets_per_day(df) function test cases
number_of_tweets_per_day(twitter_df.copy()).iloc[0]['Tweets'] == 18

number_of_tweets_per_day(twitter_df.copy()).iloc[8]['Tweets'] == 32



# word_splitter(df) function test cases
word_splitter(twitter_df.copy()).loc[0, "Split Tweets"] == ['@bongadlulane',
                                                            'please',
                                                            'send',
                                                            'an',
                                                            'email',
                                                            'to',
                                                            'mediadesk@eskom.co.za']

word_splitter(twitter_df.copy()).loc[100, "Split Tweets"] == ['#eskomnorthwest',
                                                              '#mediastatement',
                                                              ':',
                                                              'notice',
                                                              'of',
                                                              'supply',
                                                              'interruption',
                                                              'in',
                                                              'lichtenburg',
                                                              'area',
                                                              'https://t.co/7hfwvxllit']



# stop_words_remover(df) function test cases
stop_words_remover(twitter_df.copy()).loc[0, "Without Stop Words"] == ['@bongadlulane',
                                                                       'send',
                                                                       'email',
                                                                       'mediadesk@eskom.co.za']

stop_words_remover(twitter_df.copy()).loc[100, "Without Stop Words"] == ['#eskomnorthwest',
                                                                         '#mediastatement',
                                                                         ':',
                                                                         'notice',
                                                                         'supply',
                                                                         'interruption',
                                                                         'lichtenburg',
                                                                         'area',
                                                                         'https://t.co/7hfwvxllit']
