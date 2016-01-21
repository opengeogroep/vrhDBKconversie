#-------------------------------------------------------------------------------
# Name:        DBKDomeinen
# Purpose:     Vastleggen domeinen DBK t.b.v. conversie Haaglanden database.
#
# Author:      Anke Keuren (ARIS B.V.)
#
# Created:     25-06-2015
# Changes:     12-10-2015, AK:
#              - Domein voor opstelplaats toegevoegd en codes Tb1.008, Tb1.009 en
#                Tb1.010 daarin gezet. Dit ivm dubbel voorkomen van Tb1.010 in
#                de Haaglanden-database. Tb1.010 wordt voor opstelplaats redvoertuig
#                en voor Schacht gebruikt. Door het domein van opstelplaatsen
#                apart te definieren, kan Tb1.010 voor Schacht worden vertaald
#                naar code Falck11.
#              04-11-2015, AK:
#              - Gevaren naar domein brandweervoorziening gekopieerd.
#              06-11-2015, AK:
#              - Gevaar Tw03 als brandweervoorziening converteren naar TwTemp.
#              - TypeHulplijn Binnenmuur convertereren naar Binnenmuur.
#-------------------------------------------------------------------------------

class DBKDomein(object):
    def __init__(self, domein):
        self._domein = domein

    def value(self, key, fieldname):
        if self._domein:
            if key in self._domein:
                row = self._domein[key]
                if fieldname in row:
                    return row[fieldname]
                else:
                    return None
            else:
                return None
        else:
            return None

