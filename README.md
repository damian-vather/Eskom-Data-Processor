# Eskom_Predict Package
This package contains python functions used to analyse data from Eskom. These functions process both numerical and text data.

## What you will need
This project runs on the latest version of Python. Before you can start, ensure that the latest version of python is installed.  

## Installing the project package from GitHub
 Issue this command to install from GitHub:  

 `pip install git+https://github.com/Xenaschke/Eskom_Predict.git`

 If you need to install the latest version of this package, use:  

 `pip install --upgrade git+https://github.com/Xenaschke/Eskom_Predict.git`  

## Prerequisites for package functionality  
This package requires numpy to be installed. Issue these commands in your notebook to install and import numpy library:  

```
pip install numpy  
import numpy as np  
```

## Import the project package
 Issue this command to import the package:  

 `from Eskom_Predict import master`  

## Running the codes
Once the package is installed into python the following functions can be used to get the metrics:

## dictionary_of_metrics(items)  
The function takes in a list of integers and returns a dictionary containing the mean, median, variance, standard deviation,
minimum and maximum of the list of items.
#### Example
An argument:  
` items = [39660.0, 36024.0, 32127.0, 39488.0, 18422.0, 23532.0, 8842.0, 37416.0, 16156.0, 18730.0, 19261.0, 25275.0] `

Returns:

` {'mean': 26244.42, 'median': 24403.5, 'var': 108160153.17, 'std': 10400.01, 'min': 8842.0, 'max': 39660.0} `

## five_num_summary(items)
For this function, you must first import the numpy package. The function takes in a list of integers and returns a dictionary of a five-number summary containing: max, median, min, Q1 and Q3.
#### Example
An argument:  
` items = [3,5,6,78,8,9,9,6,4,6.8,7,8,9,1] `

Returns:

` {'max': 78.0, 'median': 6.9, 'min': 1.0, 'q1': 5.25, 'q3': 8.75} `  

## date_parser(list_dates)  
This function takes in a list of datetime strings, extracts the dates of each item in the list, and returns the date in 'yyyy-mm-dd' format.
#### Example
An argument:  
` list_dates = ['2019-11-29 12:50:54','2019-11-29 12:46:53''2019-11-29 12:46:10'] `

Returns:

` ['2019-11-29', '2019-11-29', '2019-11-29'] `  

## extract_municipality_hashtags(df)
This function takes a pandas dataframe of tweets and returns a modified dataframe that includes two new columns containing information about the municipality and the tweet hashtag (in lowercase).
#### Example  
An argument:  
df =  

| | Tweets | Date |  
|---|---|---|
| 0 | @BongaDlulane Please send an email to mediades... | 2019-11-29 12:50:54 |  
| 1 | @saucy_mamiie Pls log a call on 0860037566 | 2019-11-29 12:46:53 |     
| 2 |	@BongaDlulane Query escalated to media desk.	    |   2019-11-29 12:46:10  |  
| 3 |	Before leaving the office this afternoon, head... | 	2019-11-29 12:33:36  |                               
| 4 |	#ESKOMFREESTATE #MEDIASTATEMENT : ESKOM SUSPEN...	 |  2019-11-29 12:17:43  |        

Returns:

| | Tweets	 |                                           Date    |     	        municipality  |   	hashtags |
|---|----|----|----|---|
| 0	| @BongaDlulane Please send an email to mediades...	|  2019-11-29 12:50:54	| NaN	          |     NaN |
| 1 | 	@saucy_mamiie Pls log a call on 0860037566	       |  2019-11-29 12:46:53	| NaN          |     	NaN |
| 2	| @BongaDlulane Query escalated to media desk.	     |  2019-11-29 12:46:10	| NaN            |   	NaN |
| 3	| Before leaving the office this afternoon, head...	 | 2019-11-29 12:33:36 |	NaN	          |     NaN |
|4	|#ESKOMFREESTATE #MEDIASTATEMENT : ESKOM SUSPEN...	|  2019-11-29 12:17:43	| NaN	            |   [#eskomfreestate, #mediastatement] |
|...|	...	| ... |	... |	...|
| 195	| Eskom's Visitors Centresâ€™ facilities include i | 2019-11-20 10:29:07	| NaN	          |     NaN |
| 196	| #Eskom connected 400 houses and in the process... |	2019-11-20 10:25:20	| NaN	         |      [#eskom, #eskom, #poweringyourworld] |
| 197 |	@ArthurGodbeer Is the power restored as yet?	   |  2019-11-20 10:07:59	| NaN	            |   NaN |
| 198 | 	@MuthambiPaulina @SABCNewsOnline @IOL @eNCA @e... |	2019-11-20 10:07:41	 | NaN            |   	NaN |
| 199	| RT @GP_DHS: The @GautengProvince made a commit... | 	2019-11-20 10:00:09	| NaN	            |   NaN |

## number_of_tweets_per_day(df)
This function takes a dataframe containing at least a "Date" column and "Tweets" column as input. It returns a dataframe grouped by day, with the number of tweets for that day.
#### Example
An argument:  
df=

| | Tweets | Date |  
|---|---|---|
| 0 |	@BongaDlulane Please send an email to mediades...	| 2019-11-29 12:50:54 |
| 1 |	@saucy_mamiie Pls log a call on 0860037566	       | 2019-11-29 12:46:53 |
| 2 |	@BongaDlulane Query escalated to media desk.	     | 2019-11-29 12:46:10 |
| 3 |	Before leaving the office this afternoon, head... |	2019-11-29 12:33:36 |
| 4 |	#ESKOMFREESTATE #MEDIASTATEMENT : ESKOM SUSPEN...	| 2019-11-29 12:17:43 |  

