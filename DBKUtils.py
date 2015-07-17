#-------------------------------------------------------------------------------
# Name:        DBKUtils
# Purpose:     Set of common functions
#
# Author:      Anke Keuren (ARIS)
#
# Created:     07-07-2015
# Copyright:   (c) ARIS B.V. 2015
#-------------------------------------------------------------------------------
import os, datetime
from shapefile import *
from shapely.geometry import Point, LineString, Polygon

#-------------------------------------------------------------------------------
def FindField(fields, fieldname):
    for index, field in enumerate(fields):
        if field[0] == fieldname:
            return index
    return -1

#-------------------------------------------------------------------------------
def GetTableName(ConnectionString, Separator):
    # Delete xxxxData Source= part from Enc_par_table_mdb
    TableName = ConnectionString[ConnectionString.lower().find('source=') + 7:]

    # Change ! into Separator
    TableName = TableName.replace('!', Separator)
    return TableName

#-------------------------------------------------------------------------------
def Unquote(s):
    s = s.replace('\'', '')
    return s.replace('"', '')

#-------------------------------------------------------------------------------
def GeomCentroid(shape):
    if shape.shapeType in [5, 15, 25]:
        poly = Polygon(shape.points)
        polyCentroid = poly.centroid

        geom = polyCentroid.__geo_interface__
        return geom
    else:
        return None

#-------------------------------------------------------------------------------
def HasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

#-------------------------------------------------------------------------------
# Function:   SplitsAdres
# Purpose:    Splits een adres-regel in straatnaam, huisnummer en letter.
# Parameters: - adres: string
#             - result: dictionary
#-------------------------------------------------------------------------------
def SplitsAdres(adres, result):
    straat = ""
    huisnummer = ""
    huisletter = ""
    if not HasNumbers(adres):
        straat = adres
    else:
        for c in reversed(adres):
            if c.isnumeric():
                if len(straat) == 0:
                    huisnummer = c + huisnummer
                else:
                    straat = c + straat
            elif c.isalpha():
                if len(huisnummer) == 0:
                    huisletter = c + huisletter
                else:
                    straat = c + straat
            else:
                if len(straat) == 0:
                    huisnummer = c + huisnummer
                else:
                    straat = c + straat
    if len(huisletter.strip()) > 0 and len(huisnummer.strip()) == 0:
        straat = straat + " " + huisletter
        huisletter = ""

    result["openbareRuimteNaam"] = straat.strip()
    result["huisnummer"] = huisnummer.strip()
    result["huisletter"] = huisletter.strip()

#----------------------------------------------------------------------------
def LogStart():
    txt = '\n'
    txt += '#============================================================================' + '\n'
    txt += 'Start Conversie: ' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '\n'
    return txt

#----------------------------------------------------------------------------
def LogEnd():
    txt = ''
    txt += 'End Conversie  : ' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '\n'
    txt += '#============================================================================' + '\n'
    return txt

#----------------------------------------------------------------------------
def LogError(msg):
    txt = 'Error: ' + msg + '\n'
    ##txt += '#----------------------------------------------------------------------------' + '\n'
    return txt

#----------------------------------------------------------------------------
def LogWarning(msg):
    txt = 'Warning: ' + msg + '\n'
    ##txt += '#----------------------------------------------------------------------------' + '\n'
    return txt

#-------------------------------------------------------------------------------
def WriteLogTxt(logFileName,txt):
    with open(logFileName,'a') as logfile:
        logfile.write(txt)

