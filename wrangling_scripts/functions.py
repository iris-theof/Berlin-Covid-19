def label_season (month_row, year_row):
    '''
    It maps the entries of a row that contains months to seasons
    INPUT 
    Numbers from 1-12 that correspond to months
    '''
    if (month_row == 3 or month_row == 4 or month_row == 5) and (year_row == 2020) :
              return 'Frühling '+str( )+"'20"
    if (month_row == 3 or month_row == 4 or month_row == 5) and (year_row == 2021) :
              return 'Frühling '+str( )+"'21"    
    if (month_row == 6 or month_row == 7 or month_row == 8) and (year_row == 2020) :
              return 'Sommer '+str( )+"'20"
    if (month_row == 6 or month_row == 7 or month_row == 8) and (year_row == 2021) :
              return 'Sommer '+str( )+"'21"
    if (month_row == 9 or month_row == 10 or month_row == 11) and (year_row == 2020):
              return 'Herbst '+str( )+"'20"
    if (month_row == 9 or month_row == 10 or month_row == 11) and (year_row == 2021):
              return 'Herbst '+str( )+"'21"
    if (month_row == 12) and (year_row == 2020):
              return 'Winter '+str( )+"'20"+'-'+"'21"
    if (month_row == 1 or month_row == 2) and (year_row == 2021):
              return 'Winter '+str( )+"'20"+'-'+"'21"
    if (month_row == 12) and (year_row == 2021):
              return 'Winter '+str( )+"'21"+'-'+"'22"
    if (month_row == 1 or month_row == 2) and (year_row == 2022):
              return 'Winter '+str( )+"'21"+'-'+"'22"
        