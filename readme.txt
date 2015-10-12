====================================================
Documentatie conversie Haaglanden database naar JSON
====================================================

Inleiding
=========
Voor de DBK Voertuigviewer is data nodig in json-formaat. De Veiligheidsregio Haaglanden beheert haar data in ArcGIS. De data uit ArcGIS wordt via shapefiles geconverteerd naar json.
Voor het uitvoeren van de conversie is een python-script geschreven door ARIS B.V.
In dit document wordt de conversie beknopt beschreven.

Componenten en benodigdheden
============================
De conversie vereist de volgende benodigdheden.

Componenten:
- Python 3.4.3 (https://www.python.org)
- Python Package Shapely 1.5.9 (https://pypi.python.org/pypi/Shapely)

Python-scripts (ARIS):
- DBKshape2json.py
- DBKDomeinen.py
- DBKError.py
- DBKGlobals.py
- DBKProperties.py
- DBKUtils.py
- shapfile.py

Installatie
===========
Installeer Python 3.4.3 en de package Shapely 1.5.9.

Zet de python-scripts van ARIS op de gewenste locatie.

Aansturing script
=================
Het hoofdscript is DBKshape2json.py.

Aansturing
> Python.exe <scriptdir>\DBKshape2json.py <shapefileLocation> <dbkfeaturesOutputLocation> <dbkobjectOutputLocation> {logFilename}

Parameters
=========================================================================
Parameter                 Omschrijving                          Verplicht
=========================================================================
shapefileLocation         Locatie van shapefiles                verplicht
dbkfeaturesOutputLocation Locatie van uitvoer DBKFeaturesfile   verplicht
dbkobjectOutputLocation   Locatie van uitvoer DBKObjectenfiles  verplicht
logFilename               Locatie en naam van logfile           optioneel

Contact
=======
ARIS B.V.
Tel: 030-2769180
Email: anke.keuren@aris.nl of eddy.scheper@aris.nl



