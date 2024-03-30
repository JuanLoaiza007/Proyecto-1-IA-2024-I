# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/ihuntgore/Escritorio/proyectos/ia/Proyecto-1-IA-2024-I/views/Vista_principal.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
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
"}\n"
"")
        MainWindow.setProperty("class", "")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.content = QtWidgets.QFrame(self.centralwidget)
        self.content.setMinimumSize(QtCore.QSize(800, 530))
        self.content.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.content.setObjectName("content")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.content)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.left_side = QtWidgets.QFrame(self.content)
        self.left_side.setMinimumSize(QtCore.QSize(576, 528))
        self.left_side.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.left_side.setFrameShadow(QtWidgets.QFrame.Raised)
        self.left_side.setObjectName("left_side")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.left_side)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.ls_header = QtWidgets.QFrame(self.left_side)
        self.ls_header.setMinimumSize(QtCore.QSize(576, 140))
        self.ls_header.setMaximumSize(QtCore.QSize(16777215, 140))
        self.ls_header.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.ls_header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ls_header.setObjectName("ls_header")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.ls_header)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lbl_titulo = QtWidgets.QLabel(self.ls_header)
        self.lbl_titulo.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_titulo.setObjectName("lbl_titulo")
        self.horizontalLayout_4.addWidget(self.lbl_titulo)
        self.verticalLayout_2.addWidget(self.ls_header)
        self.ls_body = QtWidgets.QFrame(self.left_side)
        self.ls_body.setMinimumSize(QtCore.QSize(520, 232))
        self.ls_body.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.ls_body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ls_body.setProperty("class", "")
        self.ls_body.setObjectName("ls_body")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.ls_body)
        self.verticalLayout_3.setContentsMargins(20, 0, 20, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_2 = QtWidgets.QFrame(self.ls_body)
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setProperty("class", "")
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lbl_tipo_busqueda = QtWidgets.QLabel(self.frame_2)
        self.lbl_tipo_busqueda.setMinimumSize(QtCore.QSize(310, 32))
        self.lbl_tipo_busqueda.setMaximumSize(QtCore.QSize(350, 32))
        self.lbl_tipo_busqueda.setObjectName("lbl_tipo_busqueda")
        self.verticalLayout_4.addWidget(self.lbl_tipo_busqueda)
        self.box_tipo_busqueda = QtWidgets.QComboBox(self.frame_2)
        self.box_tipo_busqueda.setMinimumSize(QtCore.QSize(310, 32))
        self.box_tipo_busqueda.setMaximumSize(QtCore.QSize(400, 32))
        self.box_tipo_busqueda.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.box_tipo_busqueda.setObjectName("box_tipo_busqueda")
        self.box_tipo_busqueda.addItem("")
        self.box_tipo_busqueda.addItem("")
        self.verticalLayout_4.addWidget(self.box_tipo_busqueda)
        self.lbl_algoritmo = QtWidgets.QLabel(self.frame_2)
        self.lbl_algoritmo.setMinimumSize(QtCore.QSize(310, 32))
        self.lbl_algoritmo.setMaximumSize(QtCore.QSize(350, 32))
        self.lbl_algoritmo.setObjectName("lbl_algoritmo")
        self.verticalLayout_4.addWidget(self.lbl_algoritmo)
        self.box_algoritmo = QtWidgets.QComboBox(self.frame_2)
        self.box_algoritmo.setMinimumSize(QtCore.QSize(310, 32))
        self.box_algoritmo.setMaximumSize(QtCore.QSize(400, 32))
        self.box_algoritmo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.box_algoritmo.setObjectName("box_algoritmo")
        self.verticalLayout_4.addWidget(self.box_algoritmo)
        self.lbl_estado_mundo = QtWidgets.QLabel(self.frame_2)
        self.lbl_estado_mundo.setObjectName("lbl_estado_mundo")
        self.verticalLayout_4.addWidget(self.lbl_estado_mundo)
        self.frame = QtWidgets.QFrame(self.frame_2)
        self.frame.setMaximumSize(QtCore.QSize(310, 16777215))
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_cargar_mundo = QtWidgets.QPushButton(self.frame)
        self.btn_cargar_mundo.setMinimumSize(QtCore.QSize(160, 40))
        self.btn_cargar_mundo.setMaximumSize(QtCore.QSize(160, 40))
        self.btn_cargar_mundo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_cargar_mundo.setObjectName("btn_cargar_mundo")
        self.horizontalLayout_3.addWidget(self.btn_cargar_mundo, 0, QtCore.Qt.AlignLeft)
        self.btn_iniciar = QtWidgets.QPushButton(self.frame)
        self.btn_iniciar.setMinimumSize(QtCore.QSize(130, 40))
        self.btn_iniciar.setMaximumSize(QtCore.QSize(130, 40))
        self.btn_iniciar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_iniciar.setObjectName("btn_iniciar")
        self.horizontalLayout_3.addWidget(self.btn_iniciar, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_4.addWidget(self.frame, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout_3.addWidget(self.frame_2)
        self.verticalLayout_2.addWidget(self.ls_body)
        self.ls_footer = QtWidgets.QFrame(self.left_side)
        self.ls_footer.setMinimumSize(QtCore.QSize(570, 100))
        self.ls_footer.setMaximumSize(QtCore.QSize(16777215, 120))
        self.ls_footer.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.ls_footer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ls_footer.setObjectName("ls_footer")
        self.verticalLayout_2.addWidget(self.ls_footer)
        self.horizontalLayout_2.addWidget(self.left_side)
        self.right_side = QtWidgets.QFrame(self.content)
        self.right_side.setMinimumSize(QtCore.QSize(221, 528))
        self.right_side.setMaximumSize(QtCore.QSize(300, 16777215))
        self.right_side.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.right_side.setFrameShadow(QtWidgets.QFrame.Raised)
        self.right_side.setProperty("class", "")
        self.right_side.setObjectName("right_side")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.right_side)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.lbl_side_image = QtWidgets.QLabel(self.right_side)
        self.lbl_side_image.setMinimumSize(QtCore.QSize(221, 528))
        self.lbl_side_image.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lbl_side_image.setText("")
        self.lbl_side_image.setObjectName("lbl_side_image")
        self.verticalLayout_7.addWidget(self.lbl_side_image)
        self.horizontalLayout_2.addWidget(self.right_side)
        self.verticalLayout.addWidget(self.content)
        self.footer = QtWidgets.QFrame(self.centralwidget)
        self.footer.setMinimumSize(QtCore.QSize(800, 70))
        self.footer.setMaximumSize(QtCore.QSize(16777215, 70))
        self.footer.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.footer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.footer.setObjectName("footer")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.footer)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.footer_left_side = QtWidgets.QFrame(self.footer)
        self.footer_left_side.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.footer_left_side.setFrameShadow(QtWidgets.QFrame.Raised)
        self.footer_left_side.setObjectName("footer_left_side")
        self.horizontalLayout.addWidget(self.footer_left_side)
        self.footer_right_side = QtWidgets.QFrame(self.footer)
        self.footer_right_side.setMaximumSize(QtCore.QSize(200, 16777215))
        self.footer_right_side.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.footer_right_side.setFrameShadow(QtWidgets.QFrame.Raised)
        self.footer_right_side.setObjectName("footer_right_side")
        self.gridLayout = QtWidgets.QGridLayout(self.footer_right_side)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_sobre = QtWidgets.QPushButton(self.footer_right_side)
        self.btn_sobre.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_sobre.setObjectName("btn_sobre")
        self.gridLayout.addWidget(self.btn_sobre, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.footer_right_side)
        self.verticalLayout.addWidget(self.footer)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MandoAI"))
        self.centralwidget.setProperty("class", _translate("MainWindow", "background-white"))
        self.lbl_titulo.setText(_translate("MainWindow", "MandoAI"))
        self.lbl_titulo.setProperty("class", _translate("MainWindow", "h1 color-primary"))
        self.lbl_tipo_busqueda.setText(_translate("MainWindow", "Tipo de Búsqueda"))
        self.lbl_tipo_busqueda.setProperty("class", _translate("MainWindow", "h5"))
        self.box_tipo_busqueda.setProperty("class", _translate("MainWindow", "h6"))
        self.box_tipo_busqueda.setItemText(0, _translate("MainWindow", "Busqueda No Informada"))
        self.box_tipo_busqueda.setItemText(1, _translate("MainWindow", "Busqueda Informada"))
        self.lbl_algoritmo.setText(_translate("MainWindow", "Algoritmo"))
        self.lbl_algoritmo.setProperty("class", _translate("MainWindow", "h5"))
        self.box_algoritmo.setProperty("class", _translate("MainWindow", "h6"))
        self.lbl_estado_mundo.setText(_translate("MainWindow", "text_sample"))
        self.lbl_estado_mundo.setProperty("class", _translate("MainWindow", "h6 color-danger"))
        self.btn_cargar_mundo.setText(_translate("MainWindow", "Cargar Mundo"))
        self.btn_cargar_mundo.setProperty("class", _translate("MainWindow", "btn-primary h6"))
        self.btn_iniciar.setText(_translate("MainWindow", "Iniciar"))
        self.btn_iniciar.setProperty("class", _translate("MainWindow", "btn-danger h6"))
        self.lbl_side_image.setProperty("class", _translate("MainWindow", "background-light"))
        self.footer.setProperty("class", _translate("MainWindow", "background-primary"))
        self.btn_sobre.setText(_translate("MainWindow", "Sobre"))
        self.btn_sobre.setProperty("class", _translate("MainWindow", "btn-outline-dark"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
