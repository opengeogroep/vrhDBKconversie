#-------------------------------------------------------------------------------
# Name:        DBKProperties
# Purpose:
#
# Author:      Anke Keuren (ARIS B.V.)
#
# Created:     16-06-2015
#-------------------------------------------------------------------------------

import os, shapefile, datetime
import DBKGlobals as g, DBKError as e
from DBKUtils import *
#from DBKMultiProperties import *

#-------------------------------------------------------------------------------
class DBKConstProp(object):
    def __init__(self, name, value=None):
        self.name = name
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

#-------------------------------------------------------------------------------
class DBKProp(object):
    def __init__(self, name, location=None, shapefile=None, fieldname=None):
        self.name = name
        self.shapefile = self.setShapefile(location, shapefile)
        self.fieldname = fieldname
        self.fieldindex = -1
        self._value = None
        self.isList = False

##    def setShapefile(self, shapefile):
##        self.shapefile = shapefile
    def setShapefile(self, location, shapefile):
        if not os.path.exists(location):
            raise e.DirectoryError(location)
        fullname = os.path.join(location, shapefile)
        fileName, fileExt = os.path.splitext(fullname)
        if fileExt.lower() == '':
            fullname = fileName +'.shp'
        elif fileExt.lower() != '.shp':
            raise e.ShapefileError(fullname)

        if not os.path.exists(fullname):
            raise e.FileError(fullname)
        return fullname

    def setFieldname(self, fieldname):
        self.fieldname = fieldname

    def setFieldindex(self, fields):
        if self.fieldname != None:
            fieldindex = FindField(fields, self.fieldname)
            if fieldindex == -1:
                #raise e.FieldError(self.fieldname, self.shapefile)
                if g.writeLog:
                    WriteLogTxt(g.logFilename, LogWarning(e.MappingError(self.fieldname, self.shapefile, self.name).message))
            self.fieldindex = fieldindex

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


#-------------------------------------------------------------------------------
# DBKListProp: Resulteert in een list gebaseerd op meerdere velden in een record.
class DBKListProp(DBKProp):
    def __init__(self, name):
        self.name = name
        self.isList = True
        self._propList = []

    def setFieldindex(self, fields):
        for item in self._propList:
            item.setFieldindex(fields)

    def addProp(self, DBKProp):
        self._propList.append(DBKProp)
        return self

    def value(self, shaperecord, fields):
        valueList = []
        for item in self._propList:
            if isinstance(item, DBKMultiProp):
                fldidx = FindField(fields, item.joinfield)
                if fldidx > -1:
                    joinid = shaperecord.record[fldidx]
                    v = item.value(joinid)
                    if v:
                        valueList.extend(v)
                else:
                    if g.writeLog:
                        WriteLogTxt(g.logFilename, LogWarning(e.FieldError(item.joinfield, item.shapefile).message))
            else:
                v = item.value(shaperecord)
                if v:
                    valueList.append(v)

##            v = item.value(shaperecord)
##            if v:
##                valueList.append(v)
        if len(valueList) > 0:
            return valueList
        else:
            return None

#-------------------------------------------------------------------------------
class DBKStrProp(DBKProp):
    def value(self, shaperecord):
##        if self.fieldname == None:
##            return None
        if self.fieldindex == -1:
            return None
        v = shaperecord.record[self.fieldindex]
        if v:
            try:
                s = str(v)
                return s
            except:
                return None
        return None

#-------------------------------------------------------------------------------
class DBKIntProp(DBKProp):
    def value(self, shaperecord):
        if self.fieldindex == -1:
            return None
        v = shaperecord.record[self.fieldindex]
        if v:
            try:
                i = int(v)
                return i
            except:
                return None
        return None

#-------------------------------------------------------------------------------
class DBKDateProp(DBKProp):
    def value(self, shaperecord):
        if self.fieldindex == -1:
            return None
        v = shaperecord.record[self.fieldindex]
        if v:
            try:
                dt = datetime.datetime.strptime(v, "%Y%m%d")
                return str(dt)
            except:
                return None
        return None

