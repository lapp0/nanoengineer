
LIBS += -lopenbabel \
 -L../../../lib \
 -lNanorexUtility

HEADERS += \
../../../include/Nanorex/Interface/NXDataImportExportPlugin.h \
 ../../../include/Nanorex/Interface/NXDataStoreInfo.h \
 ../../../include/Nanorex/Interface/NXEntityManager.h \
 ../../../include/Nanorex/Interface/NXMoleculeData.h \
 ../../../include/Nanorex/Interface/NXMoleculeSet.h \
 ../../../include/Nanorex/Interface/NXNanoVisionResultCodes.h \
 ../../../include/Nanorex/Interface/NXNumbers.h \
 ../../../include/Nanorex/Interface/NXAtomRenderData.h \
 ../../../include/Nanorex/Interface/NXBondRenderData.h

INCLUDEPATH += ../../../include \
 $(OPENBABEL_INCPATH)

SOURCES += ../../Interface/NXDataImportExportPlugin.cpp \
 ../../Interface/NXDataStoreInfo.cpp \
 ../../Interface/NXEntityManager.cpp \
 ../../Interface/NXMoleculeData.cpp \
 ../../Interface/NXMoleculeSet.cpp \
 ../../Interface/NXNumbers.cpp \
 ../../Interface/NXAtomRenderData.cpp \
 ../../Interface/NXBondRenderData.cpp \
 ../../Interface/NXNanoVisionResultCodes.cpp

TEMPLATE = lib

CONFIG += dll \
 debug \
 stl

TARGET = NanorexInterface

DESTDIR = ../../../lib

TARGETDEPS += ../../../lib/libNanorexUtility.so

CONFIG -= release
QT -= gui

