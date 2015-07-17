#-------------------------------------------------------------------------------
# Name:        DBKTODO
# Purpose:
#
# Author:      Anke Keuren
#
# Created:     17-07-2015
# Copyright:   (c) Administrator 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#TODO:
#DONE Schrijven van DBKFeatures. Centroid kan op basis van DBKObject-polygon worden bepaald of op basis van de panden binnen het DBKOBject.
#                            Waarschijnlijk ook nog de klassen-structuur aanpasssen zodat alles ingelezen wordt vanuit DBKObject en niet vanuit pand???
#DONE Gevaren wegschrijven naar gevaarlijke stoffen.
#DONE Opstelplaats en toegang pand wegschrijven naar brandweervoorziening.
#DONE Slagboom, aanpijling en overige lijnen schrijven naar hulplijn.
#DONE Centroid bij afwijkendebinnendekking
#DONE BrandweervoorzieningProp afleiden van DBKMultiProp (en SamengesteldProp)
#DONE Brandweervoorziening: Omschrijving en bijzonderheid samenvoegen in aanvullendeInformatie.
#OBSOLETE Hulplijn: Aanrijdroute -> Arrow of anders? Uitzonderen van hulplijn als geconverteerd naar toegang terrein!!
#DONE Pandgeometrie Value aanpassen ivm afleiding van DBKMultiProp.
#DONE Verblijf aanpassen: slaapplaatsen.
#DONE Toegang terrein converteren naar brandweervoorziening.
#DONE Aanrijroute converteren naar toegangterrein.
#DONE Adressen implementeren
#DONE Bij lezen shapefile Decode met 'cp1252' want 'latin-1' werkte niet bij shapefiles uit ArcGIS 10.1.
#DONE Logfile schrijven.
#OBSOLETE ?Backup maken van bestaande DBKObjectenfile?
#OBSOLETE Toegang pand, extra vertaalslag voor domein maken.
#DONE Als geen foto of contact, dan geen lijst met alle velden null, maar "foto": null.
#DONE Veldwaarden worden niet naar de goeie elementen geschreven. Iets met fldindexen?
#DONE Nieuwe domeinwaarden toevoegen.
# Symboolgroottes vertalen.
# Opschonen en op github zetten.

#TODO buiten code:
#DONE Melden aan Thierry dat vluchtroute wel in featureclass aanwezig.
#DONE Database met referentie-object naar shapefile exporteren.
# Documentatie schrijven.


def main():
    pass

if __name__ == '__main__':
    main()
