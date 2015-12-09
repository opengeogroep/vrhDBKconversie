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
    TOEGANG_PAND = "TOEGANG_PAND" + shpExt
    TOEGANG_TERREIN = "TOEGANG_TERREIN" + shpExt
    HELLINGBAAN = "HELLINGBAAN" + shpExt
    GEVAARLIJKE_STOFFEN = "GEVAARLIJKE_STOFFEN" + shpExt
    GEVAREN = "GEVAREN" + shpExt
    DBK_LIJN ="DBK_LIJN" + shpExt
    SLAGBOOM = "SLAGBOOM" + shpExt
    AANPIJLING = "AANPIJLING" + shpExt
    TEKST = "TEKST" + shpExt
    AANRIJROUTE = "AANRIJROUTE" + shpExt
    DBK_OBJECT ="DBK_OBJECT" + shpExt
else:
    PAND = "Pand" + shpExt
    BRANDWEERVOORZIENING = "Brandweervoorziening" + shpExt
    COMPARTIMENTERING = "Compartimentering" + shpExt
    OPSTELPLAATS = "Opstelplaats" + shpExt
    TOEGANG_PAND = "Toegang_pand" + shpExt
    TOEGANG_TERREIN = "Toegang_terrein" + shpExt
    HELLINGBAAN = "Hellingbaan" + shpExt
    GEVAARLIJKE_STOFFEN = "Gevaarlijke_stoffen" + shpExt
    GEVAREN = "Gevaren" + shpExt
    DBK_LIJN ="Overige_lijnen" + shpExt
    SLAGBOOM = "Slagboom" + shpExt
    AANPIJLING = "Aanpijling" + shpExt
    TEKST = "Teksten" + shpExt
    AANRIJROUTE = "Aanrijroute" + shpExt
    DBK_OBJECT ="DBK_Object" + shpExt

