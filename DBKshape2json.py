#-------------------------------------------------------------------------------
# Name:        DBKshape2json
# Purpose:     Schrijf DBK object informatie uit de shapefiles in json-files.
#
# Author:      Anke Keuren (ARIS B.V.)
#
# Created:     11-06-2015
#-------------------------------------------------------------------------------

import sys, shapefile, datetime
from json import dumps
import DBKGlobals as g, DBKError
from DBKUtils import *
from DBKProperties import *
from DBKDomeinen import *

#-------------------------------------------------------------------------------
# CheckArguments
# <shapefileLocation> <dbkfeaturesOutputLocation> <dbkobjectOutputLocation> {logFilename}
#-------------------------------------------------------------------------------
def CheckArguments(scriptName, Arguments):
    requiredNoOfArgs = 4

    g.writeLog = False

    if len(Arguments) <= requiredNoOfArgs:
        raise DBKError.DBKError('Wrong number of arguments. Usage: DBKshape2json.py <shapefileLocation> <dbkfeaturesOutputLocation> <dbkobjectOutputLocation> {logFilename}')

    # Shapefile locatie
    g.shapefileLocation = Unquote(Arguments[1])
    if not os.path.exists(g.shapefileLocation):
        raise DBKError.DirectoryError(g.shapefileLocation)

    # Uitvoer locatie voor DBKfeatures
    g.dbkfeaturesOutputLocation = Unquote(Arguments[2])
    if not os.path.exists(g.dbkfeaturesOutputLocation):
        raise DBKError.DirectoryError(g.dbkfeaturesOutputLocation)
    g.dbkfeatureFilename = os.path.join(g.dbkfeaturesOutputLocation, 'features.json')

    # Uitvoer locatie voor DBKObjecten
    g.dbkobjectOutputLocation = Unquote(Arguments[3])
    if not os.path.exists(g.dbkobjectOutputLocation):
        raise DBKError.DirectoryError(g.dbkobjectOutputLocation)

    # Naam van logbestand
    if len(Arguments) == 5:
        g.logFilename = Unquote(Arguments[4])
        g.writeLog = True

        logFileLocation = os.path.dirname(g.logFilename)
        if not os.path.exists(logFileLocation):
            g.writeLog = False
            raise DBKError.DirectoryError(logFileLocation)


def main():

