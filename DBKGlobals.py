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
    PAND = "pand" + shpExt
    BRANDWEERVOORZIENING = "brandweervoorziening" + shpExt
    COMPARTIMENTERING = "compartimentering" + shpExt
    OPSTELPLAATS = "opstelplaats" + shpExt
    TOEGANG_PAND = "toegang_pand" + shpExt
    TOEGANG_TERREIN = "toegang_terrein" + shpExt
    HELLINGBAAN = "hellingbaan" + shpExt
    GEVAARLIJKE_STOFFEN = "gevaarlijke_stoffen" + shpExt
    GEVAREN = "gevaren" + shpExt
    DBK_LIJN ="dbk_lijn" + shpExt
    SLAGBOOM = "slagboom" + shpExt
    AANPIJLING = "aanpijling" + shpExt
    TEKST = "tekst" + shpExt
    AANRIJROUTE = "aanrijroute" + shpExt
    DBK_OBJECT ="dbk_object" + shpExt

