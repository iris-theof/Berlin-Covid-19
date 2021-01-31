import pandas as pd
import plotly.graph_objs as go
from  wrangling_scripts.functions import *

# Path to csv file
file_path = "data/all.csv"
df_berlin = pd.read_csv(file_path, sep = ';')
# Data downloaded from
#https://daten.berlin.de/datensaetze/covid-19-berlin-verteilung-den-bezirken-gesamt%C3%BCbersicht

df =pd.read_csv(file_path) 

# Export from the columns of the dataframe then names of the different neighboorhoods
list_berzik= list(df_berlin.columns) 
list_berzik.remove('id')
list_berzik.remove('datum')

# Convert 'datum' column to datetime 
datetime_t = pd.to_datetime(df_berlin.loc[:,'datum'])

# Create three additional columns with the Year, Month and the Weekday

df_berlin['Jahr'] = datetime_t.dt.year
df_berlin['Monat'] = datetime_t.dt.month
df_berlin['Wochentag'] = datetime_t.dt.weekday

# Now that all the useful information has been exported from column 'datum' we can remove it
df_berlin.drop(['datum'], axis=1, inplace = True)

#melt all the neighboorhoods in one column
df_berlin_melt = pd.melt(df_berlin, id_vars=['id','Jahr','Monat','Wochentag'],
                 value_vars=list_berzik, var_name='Berzik', value_name='COVID_Erkrankungen')

# Create didctionary of neighboorhood shortcuts in the dataframe and full names
dict_berzik = dict([('charlottenburg_wilmersdorf', 'Charlottenburg - Wilmersdorf'), 
                    ('friedrichshain_kreuzberg', 'Friedrichshain - Kreuzberg'), ('lichtenberg', 'Lichtenberg'),
                   ('marzahn_hellersdorf', 'Marzahn - Hellersdorf'),('mitte', 'Mitte'), ('neukoelln', 'Neukoelln'),
                   ('pankow','Pankow'),('reinickendorf','Reinickendorf'),('spandau','Spandau'),
                    ('steglitz_zehlendorf','Steglitz - Zehlendorf'),('tempelhof_schoeneberg','Tempelhof - Schoeneberg'),
                    ('treptow_koepenick','Treptow - Koepenick') ])

# Replace neighboorhood names with the values from the dictionary
df_berlin_melt = df_berlin_melt.replace({'Berzik': dict_berzik})
# Create new list with neighboorhood names which would contain the full names from the dictionary
berzik_list = df_berlin_melt.Berzik.unique().tolist()

# Create a data series where the sum of all 'Covid-19 Erkrankungen' in every neighborhood is shown
df_berlin_berzik = df_berlin_melt.groupby('Berzik')['COVID_Erkrankungen'].sum().reset_index(name='COVID_Erkrankungen_sum')

# Add to df_berlin_melt dataframe a new column which would correspond to the season        
df_berlin_melt['Saison'] = df_berlin_melt['Monat'].apply (lambda row: label_season(row))   

# Create a new dataframe which would contain the sum of 'Covid Erkranunkungen' for every season at each Neighboorhood
df_berlin_berzik_saison = df_berlin_melt.groupby(['Saison','Berzik'])['COVID_Erkrankungen'].sum().reset_index(name='COVID_Erkrankungen_Saison_sum')

df_berlin_berzik_saison.Saison = pd.Categorical(df_berlin_berzik_saison.Saison, 
                      categories=["Frühling","Sommer","Herbst","Winter"],
                      ordered=True)
df_berlin_berzik_saison.sort_values('Saison', inplace=True)



def return_figures():
    """Creates four plotly visualizations

    Args:
        None

    Returns:
        list (dict): list containing the four plotly visualizations

    """

  
  # filter and sort values for the visualization
  # needs to be added  

    graph_one = [] 
    
    for berzik in berzik_list:
         x_val = df_berlin_berzik_saison[df_berlin_berzik_saison['Berzik'] == berzik].Saison.tolist()
         y_val = df_berlin_berzik_saison[df_berlin_berzik_saison['Berzik'] == berzik].COVID_Erkrankungen_Saison_sum.tolist()
         graph_one.append(
             go.Scatter(
             x=x_val,
             y=y_val,
             mode='lines',
             name=berzik,
        )
    )
    


    layout_one = dict(title = '<b>COVID-19 Erkrankungen nach Jahreszeit (März 2020 bis Januar 2021)</b>',
                xaxis = dict(title = '', linewidth = 2, tickfont = dict(
                             size = 20,
                             color = 'black'
                              )),
                yaxis = dict(title = '<b>Covid-19 Erkrankungen</b>',   
                             linewidth = 2, tickfont = dict(
                             size = 18,
                             color = 'black'
                              )), 
                              font=dict(size=16),
                              textfont_size=18 )

# second chart plots ararble land for 2015 as a bar chart    
    graph_two = []

    graph_two.append(
      go.Bar(
      x = df_berlin_berzik['Berzik'],
      y = df_berlin_berzik['COVID_Erkrankungen_sum']
      )
    )

    layout_two = dict(title = '<b>Gesamt COVID-19 Erkrankungen nach Berzik</b>',
                xaxis = dict(title = '', linewidth = 2, tickfont = dict(
                size = 20,
                color = 'black'
                 )),
                yaxis = dict(title = '', linewidth = 2,  tickfont = dict(
                size = 18,
                color = 'black'
                 )),
                font=dict(size=16)     
                )
    
    # append all charts to the figures list
    figures = []
    figures.append(dict(data=graph_one, layout=layout_one))
    figures.append(dict(data=graph_two, layout=layout_two))

    return figures