Returns:  

|Date|	       Tweets|
|---|---|
| 2019-11-20	 | 18 |
| 2019-11-21	 | 11 |
| 2019-11-22	 | 25 |
| 2019-11-23	 | 19 |
| 2019-11-24	 | 14 |
| 2019-11-25	 |  20 |
| 2019-11-26  |	32 |
| 2019-11-27  |	13 |
| 2019-11-28  |	32 |
| 2019-11-29	 | 16 |   

## word_splitter(df)
This function takes a pandas dataframe with tweets as input. It returns a modified dataframe that includes a new column that contains the tokenized tweets (in lowercase).
#### Example
An argument:  
df   =               
||Tweets|                                                  Date|
|---|---|---|
|0|	@BongaDlulane Please send an email to mediades...	| 2019-11-29 12:50:54|
|1	|@saucy_mamiie Pls log a call on 0860037566	        |2019-11-29 12:46:53|
|2	|@BongaDlulane Query escalated to media desk.	      |2019-11-29 12:46:10|
|3	|Before leaving the office this afternoon, head... 	|2019-11-29 12:33:36|
|4	|#ESKOMFREESTATE #MEDIASTATEMENT : ESKOM SUSPEN...	 |2019-11-29 12:17:43|  

Returns:

||Tweets|	                                                Date	   |     Split Tweets|
|--|---|---|---|
| 0 |	@BongaDlulane Please send an email to mediades...	 |   2019-11-29	  |   [@bongadlulane, please, send, an, email, to, m...|  
|1 |	@saucy_mamiie Pls log a call on 0860037566	       |    2019-11-29	 |    [@saucy_mamiie, pls, log, a, call, on, 0860037...|  
| 2 |	@BongaDlulane Query escalated to media desk.	      |   2019-11-29	  |   [@bongadlulane, query, escalated, to, media, d...|  
| 3	| Before leaving the office this afternoon, head...   |  2019-11-29    |	 [before, leaving, the, office, this, afternoon...|  
| 4	| #ESKOMFREESTATE #MEDIASTATEMENT : ESKOM SUSPEN...	   | 2019-11-29	    | [#eskomfreestate, #mediastatement, :, eskom, s...      |

## stop_words_remover(df)
This function takes a dataframe containing at least a "Date" column and "Tweets" column as input. It returns a modified dataframe containing a column where English stop words are removed from a tokenised tweet.
#### Example  
An argument:  
df =                    
||Tweets|                                               Date|
|--|--|--|
|0|	@BongaDlulane Please send an email to mediades...	| 2019-11-29 12:50:54|
|1|	@saucy_mamiie Pls log a call on 0860037566	        |2019-11-29 12:46:53|
|2	|@BongaDlulane Query escalated to media desk.	     | 2019-11-29 12:46:10|
|3	|Before leaving the office this afternoon, head... |	2019-11-29 12:33:36|
|4	|#ESKOMFREESTATE #MEDIASTATEMENT : ESKOM SUSPEN...	 |2019-11-29 12:17:43|  

Returns:  

||Tweets	|                                    Date	      |          Without Stop Words|
|--|--|--|--|
| 0	|@BongaDlulane Please send...	   |    2019-11-29 12:50:54	  | [@bongadlulane, send, email, ...  |
| 1	|@saucy_mamiie Pls log...	        |   2019-11-29 12:46:53	  | [@saucy_mamiie, pls, log, ...  |
|2	|@BongaDlulane Query...	           |  2019-11-29 12:46:10	  | [@bongadlulane, query, ...  |
|3	|Before leaving the office...	      | 2019-11-29 12:33:36	  | [leaving, office, ...  |
|4|	#ESKOMFREESTATE #MEDIASTATEMENT... | 2019-11-29 12:17:43	  | [#eskomfreestate, #mediastatement, ... |

## Acquire the data used in our examples  
Issue these commands in your notebook to acquire the data that was used in this file's examples:  

```
import pandas as pd  

# Electricification by province (EBP) data  
ebp_url = 'https://raw.githubusercontent.com/Explore-AI/Public-Data/master/Data/electrification_by_province.csv'  
ebp_df = pd.read_csv(ebp_url)  

for col, row in ebp_df.iloc[:,1:].iteritems():  
    ebp_df[col] = ebp_df[col].str.replace(',','').astype(int)  

ebp_df.head()  

#Twitter data  
twitter_url = 'https://raw.githubusercontent.com/Explore-AI/Public-Data/master/Data/twitter_nov_2019.csv'  
twitter_df = pd.read_csv(twitter_url)  
twitter_df.head()  

# gauteng ebp data as a list  
gauteng = ebp_df['Gauteng'].astype(float).to_list()  

# dates for twitter tweets  
dates = twitter_df['Date'].to_list()
 ```

## How to contribute to the project
To contribute to this repository, one needs to email the owners of this repository before making any changes.  

For pull request process: Update the README.md with details of changes to the interface.
                          You may merge the Pull Request in once you have the sign-off of the developers.

## Authors
Abdullah Shaikh  
Kolobe Rufus Seopa  
Tshegofatjo Makhafola  
Vahiel Moodley  
Xenaschke Croucamp  

## Acknowledgements
Damian Vather for his assistance.
