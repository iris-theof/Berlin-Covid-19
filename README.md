# Link to Webapp [#](#)
`https://berlin-covid-webapp.herokuapp.com/`

# Covid-19 Berlin Data Dashboard 

This is a flask app that visualizes data from the city of Berlin Open Data,
on the registered incidents of Covid-19 in different districts according to date.
A line plot is included where the total number of Covid-19 incidents according
to neighboorhood grouped into seasons are dislplayed. The second graph is a bar
plot with the total number of Covid-19 incidents. The available data are for the
period 03.03.20 - now. Everytime the web-app is loaded new data are loaded from
the city of Berlin Open Data via API from the following url 
`https://www.berlin.de/lageso/gesundheit/infektionsepidemiologie-infektionsschutz/corona/tabelle-bezirke-gesamtuebersicht/index.php/index/all.json?q=`.

## Prerequisites

To install the flask app, you need:
- python3
- python packages in the requirements.txt file
 
 Install the packages with
``` 
 pip install -r requirements.txt
```

## Installing

On a MacOS/linux system, installation is easy. Open a terminal, and go into 
the directory with the flask app files. Run `python myapp.py` in the terminal.
