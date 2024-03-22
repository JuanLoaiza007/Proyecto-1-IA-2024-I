# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/ihuntgore/Escritorio/proyectos/ia/Proyecto-IA-2024-1/views/vista_juego.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setStyleSheet("/*\n"
" *\n"
" *  Simple Stylesheet inspired on Bootstrap for Qt Designer / Qt Creator \n"
" *  File: bootstylesheet.css\n"
" *  Author: JuanLoaiza007\n"
" *  Version: 1.1.1\n"
" *\n"
" */\n"
"\n"
"/*  # Español\n"
" *  Instrucciones para aplicar en Qt Designer / Qt Creator\n"
" *  1. Busque la vista de Inspector de objetos >> Objeto >> \"MainWindow\".\n"
" *  2. Dale clic derecho a \"MainWindow\" y seleccione \"Cambiar HojaDeEstilos\" o algo similar.\n"
" *  3. Pegue el contenido de este archivo ahí.\n"
" *  4. De clic en Aplicar y Aceptar.\n"
" *  5. Para aplicar los estilos seleccione un objeto, en el Editor de Propiedades agregue un Filtro tipo cadena de texto y nombrelo \"class\".\n"
" *  6. En el Editor de Propiedades habrá una seccion nueva llamada \"Propiedades dinámicas\" y una propiedad llamada \"class\", en la casilla de la derecha aplique todos los estilos que desee, eg. \"btn btn-outline-primary br-4\". \n"
" */\n"
"\n"
"/*  # English\n"
" *  Instructions to apply in Qt Designer / Qt Creator\n"
" *  1. Keep an eye on the Object Inspector >> Object >> \"MainWindow\".\n"
" *  2. Right click on \"MainWindow\" and select \"Change StyleSheet\" or something similar.\n"
" *  3. Paste the content of this file there.\n"
" *  4. Click Apply and Accept.\n"
" *  5. To apply the styles, select an object, in the Properties Editor add a Text String Filter and name it \"class\".\n"
" *  6. In the Property Editor there will be a new section called \"Dynamic Properties\" and a property called \"class\", in the box on the right apply all the styles you want, eg. \"btn btn-outline-primary br-4\". \n"
" */\n"
"\n"
"QMainWindow {\n"
"  font-family: \"sans-serif\";\n"
"}\n"
"\n"
"/* Border Settings */\n"
"/* Border Side Weight */\n"
".nb {\n"
"  border: 0px solid;\n"
"}\n"
".b-st-1 {\n"
"  border-top: 1px solid;\n"
"}\n"
".b-sb-1 {\n"
"  border-bottom: 1px solid;\n"
"}\n"
".b-sl-1 {\n"
"  border-left: 1px solid;\n"
"}\n"
".b-sr-1 {\n"
"  border-right: 1px solid;\n"
"}\n"
".b-st-2 {\n"
"  border-top: 2px solid;\n"
"}\n"
".b-sb-2 {\n"
"  border-bottom: 2px solid;\n"
"}\n"
".b-sl-2 {\n"
"  border-left: 2px solid;\n"
"}\n"
".b-sr-2 {\n"
"  border-right: 2px solid;\n"
"}\n"
".b-st-3 {\n"
"  border-top: 3px solid;\n"
"}\n"
".b-sb-3 {\n"
"  border-bottom: 3px solid;\n"
"}\n"
".b-sl-3 {\n"
"  border-left: 3px solid;\n"
"}\n"
".b-sr-3 {\n"
"  border-right: 3px solid;\n"
"}\n"
".b-st-4 {\n"
"  border-top: 4px solid;\n"
"}\n"
".b-sb-4 {\n"
"  border-bottom: 4px solid;\n"
"}\n"
".b-sl-4 {\n"
"  border-left: 4px solid;\n"
"}\n"
".b-sr-4 {\n"
"  border-right: 4px solid;\n"
"}\n"
"\n"
"/* Radius */\n"
".br-1 {\n"
"  border-radius: 10px;\n"
"}\n"
"\n"
".br-2 {\n"
"  border-radius: 15px;\n"
"}\n"
"\n"
".br-3 {\n"
"  border-radius: 20px;\n"
"}\n"
"\n"
".br-4 {\n"
"  border-radius: 25px;\n"
"}\n"
"\n"
"/* Background colors */\n"
".background-white {\n"
"  background-color: white;\n"
"}\n"
".background-light {\n"
"  background-color: #f8f9fa;\n"
"}\n"
".background-black {\n"
"  background-color: black;\n"
"}\n"
".background-primary {\n"
"  background-color: #0d6efd;\n"
"}\n"
".background-success {\n"
"  background-color: #198754;\n"
"}\n"
".background-warning {\n"
"  background-color: #ffc720;\n"
"}\n"
".background-danger {\n"
"  background-color: #dc3545;\n"
"}\n"
"\n"
"/* Colors */\n"
".color-white {\n"
"  color: white;\n"
"}\n"
".color-light {\n"
"  color: #f8f9fa;\n"
"}\n"
".color-black {\n"
"  color: black;\n"
"}\n"
".color-primary {\n"
"  color: #0d6efd;\n"
"}\n"
".color-success {\n"
"  color: #198754;\n"
"}\n"
".color-warning {\n"
"  color: #ffc720;\n"
"}\n"
".color-danger {\n"
"  color: #dc3545;\n"
"}\n"
"\n"
"/* Buttons */\n"
"QPushButton {\n"
"  font-weight: 500;\n"
"  color: white;\n"
"  background-color: gray;\n"
"  padding: 6px 12px;\n"
"  font-size: 18px;\n"
"  border-radius: 10px;\n"
"  border: 1px solid;\n"
"}\n"
"\n"
".btn {\n"
"  font-weight: 500;\n"
"  color: white;\n"
"  background-color: gray;\n"
"  padding: 6px 12px;\n"
"  font-size: 18px;\n"
"  border-radius: 10px;\n"
"  border: 1px solid;\n"
"}\n"
"\n"
".btn-primary {\n"
"  color: #fff;\n"
"  background-color: #0d6efd;\n"
"  border-color: #0d6efd;\n"
"}\n"
".btn-primary:hover {\n"
"  color: #fff;\n"
"  background-color: #0b5ed7;\n"
"  border-color: #0a58ca;\n"
"}\n"
"\n"
".btn-secondary {\n"
"  color: #fff;\n"
"  background-color: #6c757d;\n"
"  border-color: #6c757d;\n"
"}\n"
".btn-secondary:hover {\n"
"  color: #fff;\n"
"  background-color: #5c636a;\n"
"  border-color: #565e64;\n"
"}\n"
"\n"
".btn-success {\n"
"  color: #fff;\n"
"  background-color: #198754;\n"
"  border-color: #198754;\n"
"}\n"
".btn-success:hover {\n"
"  color: #fff;\n"
"  background-color: #157347;\n"
"  border-color: #146c43;\n"
"}\n"
"\n"
".btn-warning {\n"
"  color: #000;\n"
"  background-color: #ffc107;\n"
"  border-color: #ffc107;\n"
"}\n"
".btn-warning:hover {\n"
"  color: #000;\n"
"  background-color: #ffca2c;\n"
"  border-color: #ffc720;\n"
"}\n"
"\n"
".btn-danger {\n"
"  color: #fff;\n"
"  background-color: #dc3545;\n"
"  border-color: #dc3545;\n"
"}\n"
".btn-danger:hover {\n"
"  color: #fff;\n"
"  background-color: #bb2d3b;\n"
"  border-color: #b02a37;\n"
"}\n"
"\n"
".btn-light {\n"
"  color: #000;\n"
"  background-color: #f8f9fa;\n"
"  border-color: #f8f9fa;\n"
"}\n"
".btn-light:hover {\n"
"  color: #000;\n"
"  background-color: #f9fafb;\n"
"  border-color: #f9fafb;\n"
"}\n"
"\n"
".btn-dark {\n"
"  color: #fff;\n"
"  background-color: #212529;\n"
"  border-color: #212529;\n"
"}\n"
".btn-dark:hover {\n"
"  color: #fff;\n"
"  background-color: #1c1f23;\n"
"  border-color: #1a1e21;\n"
"}\n"
"\n"
".btn-outline-primary {\n"
"  background-color: white;\n"
"  color: #0d6efd;\n"
"  border-color: #0d6efd;\n"
"}\n"
".btn-outline-primary:hover {\n"
"  color: #fff;\n"
"  background-color: #0d6efd;\n"
"  border-color: #0d6efd;\n"
"}\n"
"\n"
".btn-outline-secondary {\n"
"  background-color: white;\n"
"  color: #6c757d;\n"
"  border-color: #6c757d;\n"
"}\n"
".btn-outline-secondary:hover {\n"
"  color: #fff;\n"
"  background-color: #6c757d;\n"
"  border-color: #6c757d;\n"
"}\n"
"\n"
".btn-outline-success {\n"
"  background-color: white;\n"
"  color: #198754;\n"
"  border-color: #198754;\n"
"}\n"
".btn-outline-success:hover {\n"
"  color: #fff;\n"
"  background-color: #198754;\n"
"  border-color: #198754;\n"
"}\n"
"\n"
".btn-outline-info {\n"
"  background-color: white;\n"
"  color: #0dcaf0;\n"
"  border-color: #0dcaf0;\n"
"}\n"
".btn-outline-info:hover {\n"
"  color: #000;\n"
"  background-color: #0dcaf0;\n"
"}\n"
"\n"
".btn-outline-warning {\n"
"  background-color: white;\n"
"  color: #ffc107;\n"
"  border-color: #ffc107;\n"
"}\n"
".btn-outline-warning:hover {\n"
"  color: #000;\n"
"  background-color: #ffc107;\n"
"  border-color: #ffc107;\n"
"}\n"
"\n"
".btn-outline-danger {\n"
"  background-color: white;\n"
"  color: #dc3545;\n"
"  border-color: #dc3545;\n"
"}\n"
".btn-outline-danger:hover {\n"
"  color: #fff;\n"
"  background-color: #dc3545;\n"
"  border-color: #dc3545;\n"
"}\n"
"\n"
".btn-outline-light {\n"
"  background-color: #41464b;\n"
"  color: #f8f9fa;\n"
"  border-color: #f8f9fa;\n"
"}\n"
".btn-outline-light:hover {\n"
"  color: #000;\n"
"  background-color: #f8f9fa;\n"
"  border-color: #f8f9fa;\n"
"}\n"
"\n"
".btn-outline-dark {\n"
"  background-color: white;\n"
"  color: #212529;\n"
"  border-color: #212529;\n"
"}\n"
".btn-outline-dark:hover {\n"
"  color: #fff;\n"
"  background-color: #212529;\n"
"  border-color: #212529;\n"
"}\n"
"\n"
".btn-link {\n"
"  background-color: white;\n"
"  font-weight: 400;\n"
"  color: #0d6efd;\n"
"  text-decoration: underline;\n"
"}\n"
".btn-link:hover {\n"
"  color: #0a58ca;\n"
"}\n"
"\n"
"/* Title sizes */\n"
"QLabel {\n"
"  font-size: 22px;\n"
"}\n"
"\n"
".h1 {\n"
"  font-size: 42px;\n"
"}\n"
"\n"
".h2 {\n"
"  font-size: 36px;\n"
"}\n"
"\n"
".h3 {\n"
"  font-size: 32px;\n"
"}\n"
"\n"
".h4 {\n"
"  font-size: 28px;\n"
"}\n"
"\n"
".h5 {\n"
"  font-size: 22px;\n"
"}\n"
"\n"
".h6 {\n"
"  font-size: 18px;\n"
"}\n"
"\n"
"/* Alerts */\n"
".alert {\n"
"  border: 1px solid;\n"
"}\n"
"\n"
".alert-primary {\n"
"  color: #084298;\n"
"  background-color: #cfe2ff;\n"
"  border-color: #b6d4fe;\n"
"}\n"
".alert-secondary {\n"
"  color: #41464b;\n"
"  background-color: #e2e3e5;\n"
"  border-color: #d3d6d8;\n"
"}\n"
".alert-success {\n"
"  color: #0f5132;\n"
"  background-color: #d1e7dd;\n"
"  border-color: #badbcc;\n"
"}\n"
".alert-info {\n"
"  color: #055160;\n"
"  background-color: #cff4fc;\n"
"  border-color: #b6effb;\n"
"}\n"
".alert-warning {\n"
"  color: #664d03;\n"
"  background-color: #fff3cd;\n"
"  border-color: #ffecb5;\n"
"}\n"
".alert-danger {\n"
"  color: #842029;\n"
"  background-color: #f8d7da;\n"
"  border-color: #f5c2c7;\n"
"}\n"
".alert-light {\n"
"  color: #636464;\n"
"  background-color: #fefefe;\n"
"  border-color: #fdfdfe;\n"
"}\n"
".alert-dark {\n"
"  color: #141619;\n"
"  background-color: #d3d3d4;\n"
"  border-color: #bcbebf;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(800, 80))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 80))
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lbl_titulo = QtWidgets.QLabel(self.frame)
        self.lbl_titulo.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_titulo.setObjectName("lbl_titulo")
        self.horizontalLayout_3.addWidget(self.lbl_titulo)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setMinimumSize(QtCore.QSize(800, 340))
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setMinimumSize(QtCore.QSize(100, 400))
        self.frame_4.setMaximumSize(QtCore.QSize(150, 16777215))
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.frame_2)
        self.frame_5.setMinimumSize(QtCore.QSize(500, 400))
        self.frame_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setProperty("class", "")
        self.frame_5.setObjectName("frame_5")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_9 = QtWidgets.QFrame(self.frame_5)
        self.frame_9.setMinimumSize(QtCore.QSize(50, 0))
        self.frame_9.setMaximumSize(QtCore.QSize(50, 16777215))
        self.frame_9.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_15 = QtWidgets.QFrame(self.frame_9)
        self.frame_15.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.verticalLayout_3.addWidget(self.frame_15)
        self.gridLayout.addWidget(self.frame_9, 0, 0, 3, 1)
        self.frame_11 = QtWidgets.QFrame(self.frame_5)
        self.frame_11.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_11)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.table_mapa = QtWidgets.QTableWidget(self.frame_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table_mapa.sizePolicy().hasHeightForWidth())
        self.table_mapa.setSizePolicy(sizePolicy)
        self.table_mapa.setMinimumSize(QtCore.QSize(0, 0))
        self.table_mapa.setMaximumSize(QtCore.QSize(850, 790))
        self.table_mapa.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.table_mapa.setFont(font)
        self.table_mapa.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.table_mapa.setFocusPolicy(QtCore.Qt.NoFocus)
        self.table_mapa.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.table_mapa.setFrameShadow(QtWidgets.QFrame.Plain)
        self.table_mapa.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.table_mapa.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.table_mapa.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.table_mapa.setAutoScroll(False)
        self.table_mapa.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table_mapa.setTabKeyNavigation(False)
        self.table_mapa.setProperty("showDropIndicator", False)
        self.table_mapa.setDragDropOverwriteMode(False)
        self.table_mapa.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.table_mapa.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.table_mapa.setTextElideMode(QtCore.Qt.ElideNone)
        self.table_mapa.setShowGrid(True)
        self.table_mapa.setWordWrap(True)
        self.table_mapa.setCornerButtonEnabled(False)
        self.table_mapa.setRowCount(0)
        self.table_mapa.setObjectName("table_mapa")
        self.table_mapa.setColumnCount(0)
        self.table_mapa.horizontalHeader().setVisible(True)
        self.table_mapa.horizontalHeader().setSortIndicatorShown(False)
        self.horizontalLayout_2.addWidget(self.table_mapa)
        self.gridLayout.addWidget(self.frame_11, 1, 1, 1, 1)
        self.frame_10 = QtWidgets.QFrame(self.frame_5)
        self.frame_10.setMinimumSize(QtCore.QSize(50, 0))
        self.frame_10.setMaximumSize(QtCore.QSize(50, 16777215))
        self.frame_10.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.gridLayout.addWidget(self.frame_10, 0, 2, 3, 1)
        self.frame_13 = QtWidgets.QFrame(self.frame_5)
        self.frame_13.setMinimumSize(QtCore.QSize(0, 20))
        self.frame_13.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_13.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.gridLayout.addWidget(self.frame_13, 2, 1, 1, 1)
        self.frame_12 = QtWidgets.QFrame(self.frame_5)
        self.frame_12.setMinimumSize(QtCore.QSize(0, 20))
        self.frame_12.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_12.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.gridLayout.addWidget(self.frame_12, 0, 1, 1, 1)
        self.horizontalLayout.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(self.frame_2)
        self.frame_6.setMinimumSize(QtCore.QSize(100, 400))
        self.frame_6.setMaximumSize(QtCore.QSize(150, 16777215))
        self.frame_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout.addWidget(self.frame_6)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setMinimumSize(QtCore.QSize(800, 60))
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_7 = QtWidgets.QFrame(self.frame_3)
        self.frame_7.setMinimumSize(QtCore.QSize(0, 20))
        self.frame_7.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_2.addWidget(self.frame_7)
        self.frame_8 = QtWidgets.QFrame(self.frame_3)
        self.frame_8.setMinimumSize(QtCore.QSize(0, 40))
        self.frame_8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_2.addWidget(self.frame_8)
        self.verticalLayout.addWidget(self.frame_3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.centralwidget.setProperty("class", _translate("MainWindow", "background-white"))
        self.lbl_titulo.setText(_translate("MainWindow", "TextLabel"))
        self.lbl_titulo.setProperty("class", _translate("MainWindow", "h1 color-primary"))
        self.frame_8.setProperty("class", _translate("MainWindow", "background-primary"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