#-------------------------------------------------------------------------------
class DBKBoolProp(DBKProp):
    def value(self, shaperecord):
        if self.fieldindex == -1:
            return None
        v = shaperecord.record[self.fieldindex]
        if v:
            try:
                if v.upper() == "JA":
                    return True
                elif v.upper() == "NEE":
                    return False
                else:
                    return None
            except:
                return None
        return None

#-------------------------------------------------------------------------------
class DBKHoekProp(DBKIntProp):
    def __init__(self, name, location, shapefile, fieldname, correction=0):
        super(DBKHoekProp, self).__init__(name, location, shapefile, fieldname)
        self._correction = correction

    def value(self, shaperecord):
        v = super(DBKHoekProp, self).value(shaperecord)
        if v:
            v = v + self._correction
            if v < -360:
                v = v + 360
            elif v > 360:
                v = v - 360
            return v
        return None

#-------------------------------------------------------------------------------
# DBKSymbProp: Symboolcode property. In Haaglanden zijn symboolcodes met een
#              komma opgenomen. Deze worden t.b.v. DBK vervangen door een punt.
class DBKSymbProp(DBKStrProp):
    def __init__(self, name, location, shapefile, fieldname, domein=None, domeinfldname=None):
        super(DBKSymbProp, self).__init__(name, location, shapefile, fieldname)
        self._domein = domein
        self._domeinfldname = domeinfldname

    def value(self, shaperecord):
        s = super(DBKSymbProp, self).value(shaperecord)
        if s:
            try:
                if self._domein:
                    return self._domein.value(s.replace(",", "."), self._domeinfldname)
                else:
                    return s.replace(",", ".")
            except:
                return None
        return None

#-------------------------------------------------------------------------------
class DBKGeomProp(DBKProp):
    def __init__(self):
        super(DBKGeomProp, self).__init__("geometry")

    def setShapefile(self, location, shapefile):
        return None

    def setFieldindex(self, fields):
        return None

    def value(self, shaperecord):
        geom = shaperecord.shape.__geo_interface__
        geom.update({"crs": {"type": "name","properties": {"name": "EPSG:28992"}}})
        return geom

#-------------------------------------------------------------------------------
class DBKGeomCentroidProp(DBKProp):
    def __init__(self):
        super(DBKGeomCentroidProp, self).__init__("geometry")

    def setShapefile(self, location, shapefile):
        return None

    def setFieldindex(self, fields):
        return None

    def value(self, shaperecord):
        geomCentroid = GeomCentroid(shaperecord.shape)
        geomCentroid.update({"crs": {"type": "name","properties": {"name": "EPSG:28992"}}})
        return geomCentroid

#-------------------------------------------------------------------------------
# Input uit meerdere velden wordt in een veld samengevoegd.
class DBKMultiFieldProp(DBKProp):
    def __init__(self, name, location, shapefile, fieldnames):
        super(DBKMultiFieldProp, self).__init__(name, location, shapefile)
        self._fieldnames = []
        self._fieldnames.extend(fieldnames)
        self._fieldindices = []

    def setFieldindex(self, fields):
        for f in self._fieldnames:
            fieldindex = FindField(fields, f)
            if fieldindex == -1:
                #raise e.FieldError(self.fieldname, self.shapefile)
                if g.writeLog:
                    WriteLogTxt(g.logFilename, LogWarning(e.MappingError(self.fieldname, self.shapefile, self.name).message))
            self._fieldindices.append(fieldindex)

    def value(self, shaperecord):
        if self._fieldnames.count == 0:
            return None
        s = ""
        for i in self._fieldindices:
            if i > -1:
                v = shaperecord.record[i]
                if v:
                    try:
                        if len(s) > 0:
                            s += "; "
                        s += str(v)
                    except:
                        return None
        return s
        #return None