class DBKDBrandweervoorziening(DBKDomein):
    def __init__(self):
        d = {"Tbk7.004":{"symboolcode":"Tbk7.004","naam":"Lift","namespace":"NEN1414","categorie":"objectinformatie"},
		"Tw01":{"symboolcode":"Tw01","naam":"Algemeen gevaar","namespace":"NEN1414","categorie":"repressief"},
		"Trap2":{"symboolcode":"Trap2","naam":"Trap","namespace":"Other","categorie":"preventief"},
		"Tb1.005":{"symboolcode":"Tb1.005","naam":"Nevenbrandweerpaneel","namespace":"NEN1414","categorie":"preventief"},
		"Tn06":{"symboolcode":"Tn06","naam":"Verzamelplaats","namespace":"NEN1414","categorie":"preventief"},
		"Tb1.007":{"symboolcode":"Tb1.007","naam":"Droge blusleiding","namespace":"NEN1414","categorie":"preventief"},
		"Tbk5.001":{"symboolcode":"Tbk5.001","naam":"Brandweerlift","namespace":"NEN1414","categorie":"preventief"},
		"Tb4.021":{"symboolcode":"Tb4.021","naam":"Blussysteem AFFF","namespace":"NEN1414","categorie":"preventief"},
		"Tb4.022":{"symboolcode":"Tb4.022","naam":"Blussysteem schuim","namespace":"NEN1414","categorie":"preventief"},
		"Tb4.023":{"symboolcode":"Tb4.023","naam":"Blussysteem water","namespace":"NEN1414","categorie":"preventief"},
		"Tb4.024":{"symboolcode":"Tb4.024","naam":"Blussysteem kooldioxide","namespace":"NEN1414","categorie":"preventief"},
		"Tb4.025":{"symboolcode":"Tb4.025","naam":"Blussysteem Hi Fog","namespace":"NEN1414","categorie":"preventief"},
		"Tbk5.002":{"symboolcode":"Tbk5.002","naam":"Brandwerende scheiding van 60 minuten","namespace":"NEN1414","categorie":"preventief"},
		"CAI":{"symboolcode":"CAI","naam":"Aansluiting CAI","namespace":"Other","categorie":""},
		"Signal":{"symboolcode":"Signal","naam":"Signaal","namespace":"Other","categorie":""},
		"Sewer":{"symboolcode":"Sewer","naam":"Toegang riool","namespace":"Other","categorie":""},
		"Tbk5.003":{"symboolcode":"Tbk5.003","naam":"Brandwerende scheiding van 30 minuten","namespace":"NEN1414","categorie":"preventief"},
		"Tbk5.004":{"symboolcode":"Tbk5.004","naam":"Rookwerende scheiding","namespace":"NEN1414","categorie":"preventief"},
		"Tb1.004":{"symboolcode":"Tb1.004","naam":"Brandweerpaneel","namespace":"NEN1414","categorie":"preventief"},
		"Tb1.004a":{"symboolcode":"Tb1.004a","naam":"Brandmeldcentrale","namespace":"NEN1414","categorie":"preventief"},
		"C2000":{"symboolcode":"C2000","naam":"C2000","namespace":"Other","categorie":"preparatief"},
		"Openwater":{"symboolcode":"Openwater","naam":"Open water","namespace":"Other","categorie":"preparatief"},
		"Tb1.001":{"symboolcode":"Tb1.001","naam":"Brandweeringang","namespace":"NEN1414","categorie":"preparatief"},
		"Tb1.002":{"symboolcode":"Tb1.002","naam":"Overige ingangen","namespace":"NEN1414","categorie":"preparatief"},
		"Tb1.003":{"symboolcode":"Tb1.003","naam":"Sleutelkluis","namespace":"NEN1414","categorie":"preparatief"},
		"Tb2.003":{"symboolcode":"Tb2.003","naam":"Schakelaar elektriciteit","namespace":"NEN1414","categorie":"preparatief"},
		"Tb2.021":{"symboolcode":"Tb2.021","naam":"Afsluiter gas","namespace":"NEN1414","categorie":"preparatief"},
		"Tb2.022":{"symboolcode":"Tb2.022","naam":"Afsluiter water","namespace":"NEN1414","categorie":"preparatief"},
		"Tb2.001":{"symboolcode":"Tb2.001","naam":"Noodschakelaar neon","namespace":"NEN1414","categorie":"preparatief"},
		"Tb2.005":{"symboolcode":"Tb2.005","naam":"Schakelaar rook-/warmteafvoer","namespace":"NEN1414","categorie":"preparatief"},
		"Tb2.004":{"symboolcode":"Tb2.004","naam":"Schakelaar luchtbehandeling","namespace":"NEN1414","categorie":"preparatief"},
		"Tb2.023":{"symboolcode":"Tb2.023","naam":"Afsluiter sprinkler","namespace":"NEN1414","categorie":"preparatief"},
		"Tb2.041":{"symboolcode":"Tb2.041","naam":"Activering blussysteem","namespace":"NEN1414","categorie":"preparatief"},
		"Tb2.042":{"symboolcode":"Tb2.042","naam":"Schakelkast elektriciteit","namespace":"NEN1414","categorie":"preparatief"},
		"Tb4.003":{"symboolcode":"Tb4.003","naam":"Geboorde put","namespace":"NEN1414","categorie":"preparatief"},
		"Falck13":{"symboolcode":"Falck13","naam":"Flitslicht","namespace":"Other","categorie":"preparatief"},
		"Tb2.043":{"symboolcode":"Tb2.043","naam":"Noodstop","namespace":"NEN1414","categorie":"preparatief"},
		"Falck14":{"symboolcode":"Falck14","naam":"Brandweervoorziening","namespace":"Other","categorie":"preparatief"},
		"Falck15":{"symboolcode":"Falck15","naam":"PGS 15 Kluis","namespace":"Other","categorie":"preparatief"},
		"Falck12":{"symboolcode":"Falck12","naam":"Rook Warmte Afvoerluiken","namespace":"Other","categorie":"preventief"},
		"Tb1.010":{"symboolcode":"Falck11","naam":"Schacht of kanaal","namespace":"Other","categorie":"objectinformatie"},
		"Tb1.007a":{"symboolcode":"Tb.1007a","naam":"Afname Droge Buisleiding","namespace":"NEN1414","categorie":"preventief"},
		"Tb4.001":{"symboolcode":"Tb4.001","naam":"Hydrant","namespace":"NEN1414","categorie":"preparatief"},
		"Tb4.002":{"symboolcode":"Tb4.002","naam":"Ondergrondse brandkraan","namespace":"NEN1414","categorie":"preparatief"},
		"Tb2.002":{"symboolcode":"Tb2.002","naam":"Noodschakelaar CV","namespace":"NEN1414","categorie":"preparatief"},
		"Falck17":{"symboolcode":"Falck17","naam":"Trap wokkel","namespace":"Other","categorie":"preventief"},
		"Falck16":{"symboolcode":"Falck16","naam":"Trap standaard","namespace":"Other","categorie":"preventief"},
		"Falck18":{"symboolcode":"Falck18","naam":"Open water deze zijde","namespace":"Other","categorie":"preparatief"},
		"Falck19":{"symboolcode":"Falck19","naam":"Bluswaterriool","namespace":"Other","categorie":"preparatief"},
		"Falck20":{"symboolcode":"Falck20","naam":"Open water bereikbaar","namespace":"Other","categorie":"preparatief"},
        "Tb02":{"symboolcode":"Tb02","naam":"Brandslanghaspel", "namespace": "NEN1414","categorie":""},
        "To02":{"symboolcode":"To02","naam":"Slaapplaats", "namespace": "NEN1414","categorie":""},
        "To03":{"symboolcode":"To03","naam":"Noodstroom aggregaat", "namespace": "NEN1414","categorie":""},
        "To04":{"symboolcode":"To04","naam":"Brandweerinfokast", "namespace": "NEN1414","categorie":""},
        "Tb2.024":{"symboolcode":"Tb2.024","naam":"Afsluiter omloopleiding", "namespace": "NEN1414","categorie":"preparatief"},
        "Tb2.025":{"symboolcode":"Tb2.025","naam":"Afsluiter LPG", "namespace": "NEN1414","categorie":"preparatief"},
        "Tb2.026":{"symboolcode":"Tb2.026","naam":"Afsluiter schuimvormend middel", "namespace": "NEN1414","categorie":"preparatief"},
        "Tb1.011":{"symboolcode":"Tb1.011","naam":"Gas detectiepaneel", "namespace": "NEN1414","categorie":"preventief"},
        "Tb4.005":{"symboolcode":"Tb4.005","naam":"Gesprinklerde ruimte", "namespace": "NEN1414","categorie":""},
        "Tn05":{"symboolcode":"Tn05","naam":"Nooduitgang", "namespace": "NEN1414","categorie":""},
        "Tn504":{"symboolcode":"Tr504","naam":"Indicator/flitslicht", "namespace": "NEN1414","categorie":""},
        "To1.001":{"symboolcode":"To1.001","naam":"Trap", "namespace": "NEN1414","categorie":"preventief"},
        "To1.002":{"symboolcode":"To1.002","naam":"Trap rond", "namespace": "NEN1414","categorie":"preventief"},
        "To1.003":{"symboolcode":"To1.003","naam":"Trappenhuis", "namespace": "NEN1414","categorie":"preventief"},
        "Tbe05":{"symboolcode":"Tbe05","naam":"Niet toegankelijk", "namespace": "NEN1414","categorie":""},
        "Tbe01":{"symboolcode":"Tbe01","naam":"Sleutel of ring paal", "namespace": "NEN1414","categorie":""},
        "Tbe02":{"symboolcode":"Tbe02","naam":"Poller", "namespace": "NEN1414","categorie":""},
        "TbeRIJ":{"symboolcode":"TbeRIJ","naam":"Berijdbaar", "namespace": "NEN1414","categorie":""},
        "Tbe06":{"symboolcode":"Tbe06","naam":"Parkeerplaats", "namespace": "NEN1414","categorie":""},
        "TbeBus":{"symboolcode":"TbeBus","naam":"Bussluis", "namespace": "NEN1414","categorie":""},
        "TbeHoogte":{"symboolcode":"TbeHoogte","naam":"Doorrijhoogte", "namespace": "NEN1414","categorie":""},
        "Falck36":{"symboolcode":"Falck36","naam":"Hellingbaan","namespace":"Other","categorie":"objectinformatie"},
        "Tw09":{"symboolcode":"Tw09","naam":"Radioactief Materiaal","namespace":"NEN1414","categorie":""},
        "Tw10":{"symboolcode":"Tw10","naam":"Laserstralen","namespace":"NEN1414","categorie":""},
        "Tw11":{"symboolcode":"Tw11","naam":"Niet-ioniserende Straling","namespace":"NEN1414","categorie":""},
        "Tw12":{"symboolcode":"Tw12","naam":"Magnetisch Veld","namespace":"NEN1414","categorie":""},
        "Tw14":{"symboolcode":"Tw14","naam":"Vallen door Hoogteverschil","namespace":"NEN1414","categorie":""},
        "Tw15":{"symboolcode":"Tw15","naam":"Biologische Agentia","namespace":"NEN1414","categorie":""},
        "Tw16":{"symboolcode":"Tw16","naam":"Lage temperatuur of bevriezing","namespace":"NEN1414","categorie":""},
        "Tw19":{"symboolcode":"Tw19","naam":"Explosieve atmosfeer","namespace":"NEN1414","categorie":""},
        "Tw28":{"symboolcode":"Tw28","naam":"Accus en klein chemisch materiaal","namespace":"NEN1414","categorie":""},
        "Tw02":{"symboolcode":"Tw02","naam":"Electrische Spanning","namespace":"NEN1414","categorie":""},
        "Tw08":{"symboolcode":"Tw08","naam":"Explosief","namespace":"NEN1414","categorie":""},
        "Tw03":{"symboolcode":"TwTemp","naam":"Temperatuur","namespace":"NEN1414","categorie":""},
        "Tw07":{"symboolcode":"Tw07","naam":"Brand bevorderend (oxiderend)","namespace":"NEN1414","categorie":""},
        "Tw05":{"symboolcode":"Tw05","naam":"Corrosief (bijtend)","namespace":"NEN1414","categorie":""},
        "Tw04":{"symboolcode":"Tw04","naam":"Toxisch (giftig)","namespace":"NEN1414","categorie":""},
        "Tw21":{"symboolcode":"Tw21","naam":"Niet blussen met water","namespace":"NEN1414","categorie":""},
        "Tw22":{"symboolcode":"Tw22","naam":"Markering lab laag risico","namespace":"NEN1414","categorie":""},
        "Tw23":{"symboolcode":"Tw23","naam":"Markering lab middel risico","namespace":"NEN1414","categorie":""},
        "Tw24":{"symboolcode":"Tw24","naam":"Markering lab hoog risico","namespace":"NEN1414","categorie":""},
        "Tw01":{"symboolcode":"Tw01","naam":"Algemeen gevaar","namespace":"NEN1414","categorie":""}
}

        super(DBKDBrandweervoorziening, self).__init__(d)

