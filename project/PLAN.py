import sys
import webbrowser
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
from Planer import Ui_Main
from Progects import Ui_progect
from Produckts import Ui_products
from settings import Ui_SettingWindow

class Вefault_functions():
    def __init__(self):
        self.lineEdit = None
        self.textBrowser = None

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()","","All Files (*);;Text Files (*.txt)", options=options)
        if file_name:
            content = self.textBrowser.toPlainText()  # Пример получения текста из TextBrowser
            try:
                with open(file_name, 'w', encoding='utf-8') as file:
                    file.write(content)
                QMessageBox.information(self, "Успех", "Файл успешно сохранен!")
            except Exception as e:
                QMessageBox.critical(self, "Ошибка", str(e))


    # Методы для изменения или сохранение данных
    def buttonClear(self):
        self.textBrowser.clear()
    def buttonAppend(self):
        self.textBrowser.append(self.lineEdit.text()) # line_edit
    def menuSave(self):
        self.openFileNameDialog()

    # Методы перемещения
    def openPlan(self):
        widget.addWidget(Plan())
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def openProducts(self):
        widget.addWidget(Products())
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def openProject(self):
        widget.addWidget(Projects())
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def openSettingWindow(self):
        widget.addWidget(Sett())
        widget.setCurrentIndex(widget.currentIndex() + 1)


class Plan(Ui_Main, QMainWindow, Вefault_functions):
    def __init__(self = None):
        super(Plan, self).__init__()
        self.all_dates = None
        self.setupUi(self)
        self.initUI()


    def initUI(self):
        widget.setWindowTitle('Планер')
        self.all_dates = { }
        self.pushButton.clicked.connect(self.find_date)
        self.pushButton.setAutoDefault(True)
        self.pushButton_2.clicked.connect(self.buttonClear)
        self.action_1.triggered.connect(self.menuSave)
        self.action_2.triggered.connect(self.openProject)
        self.action_3.triggered.connect(self.openProducts)
        self.action_4.triggered.connect(self.openSettingWindow)

    def find_date(self):
        string_date = self.calendarWidget.selectedDate().getDate()
        if int(string_date[1]) <= 9:
            string_date = (string_date[0], '0' + str(string_date[1]), string_date[-1])
        if int(string_date[2]) <= 9:
            string_date = (string_date[0], str(string_date[1]), '0' + str(string_date[-1]))
        line_edit = self.lineEdit.text()
        self.all_dates[f"{string_date[0]}-{string_date[1]}-{string_date[2]}-{self.timeEdit.time().toString()}"] = line_edit
        self.textBrowser.clear()
        for key in sorted(self.all_dates.keys()):
            self.textBrowser.append(f"{key} - {self.all_dates[key]}")

    # Переопределение методов которые не используются
    def buttonAppend(self):
        pass
    def openPlan(self):
        pass

class Projects(Ui_progect, QMainWindow, Вefault_functions):
    def __init__(self = None):
        super(Projects, self).__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        widget.setWindowTitle('Проекты')
        self.action.triggered.connect(self.openPlan)
        self.menu_3.triggered.connect(self.openSettingWindow)
        self.action_3.triggered.connect(self.openProducts)
        self.action_1.triggered.connect(self.menuSave)
        self.pushButton.clicked.connect(self.buttonAppend)
        self.pushButton_2.clicked.connect(self.buttonClear)
    # Переопределение методов которые не используются
    def openProject(self):
        pass

class Products(Ui_products, QMainWindow, Вefault_functions):
    def __init__(self = None):
        super(Products, self).__init__()
        self.setupUi(self)
        self.initUI()


    def initUI(self):
        widget.setWindowTitle('Список продуктов')
        self.action.triggered.connect(self.openPlan)
        self.menu_3.triggered.connect(self.openSettingWindow)
        self.action_3.triggered.connect(self.openProducts)
        self.action_1.triggered.connect(self.menuSave)
        self.pushButton.clicked.connect(self.buttonAppend)
        self.pushButton_2.clicked.connect(self.buttonClear)
    # Переопределение методов которые не используются
    def openProducts(self):
        pass


class Sett(Ui_SettingWindow, QMainWindow, Вefault_functions):
    def __init__(self = None):
        super(Sett, self).__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        widget.setWindowTitle('Настройки')
        self.pushButton_2.clicked.connect(self.link)
        self.pushButton_3.clicked.connect(self.openPlan)
        self.pushButton4.clicked.connect(self.Podelitcz)

    def link(self):
        webbrowser.open('https://vk.com/sergei239')

    def Podelitcz(self):
        QMessageBox.information(widget, 'Да-да', 'не дам)', QMessageBox.Ok)

app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
plan = Plan()
widget.setWindowIcon(QIcon('../planner.png'))
widget.addWidget(plan)
widget.show()
sys.exit(app.exec_())
