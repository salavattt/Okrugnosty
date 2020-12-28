# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtGui import QPixmap
from copy import deepcopy
import sqlite3
import sys
import random
from PyQt5.Qt import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 60, 721, 371))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(180, 510, 351, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(540, 510, 161, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 440, 171, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(410, 440, 171, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(590, 440, 171, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(220, 440, 181, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(190, 10, 401, 41))
        self.label_7.setObjectName("label_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "отправить сообщение"))
        self.pushButton.setStyleSheet("background-color: #8b008b")
        self.pushButton_2.setText(_translate("MainWindow", "Привет!"))
        self.pushButton_2.setStyleSheet("background-color: #8b008b")
        self.pushButton_3.setText(_translate("MainWindow", "Как дела?"))
        self.pushButton_3.setStyleSheet("background-color: #8b008b")
        self.pushButton_4.setText(_translate("MainWindow", "Скажи погоду на завтра"))
        self.pushButton_4.setStyleSheet("background-color: #8b008b")
        self.pushButton_5.setText(_translate("MainWindow", "Как тебя завут?"))
        self.pushButton_5.setStyleSheet("background-color: #8b008b")
        self.label_7.setText(_translate("MainWindow",
                                        "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">ЯНДЕКС АЛИСА 0.9</span></p></body></html>"))
        self.pushButton_2.clicked.connect(self.chat_hello)
        self.pushButton_5.clicked.connect(self.what_is_your_name)
        self.pushButton_3.clicked.connect(self.chat_how_are_you)
        self.pushButton_4.clicked.connect(self.weather)
        self.what_chat = 0

    def chat_hello(self):
        self.chat('hello')

    def chat_how_are_you(self):
        self.chat('how are you')

    def what_is_your_name(self):
        self.chat('what is your name')

    def weather(self):
        self.chat('weather')

    def chat(self, chat):
        if self.what_chat >= 1:

            self.label.setText(self.label_3.text())
            self.label.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Bold))
            if self.what_chat == 2:
                self.label_2.setStyleSheet("background-color: #8b008b")
            self.label.setAlignment(Qt.AlignRight)
            self.label_2.setText(self.label_4.text())
            self.label_2.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Bold))
            if self.what_chat == 1:
                self.label_4.setStyleSheet("background-color: #8b008b")
            self.label_3.setText(self.label_5.text())
            self.label_3.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Bold))
            self.label_3.setAlignment(Qt.AlignRight)
            self.label_4.setText(self.label_6.text())
            self.label_4.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Bold))

        if chat == 'hello':
            _translate = QtCore.QCoreApplication.translate
            MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
            self.label_5.setText('Привет!')
            self.label_5.setAlignment(Qt.AlignRight)
            num = random.randint(1, 3)
            if num == 1:
                self.label_6.setText('И тебе привет!')
                self.label_6.setStyleSheet("background-color: #8b008b")
            if num == 2:
                self.label_6.setText('привет! Давно не виделись')
                self.label_6.setStyleSheet("background-color: #8b008b")
            if num == 3:
                self.label_6.setText('Ну привет!')
                self.label_6.setStyleSheet("background-color: #8b008b")
            self.what_chat += 1

        if chat == 'how are you':
            self.label_5.setText('Как дела?')
            self.label_5.setAlignment(Qt.AlignRight)
            num = random.randint(1, 3)
            if num == 1:
                self.label_6.setText('У меня все хорошо)')
                self.label_6.setStyleSheet("background-color: #8b008b")
            if num == 2:
                self.label_6.setText('я чувстваю себя хорошо')
                self.label_6.setStyleSheet("background-color: #8b008b")
            if num == 3:
                self.label_6.setText('Отлично, приятно, что вы интересуетесь')
                self.label_6.setStyleSheet("background-color: #8b008b")
            self.what_chat += 1

        if chat == 'what is your name':
            self.label_5.setText('Как тебя завут?')
            self.label_5.setAlignment(Qt.AlignRight)
            num = random.randint(1, 2)
            if num == 1:
                self.label_6.setText('Меня завут Алиса 0.9')
                self.label_6.setStyleSheet("background-color: #8b008b")
            if num == 2:
                self.label_6.setText('Я бот чат Алиса')
                self.label_6.setStyleSheet("background-color: #8b008b")
            self.what_chat += 1

        if chat == 'weather':
            self.label_5.setText('Скажи погоду на завтра')
            self.label_5.setAlignment(Qt.AlignRight)
            num = random.randint(1, 2)
            if num == 1:
                self.label_6.setText('У меня пока нет такой функции')
                self.label_6.setStyleSheet("background-color: #8b008b")
            if num == 2:
                self.label_6.setText('Я не могу точно сказать')
                self.label_6.setStyleSheet("background-color: #8b008b")
            self.what_chat += 1
        self.label_5.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Bold))
        self.label_6.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Bold))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
