def change_date_format(dates):
    formatted_dates = list()
    for date in dates:
        #When date contains / and year comes first
        if '/' in date[4] and '/' in date[7] and len(date) == 10:
            year = date[:4]
            month = date[5:7]
            day = date[8:]
            date = year + month + day
            formatted_dates.append(date)
        #When date contains / and date comes first
        elif '/' in date[2] and '/' in date[5] and len(date) == 10:
            year = date[6:]
            month = date[3:5]
            day = date[:2]
            date = year + month + day
            formatted_dates.append(date)
        #When date contains only '-'
        elif '-' in date[2] and '-' in date[5] and len(date) == 10:
            year = date[6:]
            day = date[3:5]
            month = date[:2]
            date = year + month + day
            formatted_dates.append(date)
            
    return formatted_dates

dates = change_date_format(["2010/03/30", "15/12/2016", "11-15-2012", "20130720",
                           "201-33-44123"])
print(*dates, sep='\n')