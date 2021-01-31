def label_season (row):
    '''
    It maps the entries of a row that contains months to seasons
    INPUT 
    Numbers from 1-12 that correspond to months
    '''
    if (row == 3 or row == 4 or row == 5) :
              return 'Frühling'
    if (row == 6 or row == 7 or row == 8) :
              return 'Sommer'
    if (row == 9 or row == 10 or row == 11) :
              return 'Herbst'
    if (row == 12 or row == 1 or row == 2) :
              return 'Winter'