# Parameters:
# Locatie van shapefiles
# Locatie van uitvoer DBKFeaturesfile.
# Locatie van uitvoer DBKObjectenfiles.
# Locatie en naam van logfile.

    try:

        currentTime = datetime.datetime.now()
        timeString = currentTime.strftime('%Y-%m-%d %H:%M:%S')
        print("Start: " + str(timeString))

        # Check argumenten
        CheckArguments('WriteDBKObjecten', sys.argv)

        if g.writeLog:
            WriteLogTxt(g.logFilename, LogStart())

        # CreÃƒÆ’Ã‚Â«er de domeinen.
        DtypeBrandcomp = DBKDBrandcompartiment()
        DtypeBrandweervoorz = DBKDBrandweervoorziening()
        DtypeGevaarlijkeStof = DBKDGevaarlijkestof()
        DtypeHulplijn = DBKDHulplijn()

        # Definieer DBKobject properties
        DBKObjectDef = [
                        DBKStrProp("identificatie", g.shapefileLocation, "PAND", "DBK_OBJECT"),
                        DBKBoolProp("BHVaanwezig", g.shapefileLocation, "PAND", "AANWEZIG_1"),
                        DBKDateProp("controleDatum", g.shapefileLocation, "PAND", "LAATSTE_CO"),
                        DBKStrProp("formeleNaam", g.shapefileLocation, "PAND", "NAAM_PAND"),
                        DBKStrProp("informeleNaam", g.shapefileLocation, "PAND", "INFORMELE_"),
                        DBKStrProp("OMSnummer", g.shapefileLocation, "PAND", "OMS_NUMMER"),
                        DBKStrProp("inzetprocedure", g.shapefileLocation, "PAND", "INZETPROCE"),
                        DBKIntProp("laagsteBouwlaag", g.shapefileLocation, "PAND", "BOUWLAGENO"),
                        DBKIntProp("hoogsteBouwlaag", g.shapefileLocation, "PAND", "BOUWLAGENB"),
                        DBKStrProp("risicoklasse", g.shapefileLocation, "PAND", "RISICOKLAS"),
                        DBKStrProp("gebouwconstructie", g.shapefileLocation, "PAND", "GEBOUWCONS"),
                        DBKStrProp("gebruikstype", g.shapefileLocation, "PAND", "GEBRUIKSDO"),
                        DBKListProp("verblijf")
                           #Dag
                          .addProp(DBKVerblijfProp("verblijf", g.shapefileLocation, "PAND", "PERSONEEL_", "Personeel", True, "09:00:00", "17:00:00", True))
                          .addProp(DBKVerblijfProp("verblijf", g.shapefileLocation, "PAND", "BEZOEKERS_", "Bezoekers", True, "09:00:00", "17:00:00", True))
                          .addProp(DBKVerblijfProp("verblijf", g.shapefileLocation, "PAND", "SLAAPPLAAT", "Slaapplaatsen", True, "09:00:00", "17:00:00", True))
                          #Nacht
                          .addProp(DBKVerblijfProp("verblijf", g.shapefileLocation, "PAND", "PERSONEEL1", "Personeel", True, "17:00:00", "09:00:00", True))
                          .addProp(DBKVerblijfProp("verblijf", g.shapefileLocation, "PAND", "BEZOEKERS1", "Bezoekers", True,  "17:00:00", "09:00:00", True))
                          .addProp(DBKVerblijfProp("verblijf", g.shapefileLocation, "PAND", "SLAAPPLA_1", "Slaapplaatsen", True,  "17:00:00", "09:00:00", True))
                          #Weekend
                          .addProp(DBKVerblijfProp("verblijf", g.shapefileLocation, "PAND", "PERSONEE_1", "Personeel", True, "17:00:00", "09:00:00", False))
                          .addProp(DBKVerblijfProp("verblijf", g.shapefileLocation, "PAND", "BEZOEKER_1", "Bezoekers", True,  "17:00:00", "09:00:00", False))
                          .addProp(DBKVerblijfProp("verblijf", g.shapefileLocation, "PAND", "SLAAPPLA_2", "Slaapplaatsen", True,  "17:00:00", "09:00:00", False)),
                        DBKListProp("adres")
                          .addProp(DBKAdresProp("adres", g.shapefileLocation, "PAND", "ADRES", "PLAATS")),
                        DBKListProp("afwijkendebinnendekking")
                          .addProp(DBKBinnendekCompProp("afwijkendebinnendekking", g.shapefileLocation, "PAND", "C2000_BINN", "AFWIJKENDE", "BINNENDEKK")),
                        DBKListProp("pandgeometrie")
                            .addProp(DBKPandgeometrieProp("pandgeometrie", g.shapefileLocation, "PAND", "DBK_OBJECT", "BAGPAND_ID", "STATUS_BAG")),
                        DBKListProp("brandcompartiment")
                            .addProp(DBKBrandCompProp("brandcompartiment",  g.shapefileLocation, "COMPARTIMENTERING", "DBK_OBJECT", "SYMBOOLCOD", "BIJZONDERH", DtypeBrandcomp)),
                        DBKListProp("brandweervoorziening")
                            .addProp(DBKBWVoorzProp("brandweervoorziening", g.shapefileLocation, "BRANDWEERVOORZIENING", "DBK_OBJECT", "SYMBOOLCOD", "OMSCHRIJVI", "BIJZONDERH", "SYMBOOLHOE", "SYMBOOLGRO", DtypeBrandweervoorz))
                            .addProp(DBKBWVoorzProp("brandweervoorziening", g.shapefileLocation, "OPSTELPLAATS", "DBK_OBJECT", "SYMBOOLCOD", "OMSCHRIJVI", "BIJZONDERH", "SYMBOOLHOE", "SYMBOOLGRO", DtypeBrandweervoorz))
                            .addProp(DBKBWVoorzProp("brandweervoorziening", g.shapefileLocation, "TOEGANG_PAND", "DBK_OBJECT", "SYMBOOLCOD", "OMSCHRIJVI", "BIJZONDERH", "SYMBOOLHOE", "SYMBOOLGRO", DtypeBrandweervoorz))
                            .addProp(DBKBWVoorzProp("brandweervoorziening", g.shapefileLocation, "TOEGANG_TERREIN", "DBK_OBJECT", "SYMBOOLCOD", "OMSCHRIJVI", "BIJZONDERH", "SYMBOOLHOE", "SYMBOOLGRO", DtypeBrandweervoorz)),
                        DBKListProp("contact")
                          .addProp(DBKContactProp("contact", g.shapefileLocation, "PAND", "CONTACT_FU", "CONTACT_NA", "CONTACT_TE")),
                        DBKListProp("foto")
                          .addProp(DBKFotoProp("foto", g.shapefileLocation, "PAND", "FOTO", "FOTO")),
                        DBKListProp("gevaarlijkestof")
                            .addProp(DBKGevaarStofProp("gevaarlijkestof", g.shapefileLocation, "GEVAARLIJKE_STOFFEN", "DBK_OBJECT", "STOFNAAM", "GEVI_CODE", "VN_NUMMER", "SYMBOOLCOD", "HOEVEELHEI", "BIJZONDERH", DtypeGevaarlijkeStof))
                            .addProp(DBKGevaarStofProp("gevaarlijkestof", g.shapefileLocation, "GEVAREN", "DBK_OBJECT", "SOORT_GEVA", None, None, "SYMBOOLCOD", None, "BIJZONDERH", DtypeGevaarlijkeStof)),
                        DBKListProp("hulplijn")
                            .addProp(DBKHulplijnDomProp("hulplijn", g.shapefileLocation, "DBK_LIJN", "DBK_OBJECT", "TYPE", "BIJZONDERH", "OPMERKINGE", DtypeHulplijn))
                            .addProp(DBKHulplijnConstProp("hulplijn", g.shapefileLocation, "SLAGBOOM", "DBK_OBJECT", "BIJZONDERH", "Bbarrier"))
                            .addProp(DBKHulplijnConstProp("hulplijn", g.shapefileLocation, "AANPIJLING", "DBK_OBJECT", "BIJZONDERH", "Line")),
                        DBKListProp("tekstobject")
                            .addProp(DBKTekstProp("tekst", g.shapefileLocation, "TEKST", "DBK_OBJECT", "TEKST", "SYMBOOLHOE", "SYMBOOLGRO")),
                        DBKListProp("toegangterrein")
                            .addProp(DBKToegangTerreinProp("toegangterrein", g.shapefileLocation, "AANRIJROUTE", "DBK_OBJECT", "BIJZONDERH"))
        ]

        # Definieer DBKfeature properties
        DBKFeaturePropDef = [
                        DBKStrProp("identificatie", g.shapefileLocation, "PAND", "DBK_OBJECT"),
                        DBKBoolProp("BHVaanwezig", g.shapefileLocation, "PAND", "AANWEZIG_1"),
                        DBKDateProp("controleDatum", g.shapefileLocation, "PAND", "LAATSTE_CO"),
                        DBKStrProp("formeleNaam", g.shapefileLocation, "PAND", "NAAM_PAND"),
                        DBKStrProp("informeleNaam", g.shapefileLocation, "PAND", "INFORMELE_"),
                        DBKStrProp("OMSnummer", g.shapefileLocation, "PAND", "OMS_NUMMER"),
                        DBKStrProp("inzetprocedure", g.shapefileLocation, "PAND", "INZETPROCE"),
                        DBKConstProp("typeFeature", "Object"),
                        DBKConstProp("verwerkt", None),
                        DBKConstProp("hoofdobject", None),
                        DBKConstProp("bouwlaag", None),
                        DBKStrProp("risicoklasse", g.shapefileLocation, "PAND", "RISICOKLAS"),
                        DBKConstProp("verdiepingen", 0),
                        DBKListProp("adres")
                          .addProp(DBKAdresProp("adres", g.shapefileLocation, "PAND", "ADRES", "PLAATS")),
        ]

        # Definieer geometry-property voor DBKfeature
        DBKfeatGeomProp = DBKGeomCentroidProp()

        # Lees de shapefile met DBKObjecten.
        dbkobjectReader = shapefile.Reader(os.path.join(g.shapefileLocation, "DBK_OBJECT.shp"))

        # Haal de attribuutvelden op van de DBKObjecten-shapefile.
        dbkobjectfields = dbkobjectReader.fields[1:]

        # Bepaal de index van het ID-veld van de DBKObjecten-shapefile.
        idfldindex = FindField(dbkobjectfields, "ID")


        # Lees de shapefile met panden.
        pandReader = shapefile.Reader(os.path.join(g.shapefileLocation, "PAND.shp"))

        # Haal de attribuutvelden op van de panden-shapefile.
        pandfields = pandReader.fields[1:]

        # Bepaal voor alle DBKObject-properties de veldindex bij de pand-velden .
        for item in DBKObjectDef:
            if isinstance(item, DBKProp):
                item.setFieldindex(pandfields)

        # Bepaal voor alle DBKfeature-properties de veldindex bij de pand-velden .
        for item in DBKFeaturePropDef:
            if isinstance(item, DBKProp):
                item.setFieldindex(pandfields)

        # Zet de hoofdpanden in een dictionary met het joinID als key.
        # We gaan ervan uit dat een DBKObject 1 hoofdpand heeft.
        joinfldindex = FindField(pandfields, "DBK_OBJECT")
        hsfldidx = FindField(pandfields, "HOOFD_SUB")
        hoofdpanden = dict()
        for sr in pandReader.shapeRecords():
            joinID = sr.record[joinfldindex]
            if sr.record[hsfldidx] == "Hoofdpand":
                if not joinID in hoofdpanden:
                    hoofdpanden[joinID] = sr

        # Definieer de lijst voor DBKFeatures.
        DBKFeatures = []
        teller = 0

        # Doorloop de DBKObjecten.
        for srDBKObject in dbkobjectReader.shapeRecords():
            dictDBKObject = dict()
            dictDBKFeature = dict()
            dictDBKFeatProp = dict()

            # Als het DBKObject een hoofdpand heeft, dan gaan we schrijven.
            joinID = srDBKObject.record[idfldindex]
            if joinID in hoofdpanden:
                srHoofdpand = hoofdpanden[joinID]

                # Lees alle DBKObject-properties
                for item in DBKObjectDef:
                    if isinstance(item, DBKMultiProp):
                        fldidx = FindField(pandfields, item.joinfield)
                        dictDBKObject.update({item.name: item.value(joinID)})
                    elif isinstance(item, DBKListProp):
                        dictDBKObject.update({item.name: item.value(srHoofdpand, pandfields)})
                    else:
                        dictDBKObject.update({item.name: item.value(srHoofdpand)})
                # Schrijf het DBKObject in een json-file.
                dbkobjectJSON = open(os.path.join(g.dbkobjectOutputLocation, str(joinID) + '.json'), "w")
                # pretty
                dbkobjectJSON.write(dumps({"DBKObject": dictDBKObject}, indent=2, ensure_ascii=False, sort_keys=True) + "\n")
                # flat
                #dbkobjectJSON.write(dumps({"DBKObject": dictDBKObject}, ensure_ascii=False, sort_keys=True))
                dbkobjectJSON.close()


                # Lees alle DBKFeature-properties:
                for item in DBKFeaturePropDef:
                    if isinstance(item, DBKMultiProp):
                        dictDBKFeatProp.update({item.name: item.value(joinID)})
                    elif isinstance(item, DBKListProp):
                        dictDBKFeatProp.update({item.name: item.value(srHoofdpand, pandfields)})
                    else:
                        if type(item) is DBKConstProp:
                            dictDBKFeatProp.update({item.name: item.value})
                        else:
                            dictDBKFeatProp.update({item.name: item.value(srHoofdpand)})
                # Zet ook een gid aan de hand van de teller.
                dictDBKFeatProp.update({"gid": teller})

                # Zet de properties in de DBKFeature dictionary.
                dictDBKFeature.update({"properties": dictDBKFeatProp})

                # De centroid wordt bepaald op basis van de DBKObject polygoon.
                dictDBKFeature.update({DBKfeatGeomProp.name: DBKfeatGeomProp.value(srDBKObject)})

                # Zet het id (gelijk aan gid).
                dictDBKFeature.update({"id": "DBKFeature.gid--" + str(teller)})

                # Het type is "Feature"
                dictDBKFeature.update({"type": "Feature"})

                # Voeg het DBKfeature toe aan de lijst met DBKFeatures.
                DBKFeatures.append(dictDBKFeature)
            else:
                # Als het DBKObject geen hoofdpand heeft zetten we dit in de logfile.
                if g.writeLog:
                    WriteLogTxt(g.logFilename, 'Geen hoofdpand gevonden voor joinID {0}.\n'.format(joinID))
            teller += 1

        # Als alle DBKObjecten zijn doorlopen, dan schrijven we ook de DBKFeatures in een json-file.
        dbkfeatureJSON = open(g.dbkfeatureFilename, "w")
        # pretty
        dbkfeatureJSON.write(dumps({"type":"FeatureCollection","features": DBKFeatures}, indent=2, ensure_ascii=False, sort_keys=True) + "\n")
        # flat
        #dbkfeatureJSON.write(dumps({"type":"FeatureCollection","features": DBKFeatures}, ensure_ascii=False, sort_keys=True))
        dbkfeatureJSON.close()

        currentTime = datetime.datetime.now()
        timeString = currentTime.strftime('%Y-%m-%d %H:%M:%S')
        print("Einde: " + str(timeString))


    except OSError as err:
        print (err.strerror)
        if g.writeLog:
            WriteLogTxt(g.logFilename, LogError(err.strerror))
    except DBKError.DBKError as err:
        print (err.message)
        if g.writeLog:
            WriteLogTxt(g.logFilename, LogError(err.message))
    except Exception as err:
        print (err)
        if g.writeLog:
            WriteLogTxt(g.logFilename, err)
    finally:
        if 'dbkobjectJSON' in locals():
            dbkobjectJSON.close
        if g.writeLog:
            WriteLogTxt(g.logFilename, LogEnd())


if __name__ == '__main__':
    main()
