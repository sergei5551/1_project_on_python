
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SettingWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName('MainWindow')
        MainWindow.resize(610, 361)
        MainWindow.setStyleSheet('QPushButton {\nbackground-color: rgb(170, 255, 127);\nfont: 16pt "MS Shell Dlg 2";\n}\nQPushButton:hover {\nbackground-color: rgb(106, 158, 78);\n}\nQPushButton:pressed {\nbackground-color: rgb(112, 112, 112);\n}')
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName('centralwidget')
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName('gridLayout')
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName('verticalLayout')
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName('pushButton_3')
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName('pushButton_2')
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton4.setObjectName('pushButton4')
        self.verticalLayout.addWidget(self.pushButton4)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.viewport().setProperty('cursor', QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.textBrowser.setMouseTracking(False)
        self.textBrowser.setTabletTracking(False)
        self.textBrowser.setStyleSheet('background-color: rgb(170, 255, 127);')
        self.textBrowser.setOverwriteMode(False)
        self.textBrowser.setObjectName('textBrowser')
        self.verticalLayout.addWidget(self.textBrowser)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.pushButton_3.setText(_translate('MainWindow', 'Главная'))
        self.pushButton_2.setText(_translate('MainWindow', 'Обратная связь'))
        self.pushButton4.setText(_translate('MainWindow', 'Поделиться'))
        self.textBrowser.setHtml(_translate('MainWindow', '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n<html><head><meta name="qrichtext" content="1" /><style type="text/css">\np, li { white-space: pre-wrap; }\n</style></head><body style=" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;">\n<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:16pt;">Версия: Beta_1</span></p>\n<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:16pt;">Обратная связь:Вк</span></p>\n<p align="center" style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;"><br /></p>\n<p align="center" style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;"><br /></p>\n<p align="center" style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;"><br /></p>\n<p align="center" style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;"><br /></p>\n<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:16pt;">Создатель:Сережа</span></p></body></html>'))


