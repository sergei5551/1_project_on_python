
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_products(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName('MainWindow')
        MainWindow.resize(825, 576)
        MainWindow.setStyleSheet('QPushButton {\nfont: 16pt "MS Shell Dlg 2";\nbackground-color: rgb(249, 255, 175);\n}\nQPushButton:hover {\nbackground-color: yellow;\n}\nQPushButton:pressed {\nbackground-color: rgb(255, 255, 127);\n}\n')
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName('centralwidget')
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName('gridLayout')
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName('pushButton')
        self.gridLayout.addWidget(self.pushButton, 3, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName('pushButton_2')
        self.gridLayout.addWidget(self.pushButton_2, 3, 0, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setMinimumSize(QtCore.QSize(417, 0))
        self.textBrowser.setStyleSheet('background-color: rgb(255, 255, 0);\ncolor:rgb(0, 85, 255);\nfont: 16pt "MS Shell Dlg 2";')
        self.textBrowser.setObjectName('textBrowser')
        self.gridLayout.addWidget(self.textBrowser, 1, 0, 1, 2)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setStyleSheet('color:rgb(0, 85, 255);\nfont: 16pt "MS Shell Dlg 2";\nbackground-color: rgb(255, 255, 127);')
        self.lineEdit.setObjectName('lineEdit')
        self.gridLayout.addWidget(self.lineEdit, 2, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 825, 21))
        self.menubar.setObjectName('menubar')
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName('menu')
        self.action_1 = QtWidgets.QAction(MainWindow)
        self.action_1.setObjectName('action_1')
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName('menu_2')
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName('menu_3')
        MainWindow.setMenuBar(self.menubar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName('action')
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName('action_3')
        self.action_4 = QtWidgets.QAction(MainWindow)
        self.action_4.setObjectName('action_4')
        self.menu.addAction(self.action_1)
        self.menu_2.addAction(self.action)
        self.menu_2.addAction(self.action_3)
        self.menu_3.addAction(self.action_4)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.pushButton.setText(_translate('MainWindow', '+'))
        self.lineEdit.setPlaceholderText(_translate('Main', 'Продукт'))
        self.pushButton_2.setText(_translate('MainWindow', '-'))
        self.menu.setTitle(_translate('Main', 'Текст'))
        self.action_1.setText(_translate('Main', 'Сохранить'))
        self.menu_2.setTitle(_translate('MainWindow', 'Режимы'))
        self.menu_3.setTitle(_translate('MainWindow', 'Настройки'))
        self.action_4.setText(_translate('Main', 'Открыть'))
        self.action.setText(_translate('MainWindow', 'Ежедневник'))
        self.action_3.setText(_translate('MainWindow', 'Проекты'))