#-------------------------------------------------------------------------------
class DBKSamengesteldProp(DBKProp):
    def __init__(self, name, location, shapefile=None, fieldname=None):
        super(DBKSamengesteldProp, self).__init__(name, location, shapefile, fieldname)

        self._Props = []

    def setFieldindex(self, fields):
        super(DBKSamengesteldProp,self).setFieldindex(fields)
        for item in self._Props:
            if isinstance(item, DBKProp):
                item.setFieldindex(fields)

    def addProp(self, DBKProp):
        self._Props.append(DBKProp)
        return self


    #---------------------------------------------------------------------------
    # Retourneer alle elementen van het samengestelde element.
    # Controleer of niet alle waarden van de elementen leeg zijn. Als dat zo
    # is, dan None teruggeven.
    def value(self, shaperecord):
        allEmpty = True
        SGProp = dict()

        for item in self._Props:
            if type(item) is DBKConstProp:
                SGProp.update({item.name: item.value})
            else:
                v = item.value(shaperecord)
                if v:
                    allEmpty = False
                SGProp.update({item.name: item.value(shaperecord)})
        if allEmpty:
            return None
        else:
            return SGProp


#-------------------------------------------------------------------------------
# DBKMultiProp: Resulteert in een list gebaseerd op meerdere records in een
#               shapefile.
class DBKMultiProp(DBKSamengesteldProp):
##    def __init__(self, name, shapefile, joinfield, DBKProp):
##    def __init__(self, name, location, shapefile, joinfield, DBKProp):
    def __init__(self, name, location, shapefile, joinfield):
        super(DBKMultiProp, self).__init__(name, location, shapefile)
##        self.name = name
##        self._shapefile = self.setShapefile(location, shapefile)
        self.joinfield = joinfield
#        self._dbkProp = DBKProp
        self._fieldindex = None
        self._shaperecords = dict()
        self._propList = []
        self._shapefileList = []
        self._shapefileList.append(self.setShapefile(location, shapefile))

    def setFieldindex(self, fields):
        return None

    def _read(self):
        reader = shapefile.Reader(self.shapefile)

        # Haal alleen de attribuutvelden op.
        fields = reader.fields[1:]

        # Bepaal bij de veldindex van het joinfield.
        fldindex = FindField(fields, self.joinfield)

        # Bepaal ook de veldindex van Property
        # Zet de fieldindex op basis van de hier ingelezen shapefile en
        # doe dit in de klasse SamengesteldProp.
        super(DBKMultiProp, self).setFieldindex(fields)

        # Zet de shaperecords in een dictionary met het joinID als key.
        for sr in reader.shapeRecords():
            joinID = sr.record[fldindex]
            if joinID in self._shaperecords:
                self._shaperecords[joinID].append(sr)
            else:
                self._shaperecords[joinID] = [sr]