class DBKDOpstelplaats(DBKDomein):
    def __init__(self):
        d = {"Tb1.008":{"symboolcode":"Tb1.008","naam":"Opstelplaats eerste blusvoertuig","namespace":"NEN1414","categorie":"repressief"},
		"Tb1.009":{"symboolcode":"Tb1.009","naam":"Opstelplaats overige blusvoertuigen","namespace":"NEN1414","categorie":"repressief"},
        "Tb1.010":{"symboolcode":"Tb1.010","naam":"Opstelplaats redvoertuig", "namespace": "NEN1414","categorie":"repressief"}}

        super(DBKDOpstelplaats, self).__init__(d)

class DBKDBrandcompartiment(DBKDomein):
    def __init__(self):
        #d = {"":"Scheiding (algemeen)","Tbk5.002":"60 minuten brandwerende scheiding","Tbk5.003":"30 minuten brandwerende scheiding","Tbk5.004":"Rookwerende scheiding","Tbk5.005":"> 60 minuten brandwerende scheiding"}
        d = {"":{"symboolcode":"","naam":"Scheiding (algemeen)"},
		"Tbk5.002":{"symboolcode":"Tbk5.002","naam":"60 minuten brandwerende scheiding"},
		"Tbk5.003":{"symboolcode":"Tbk5.003","naam":"30 minuten brandwerende scheiding"},
		"Tbk5.000":{"symboolcode":"Tbk5.000","naam":"Rookwerende scheiding"},
		"Tbk5.005":{"symboolcode":"Tbk5.005","naam":"> 60 minuten brandwerende scheiding"},
    "Tbk5.120":{"symboolcode":"Tbk5.120","naam":"> 120 minuten brandwerende scheiding"}}

        super(DBKDBrandcompartiment, self).__init__(d)

