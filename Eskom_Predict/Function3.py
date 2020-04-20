def date_parser(list_dates):
    """
    From datetime strings, return only the date in 'yyyy-mm-dd' format.

    Args:
        list_dates (list): List of datetime strings

    Returns:
        (list) : Extract only the date of each item in the input list
                 and return in 'yyyy-mm-dd' format

    Examples:
        >>> date_parser(['2019-11-29 12:50:54',
                        '2019-11-29 12:46:53',
                        '2019-11-29 12:46:10'])

        ['2019-11-29',
         '2019-11-29',
         '2019-11-29']

    """
    #Remove the dates in the format 'yyyy-mm-dd' from the given list
    dates_only = list(map(lambda x : x[:10] ,list_dates))
    #Return the list containing only the dates
    return dates_only