##    def setShapefile(self, location, shapefile):
##        if not os.path.exists(location):
##            raise e.DirectoryError(location)
##        fullname = os.path.join(location, shapefile)
##        fileName, fileExt = os.path.splitext(fullname)
##        if fileExt.lower() == '':
##            fullname = fileName +'.shp'
##        elif fileExt.lower() != '.shp':
##            raise e.ShapefileError(fullname)
##
##        if not os.path.exists(fullname):
##            raise e.FileError("File '{0}' does not exists".format(fullname))
##        return fullname
##    def setShapefile(self, location, shapefile):
##        if not os.path.exists(location):
##            raise e.DirectoryError(location)
##        fullname = os.path.join(location, shapefile)
##        fileName, fileExt = os.path.splitext(fullname)
##        if fileExt.lower() == '':
##            fullname = fileName +'.shp'
##        elif fileExt.lower() != '.shp':
##            raise e.ShapefileError(fullname)
##
##        if not os.path.exists(fullname):
##            #raise e.FileError(fullname)
##            if g.writeLog:
##                WriteLogTxt(g.logFilename, LogWarning(e.FileError(fullname).message))
##            return None
##
##        return fullname

    def value(self, joinID):
        #Lees de shapefile als dit nog niet was gebeurd.
        if self.shapefile:
            buffer = []
            if len(self._shaperecords) == 0:
                self._read()

            #Als na het lezen nog geen records, dan was de shapefile leeg.
            if len(self._shaperecords) > 0:
                #Zoek de records met joinID
                if joinID in self._shaperecords:
                    shaperecords = self._shaperecords[joinID]
                    for sr in shaperecords:
                        #buffer.append({self._dbkProp.name: self._dbkProp.value(sr)})
                        #buffer.append(self._dbkProp.value(sr))
                        buffer.append(super(DBKMultiProp, self).value(sr))
                    return buffer
                else:
                    return None
            else:
                return None
        else:
            return None

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
class DBKVerblijfProp(DBKProp):
    def __init__(self, name, location, shapefile=None, fieldname=None, typegroep=None,
                 zelfredzaam=True,begintijd=None,eindtijd=None, doordeweeks=True):
        super(DBKVerblijfProp, self).__init__(name, location, shapefile, fieldname)

        self._constProps = [DBKConstProp("typeAanwezigheidsgroep", typegroep),
                      DBKConstProp("tijdvakBegintijd", begintijd),
                      DBKConstProp("tijdvakEindtijd", eindtijd),
                      DBKConstProp("maandag", doordeweeks),
                      DBKConstProp("dinsdag", doordeweeks),
                      DBKConstProp("woensdag", doordeweeks),
                      DBKConstProp("donderdag", doordeweeks),
                      DBKConstProp("vrijdag", doordeweeks),
                      DBKConstProp("zaterdag", not doordeweeks),
                      DBKConstProp("zondag", not doordeweeks)
                      ]
        self._zelfredzaam = zelfredzaam

        self._aantal = DBKStrProp("aantal", location, shapefile, fieldname)
        if not zelfredzaam:
            self._aantalNZR = DBKStrProp("aantal", location, shapefile, fieldname)

    def setFieldindex(self, fields):
        super(DBKVerblijfProp,self).setFieldindex(fields)
        self._aantal.setFieldindex(fields)
        if not self._zelfredzaam:
            self._aantalNZR.setFieldindex(fields)

    def value(self, shaperecord):
        v = self._aantal.value(shaperecord)
        if v:
            verblijf = dict()
            verblijf.update({self._aantal.name: self._aantal.value(shaperecord)})
            if not self._zelfredzaam:
                verblijf.update({self._aantalNZR.name: self._aantalNZR.value(shaperecord)})
            else:
                verblijf.update({"aantalNietZelfredzaam": ""})

            for item in self._constProps:
                verblijf.update({item.name: item.value})
            return verblijf
        else:
            return None

#-------------------------------------------------------------------------------
class DBKAdresProp(DBKSamengesteldProp):
    def __init__(self, name, location, shapefile, adresfldname, plaatsfldname):
        super(DBKAdresProp, self).__init__(name, location, shapefile)

        self._adresfldname = adresfldname
        self._adresfldidx = -1
        self._plaatsfldname = plaatsfldname
        self._plaatsfldidx = -1

        self.addProp(DBKConstProp("bagId", None))
        self.addProp(DBKStrProp("woonplaatsNaam", location, shapefile, plaatsfldname))
        self.addProp(DBKConstProp("gemeenteNaam", None))
        self.addProp(DBKConstProp("adresseerbaarObject", None)),
        self.addProp(DBKConstProp("typeAdresseerbaarObject", None))
        self.addProp(DBKConstProp("huisnummertoevoeging", None))
        self.addProp(DBKConstProp("postcode", None))

##        "openbareRuimteNaam": Afleiden uit PAND.ADRES?,
##        "huisnummer": Afleiden uit PAND.ADRES?,
##        "huisletter": Afleiden uit PAND.ADRES?,

    def setFieldindex(self, fields):
        super(DBKAdresProp, self).setFieldindex(fields)

        # Zet de veld-index van het adres-veld.
        if self._adresfldname != None:
            self._adresfldidx = FindField(fields, self._adresfldname)
            if self._adresfldidx == -1:
                #raise e.FieldError(self._adresfldname, self.shapefile)
                if g.writeLog:
                    #WriteLogTxt(g.logFilename, LogWarning(e.FieldError(self._adresfldname, self.shapefile).message))
                    WriteLogTxt(g.logFilename, LogWarning(e.MappingError(self._adresfldname, self.shapefile, self.name).message))
