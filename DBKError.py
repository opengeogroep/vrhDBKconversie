#-------------------------------------------------------------------------------
# Name:        DBKError
# Purpose:     Several types of errors
#
# Author:      Anke Keuren (ARIS)
#
# Created:     15-07-2015
# Copyright:   (c) ARIS B.V. 2015
#-------------------------------------------------------------------------------

class DBKError(Exception):
    def __init__(self, msg):
        self.message = msg

    def __str__(self):
        return self.message

class DirectoryError(DBKError):
    def __init__(self, dirname):
        self.message = "Directory {0} does not exist.".format(dirname)

class FileError(DBKError):
    def __init__(self, filename):
        self.message = "File {0} does not exist.".format(filename)

class FieldError(DBKError):
    def __init__(self, fieldname, shapefile):
        self.message = "Field {0} does not exist in shapefile {1}.".format(fieldname, shapefile)

class MappingError(DBKError):
    def __init__(self, fieldname, shapefile, element):
        self.message = "Field {0} does not exist in shapefile {1}. Waarden voor element {2} kunnen niet worden ingevuld.".format(fieldname, shapefile, element)

class ShapefileError(DBKError):
    def __init__(self, filename):
        self.message = "File {0} is not a shapefile.".format(filename)

class DatasetError(DBKError):
    def __init__(self, dataset):
        self.message = "Dataset {0} does not exist.".format(dataset)

class WorkspaceError(DBKError):
    def __init__(self, workspace):
        self.message = "Workspace {0} does not exist.".format(workspace)