class DBKDGevaarlijkestof(DBKDomein):
    def __init__(self):
        #d = {"Tw2.002":"NFPA-gevarendiamant","EU-GHS01":"Explosief","EU-GHS02":"Ontvlambaar","EU-GHS03":"Brand bevorderend (oxiderend)","EU-GHS04":"Houder onder druk","EU-GHS05":"Corrosief (bijtend)","EU-GHS06":"Toxisch (giftig)","EU-GHS07":"Schadelijk","EU-GHS08":"Schadelijk voor de gezondheid op lange termijn","EU-GHS09":"Milieugevaarlijk","Tw09":"Radioactief Materiaal","Tw10":"Laserstralen","Tw11":"Niet-ioniserende Straling","Tw12":"Magnetisch Veld","Tw14":"Vallen door Hoogteverschil","Tw15":"Biologische Agentia","Tw16":"Lage temperatuur of bevriezing","Tw19":"Explosieve atmosfeer","Tw28":"Accus en klein chemisch materiaal","Tw02":"Electrische Spanning"}
        d = {"Tw2.002":{"symboolcode":"Tw2.002","naam":"NFPA-gevarendiamant","namespace":"NEN1414"},
        "EU-GHS01":{"symboolcode":"EU-GHS01","naam":"Explosief","namespace":"EU-GHS"},
        "EU-GHS02":{"symboolcode":"EU-GHS02","naam":"Ontvlambaar","namespace":"EU-GHS"},
        "EU-GHS03":{"symboolcode":"EU-GHS03","naam":"Brand bevorderend (oxiderend)","namespace":"EU-GHS"},
        "EU-GHS04":{"symboolcode":"EU-GHS04","naam":"Houder onder druk","namespace":"EU-GHS"},
        "EU-GHS05":{"symboolcode":"EU-GHS05","naam":"Corrosief (bijtend)","namespace":"EU-GHS"},
        "EU-GHS06":{"symboolcode":"EU-GHS06","naam":"Toxisch (giftig)","namespace":"EU-GHS"},
        "EU-GHS07":{"symboolcode":"EU-GHS07","naam":"Schadelijk","namespace":"EU-GHS"},
        "EU-GHS08":{"symboolcode":"EU-GHS08","naam":"Schadelijk voor de gezondheid op lange termijn","namespace":"EU-GHS"},
        "EU-GHS09":{"symboolcode":"EU-GHS09","naam":"Milieugevaarlijk","namespace":"EU-GHS"},
        "Tw09":{"symboolcode":"Tw09","naam":"Radioactief Materiaal","namespace":"NEN1414"},
        "Tw10":{"symboolcode":"Tw10","naam":"Laserstralen","namespace":"NEN1414"},
        "Tw11":{"symboolcode":"Tw11","naam":"Niet-ioniserende Straling","namespace":"NEN1414"},
        "Tw12":{"symboolcode":"Tw12","naam":"Magnetisch Veld","namespace":"NEN1414"},
        "Tw14":{"symboolcode":"Tw14","naam":"Vallen door Hoogteverschil","namespace":"NEN1414"},
        "Tw15":{"symboolcode":"Tw15","naam":"Biologische Agentia","namespace":"NEN1414"},
        "Tw16":{"symboolcode":"Tw16","naam":"Lage temperatuur of bevriezing","namespace":"NEN1414"},
        "Tw19":{"symboolcode":"Tw19","naam":"Explosieve atmosfeer","namespace":"NEN1414"},
        "Tw28":{"symboolcode":"Tw28","naam":"Accus en klein chemisch materiaal","namespace":"NEN1414"},
        "Tw02":{"symboolcode":"Tw02","naam":"Electrische Spanning","namespace":"NEN1414"},
        "Tw08":{"symboolcode":"Tw08","naam":"Explosief","namespace":"NEN1414"},
        "Tw03":{"symboolcode":"Tw03","naam":"Ontvlambaar","namespace":"NEN1414"},
        "Tw07":{"symboolcode":"Tw07","naam":"Brand bevorderend (oxiderend)","namespace":"NEN1414"},
        "Tw05":{"symboolcode":"Tw05","naam":"Corrosief (bijtend)","namespace":"NEN1414"},
        "Tw04":{"symboolcode":"Tw04","naam":"Toxisch (giftig)","namespace":"NEN1414"},
        "Tw21":{"symboolcode":"Tw21","naam":"Niet blussen met water","namespace":"NEN1414"},
        "Tw22":{"symboolcode":"Tw22","naam":"Markering lab laag risico","namespace":"NEN1414"},
        "Tw23":{"symboolcode":"Tw23","naam":"Markering lab middel risico","namespace":"NEN1414"},
        "Tw24":{"symboolcode":"Tw24","naam":"Markering lab hoog risico","namespace":"NEN1414"},
        "Tw01":{"symboolcode":"Tw01","naam":"Algemeen gevaar","namespace":"NEN1414"}
        }

        super(DBKDGevaarlijkestof, self).__init__(d)

class DBKDHulplijn(DBKDomein):
    def __init__(self):
        d = {"Binnenmuur":{"typeHulplijn":"Binnenmuur"},
        "Aanrijroute":{"typeHulplijn":"Line"},
        "Blusleiding":{"typeHulplijn":"DBL Leiding"},
        "Hekwerk":{"typeHulplijn":"Fence"},
        "Inzetdiepte":{"typeHulplijn":""},
        "Schadecirkel":{"typeHulplijn":"HEAT"},
        "Vluchtroute":{"typeHulplijn":""},
        "Slagboom":{"typeHulplijn":"Bbarrier"},
        "Aanpijling":{"typeHulplijn":"Line"}}

        super(DBKDHulplijn, self).__init__(d)