##        # Zet de veld-index van het plaats-veld.
##        if self._adresfldname != None:
##            self._plaatsfldidx = FindField(fields, self._plaatsfldname)
##            if self._plaatsfldidx == -1:
##                raise e.FieldError(self._plaatsfldname, self.shapefile)

    def value(self, shaperecord):
        adresProp = super(DBKAdresProp, self).value(shaperecord)
        if adresProp:
            if self._adresfldidx != -1:
                adres = shaperecord.record[self._adresfldidx]
                if adres:
                    SplitsAdres(adres, adresProp)
        return adresProp



#-------------------------------------------------------------------------------
class DBKBinnendekCompProp(DBKSamengesteldProp):
    def __init__(self, name, location, shapefile, dekkingfldname, altdekkingfldname, infofldname):
        super(DBKBinnendekCompProp, self).__init__(name, location, shapefile)

        self.addProp(DBKBoolProp("dekking", location, shapefile, dekkingfldname))
        self.addProp(DBKStrProp("alternatieveCommInfrastructuur", location, shapefile, altdekkingfldname))
        self.addProp(DBKStrProp("aanvullendeInformatie", location, shapefile, infofldname))
        self.addProp(DBKGeomCentroidProp())

#-------------------------------------------------------------------------------
class DBKBrandCompProp(DBKMultiProp):
    def __init__(self, name, location, shapefile, joinfldname, typefldname, infofldname, domein=None):
        super(DBKBrandCompProp, self).__init__(name, location, shapefile, joinfldname)

        self.addProp(DBKSymbProp("typeScheiding", location, shapefile, typefldname, domein, "naam"))
        self.addProp(DBKConstProp("Label", None))
        self.addProp(DBKStrProp("aanvullendeInformatie", location, shapefile, infofldname))
        self.addProp(DBKGeomProp())

#-------------------------------------------------------------------------------
# DBKBWVoorzProp: Brandweervoorziening
class DBKBWVoorzProp(DBKMultiProp):
    def __init__(self, name, location, shapefile, joinfldname, typefldname, omschrfldname, bijzfldname, hoekfldname, radiusfldname, domein=None):
        super(DBKBWVoorzProp, self).__init__(name, location, shapefile, joinfldname)

        #self.addProp(DBKSymbProp("typeVoorziening", location, shapefile, typefldname))
        self.addProp(DBKSymbProp("typeVoorziening", location, shapefile, typefldname, domein, "symboolcode"))
        self.addProp(DBKSymbProp("naamVoorziening", location, shapefile, typefldname, domein, "naam"))
        self.addProp(DBKSymbProp("namespace", location, shapefile, typefldname, domein, "namespace"))
        self.addProp(DBKSymbProp("categorie", location, shapefile, typefldname, domein, "categorie"))
        self.addProp(DBKMultiFieldProp("aanvullendeInformatie", location, shapefile, [omschrfldname, bijzfldname]))
        self.addProp(DBKHoekProp("hoek", location, shapefile, hoekfldname, -81))
        self.addProp(DBKIntProp("radius", location, shapefile, radiusfldname))
        self.addProp(DBKGeomProp())

#-------------------------------------------------------------------------------
class DBKContactProp(DBKSamengesteldProp):
    def __init__(self, name, location, shapefile, functiefldname, naamfldname, telfldname):
        super(DBKContactProp, self).__init__(name, location, shapefile)

        self.addProp(DBKStrProp("functie", location, shapefile, functiefldname))
        self.addProp(DBKStrProp("naam", location, shapefile, naamfldname)),
        self.addProp(DBKStrProp("telefoonnummer", location, shapefile, telfldname))

#-------------------------------------------------------------------------------
class DBKFotoProp(DBKSamengesteldProp):
    def __init__(self, name, location, shapefile, naamfldname, urlfldname):
        super(DBKFotoProp, self).__init__(name, location, shapefile)

        self.addProp(DBKStrProp("naam", location, shapefile, naamfldname)),
        self.addProp(DBKStrProp("URL", location, shapefile, urlfldname))
        self.addProp(DBKConstProp("filetype", None))

