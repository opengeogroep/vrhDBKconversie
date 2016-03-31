#-------------------------------------------------------------------------------
# Name:        DBKGlobals
# Purpose:
#
# Author:      Anke Keuren (ARIS)
#              Rinke Heida (ARIS B.V.)
#
# Created:     15-07-2015
# Changes:     20-10-2015, AK:
#              Shapefilenamen in variabelen gezet.
#              30-03-2016, RH:
#              wordSeparator toegevoegd voor verschil in underscore en spatie
# Copyright:   (c) ARIS B.V. 2015-2016
#-------------------------------------------------------------------------------

global shapefileLocation
global dbkobjectFilename
global dbkfeatureFilename
global dbkobjectOutputLocation
global dbkfeaturesOutputLocation
global logFilename
global writeLog

shpExt = ".shp"

# Definieer hoe shapefilenamen zijn opgebouwd:
# In hoodletters en met een spatie of een underscore tussen losse woorden
#UPPERCASE = True
#wordSeparator = "_"
UPPERCASE = False
wordSeparator = " "

if UPPERCASE:
    PAND = "PAND" + shpExt
    BRANDWEERVOORZIENING = "BRANDWEERVOORZIENING" + shpExt
    COMPARTIMENTERING = "COMPARTIMENTERING" + shpExt
    OPSTELPLAATS = "OPSTELPLAATS" + shpExt
    TOEGANG_PAND = "TOEGANG" + wordSeparator + "PAND" + shpExt
    TOEGANG_TERREIN = "TOEGANG" + wordSeparator + "TERREIN" + shpExt
    HELLINGBAAN = "HELLINGBAAN" + shpExt
    GEVAARLIJKE_STOFFEN = "GEVAARLIJKE" + wordSeparator + "STOFFEN" + shpExt
    GEVAREN = "GEVAREN" + shpExt
    DBK_LIJN ="DBK" + wordSeparator + "LIJN" + shpExt
    SLAGBOOM = "SLAGBOOM" + shpExt
    AANPIJLING = "AANPIJLING" + shpExt
    TEKST = "TEKST" + shpExt
    AANRIJROUTE = "AANRIJROUTE" + shpExt
    DBK_OBJECT ="DBK" + wordSeparator + "OBJECT" + shpExt
else:
    PAND = "Pand" + shpExt
    BRANDWEERVOORZIENING = "Brandweervoorziening" + shpExt
    COMPARTIMENTERING = "Compartimentering" + shpExt
    OPSTELPLAATS = "Opstelplaats" + shpExt
    TOEGANG_PAND = "Toegang" + wordSeparator + "pand" + shpExt
    TOEGANG_TERREIN = "Toegang" + wordSeparator + "terrein" + shpExt
    HELLINGBAAN = "Hellingbaan" + shpExt
    GEVAARLIJKE_STOFFEN = "Gevaarlijke" + wordSeparator + "stoffen" + shpExt
    GEVAREN = "Gevaren" + shpExt
    DBK_LIJN ="Overige" + wordSeparator + "lijnen" + shpExt
    SLAGBOOM = "Slagboom" + shpExt
    AANPIJLING = "Aanpijling" + shpExt
    TEKST = "Teksten" + shpExt
    AANRIJROUTE = "Aanrijroute" + shpExt
    DBK_OBJECT ="DBK" + wordSeparator + "Object" + shpExt

