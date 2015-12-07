#-------------------------------------------------------------------------------
# Name:        DBKGlobals
# Purpose:
#
# Author:      Anke Keuren (ARIS)
#
# Created:     15-07-2015
# Changes:     20-10-2015, AK:
#              Shapefilenamen in variabelen gezet.
# Copyright:   (c) ARIS B.V. 2015
#-------------------------------------------------------------------------------

global shapefileLocation
global dbkobjectFilename
global dbkfeatureFilename
global dbkobjectOutputLocation
global dbkfeaturesOutputLocation
global logFilename
global writeLog

shpExt = ".shp"

UPPERCASE = False

if UPPERCASE:
    PAND = "PAND" + shpExt
    BRANDWEERVOORZIENING = "BRANDWEERVOORZIENING" + shpExt
    COMPARTIMENTERING = "COMPARTIMENTERING" + shpExt
    OPSTELPLAATS = "OPSTELPLAATS" + shpExt
    TOEGANG_PAND = "TOEGANG PAND" + shpExt
    TOEGANG_TERREIN = "TOEGANG TERREIN" + shpExt
    HELLINGBAAN = "HELLINGBAAN" + shpExt
    GEVAARLIJKE_STOFFEN = "GEVAARLIJKE STOFFEN" + shpExt
    GEVAREN = "GEVAREN" + shpExt
    DBK_LIJN ="DBK LIJN" + shpExt
    SLAGBOOM = "SLAGBOOM" + shpExt
    AANPIJLING = "AANPIJLING" + shpExt
    TEKST = "TEKST" + shpExt
    AANRIJROUTE = "AANRIJROUTE" + shpExt
    DBK_OBJECT ="DBK OBJECT" + shpExt
else:
    PAND = "Pand" + shpExt
    BRANDWEERVOORZIENING = "Brandweervoorziening" + shpExt
    COMPARTIMENTERING = "Compartimentering" + shpExt
    OPSTELPLAATS = "Opstelplaats" + shpExt
    TOEGANG_PAND = "Toegang pand" + shpExt
    TOEGANG_TERREIN = "Toegang terrein" + shpExt
    HELLINGBAAN = "Hellingbaan" + shpExt
    GEVAARLIJKE_STOFFEN = "Gevaarlijke stoffen" + shpExt
    GEVAREN = "Gevaren" + shpExt
    DBK_LIJN ="Overige lijnen" + shpExt
    SLAGBOOM = "Slagboom" + shpExt
    AANPIJLING = "Aanpijling" + shpExt
    TEKST = "Teksten" + shpExt
    AANRIJROUTE = "Aanrijroute" + shpExt
    DBK_OBJECT ="DBK Object" + shpExt