#-------------------------------------------------------------------------------
# DBKGevaarStofProp: Gevaarlijke stof
class DBKGevaarStofProp(DBKMultiProp):
    def __init__(self, name, location, shapefile, joinfldname, naamfldname, gevifldname, UNfldname,  typefldname, hoeveelheidfldname, infofldname, domein=None):
        super(DBKGevaarStofProp, self).__init__(name, location, shapefile, joinfldname)

        self.addProp(DBKStrProp("naamStof", location, shapefile, naamfldname))
        self.addProp(DBKStrProp("gevaarsindicatienummer", location, shapefile, gevifldname))
        self.addProp(DBKStrProp("UNnummer", location, shapefile, UNfldname))
        self.addProp(DBKStrProp("hoeveelheid", location, shapefile, hoeveelheidfldname))
        #self.addProp(DBKSymbProp("symboolCode", location, shapefile, typefldname))
        self.addProp(DBKSymbProp("symboolCode", location, shapefile, typefldname, domein, "symboolcode"))
        self.addProp(DBKSymbProp("namespace", location, shapefile, typefldname, domein, "namespace"))
        self.addProp(DBKStrProp("aanvullendeInformatie", location, shapefile, infofldname))
        self.addProp(DBKGeomProp())

#-------------------------------------------------------------------------------
# DBKHulplijnDomProp: Hulplijn
# Hulplijn waarbij op basis van type-veld het typeHulplijn wordt bepaald.
class DBKHulplijnDomProp(DBKMultiProp):
    def __init__(self, name, location, shapefile, joinfldname, typefldname, bijzfldname, opmfldname, domein=None):
        super(DBKHulplijnDomProp, self).__init__(name, location, shapefile, joinfldname)

        self.addProp(DBKSymbProp("typeHulplijn", location, shapefile, typefldname, domein, "typeHulplijn"))
        self.addProp(DBKMultiFieldProp("aanvullendeInformatie", location, shapefile, [bijzfldname, opmfldname]))
        self.addProp(DBKGeomProp())

#-------------------------------------------------------------------------------
# DBKHulplijnConstProp: Hulplijn
# Hulplijn van 1 type.
class DBKHulplijnConstProp(DBKMultiProp):
    def __init__(self, name, location, shapefile, joinfldname, bijzfldname, typeHulplijn):
        super(DBKHulplijnConstProp, self).__init__(name, location, shapefile, joinfldname)

        self.addProp(DBKConstProp("typeHulplijn", typeHulplijn))
        self.addProp(DBKStrProp("aanvullendeInformatie", location, shapefile, bijzfldname))
        self.addProp(DBKGeomProp())

#-------------------------------------------------------------------------------
class DBKTekstProp(DBKMultiProp):
    def __init__(self, name, location, shapefile, joinfldname, tekstfldname, hoekfldname, schaalfldname):
        super(DBKTekstProp, self).__init__(name, location, shapefile, joinfldname)

        self.addProp(DBKStrProp("tekst", location, shapefile, tekstfldname)),
        self.addProp(DBKHoekProp("hoek", location, shapefile, hoekfldname, -90))
        self.addProp(DBKIntProp("schaal", location, shapefile, schaalfldname))
        self.addProp(DBKGeomProp())

#-------------------------------------------------------------------------------
class DBKPandgeometrieProp(DBKMultiProp):
    def __init__(self, name, location, shapefile, joinfldname, pandidfldname, statusfldname):
        super(DBKPandgeometrieProp, self).__init__(name, location, shapefile, joinfldname)

        self.addProp(DBKStrProp("bagId", location, shapefile, "BAGPAND_ID"))
        self.addProp(DBKStrProp("bagStatus", location, shapefile, "STATUS_BAG"))
        self.addProp(DBKGeomProp())

#-------------------------------------------------------------------------------
class DBKToegangTerreinProp(DBKMultiProp):
    def __init__(self, name, location, shapefile, joinfldname, infofldname):
        super(DBKToegangTerreinProp, self).__init__(name, location, shapefile, joinfldname)

        self.addProp(DBKConstProp("primair", False))
        self.addProp(DBKConstProp("naamRoute", None))
        self.addProp(DBKStrProp("aanvullendeInformatie", location, shapefile, infofldname))
        self.addProp(DBKGeomProp())

#-------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
