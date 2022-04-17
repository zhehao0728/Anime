# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1200, 800)
        font = QtGui.QFont()
        font.setPointSize(9)
        Form.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/picture/image/Anime.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setToolTipDuration(-1)
        self.stackedWidget = QtWidgets.QStackedWidget(Form)
        self.stackedWidget.setEnabled(True)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 40, 1200, 761))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.listWidget = QtWidgets.QListWidget(self.page)
        self.listWidget.setGeometry(QtCore.QRect(10, 10, 71, 741))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.listWidget.setFont(font)
        self.listWidget.setProperty("isWrapping", False)
        self.listWidget.setWordWrap(True)
        self.listWidget.setObjectName("listWidget")
        self.listWidget_2 = QtWidgets.QListWidget(self.page)
        self.listWidget_2.setGeometry(QtCore.QRect(80, 10, 281, 741))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.listWidget_2.setFont(font)
        self.listWidget_2.setProperty("isWrapping", False)
        self.listWidget_2.setWordWrap(True)
        self.listWidget_2.setObjectName("listWidget_2")
        self.line_2 = QtWidgets.QFrame(self.page)
        self.line_2.setGeometry(QtCore.QRect(360, -10, 20, 771))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label = QtWidgets.QLabel(self.page)
        self.label.setGeometry(QtCore.QRect(380, 10, 200, 275))
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.page)
        self.label_2.setGeometry(QtCore.QRect(600, 10, 591, 41))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.page)
        self.label_3.setGeometry(QtCore.QRect(600, 80, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.page)
        self.label_4.setGeometry(QtCore.QRect(600, 50, 591, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.page)
        self.label_5.setGeometry(QtCore.QRect(860, 80, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_5.setFont(font)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.page)
        self.label_6.setGeometry(QtCore.QRect(600, 120, 591, 161))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setText("")
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName("label_6")
        self.line_3 = QtWidgets.QFrame(self.page)
        self.line_3.setGeometry(QtCore.QRect(370, 290, 831, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.listWidget_3 = QtWidgets.QListWidget(self.page)
        self.listWidget_3.setGeometry(QtCore.QRect(715, 310, 471, 441))
        self.listWidget_3.setObjectName("listWidget_3")
        self.groupBox = QtWidgets.QGroupBox(self.page)
        self.groupBox.setGeometry(QtCore.QRect(380, 430, 321, 321))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(10, 20, 41, 21))
        self.label_7.setObjectName("label_7")
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_2.setGeometry(QtCore.QRect(60, 20, 91, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(10, 270, 301, 41))
        self.label_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_8.setWordWrap(True)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(10, 240, 71, 20))
        self.label_9.setObjectName("label_9")
        self.pushButton_14 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_14.setGeometry(QtCore.QRect(230, 240, 75, 23))
        self.pushButton_14.setObjectName("pushButton_14")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 50, 141, 171))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_16 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_16.setObjectName("pushButton_16")
        self.verticalLayout.addWidget(self.pushButton_16)
        self.pushButton_17 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_17.setObjectName("pushButton_17")
        self.verticalLayout.addWidget(self.pushButton_17)
        self.pushButton_15 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_15.setObjectName("pushButton_15")
        self.verticalLayout.addWidget(self.pushButton_15)
        self.checkBox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_3.setGeometry(QtCore.QRect(160, 10, 151, 211))
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_3)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 40, 131, 171))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox_3.setObjectName("checkBox_3")
        self.verticalLayout_2.addWidget(self.checkBox_3)
        self.checkBox_6 = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox_6.setObjectName("checkBox_6")
        self.verticalLayout_2.addWidget(self.checkBox_6)
        self.checkBox_5 = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox_5.setObjectName("checkBox_5")
        self.verticalLayout_2.addWidget(self.checkBox_5)
        self.checkBox_4 = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox_4.setObjectName("checkBox_4")
        self.verticalLayout_2.addWidget(self.checkBox_4)
        self.checkBox_2 = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout_2.addWidget(self.checkBox_2)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 20, 61, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_3.setGeometry(QtCore.QRect(80, 20, 61, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.groupBox_2 = QtWidgets.QGroupBox(self.page)
        self.groupBox_2.setGeometry(QtCore.QRect(380, 310, 321, 101))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayoutWidget = QtWidgets.QWidget(self.groupBox_2)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 20, 321, 71))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_12 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout.addWidget(self.pushButton_12, 0, 0, 1, 1)
        self.pushButton_13 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_13.setObjectName("pushButton_13")
        self.gridLayout.addWidget(self.pushButton_13, 0, 1, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout.addWidget(self.pushButton_10, 1, 0, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.pushButton_9, 1, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.page)
        self.label_10.setGeometry(QtCore.QRect(380, 200, 811, 91))
        font = QtGui.QFont()
        font.setPointSize(60)
        self.label_10.setFont(font)
        self.label_10.setText("")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.tableWidget = QtWidgets.QTableWidget(self.page_2)
        self.tableWidget.setGeometry(QtCore.QRect(10, 80, 1181, 671))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.groupBox_4 = QtWidgets.QGroupBox(self.page_2)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 10, 281, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_4)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 263, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.checkBox_13 = QtWidgets.QCheckBox(self.horizontalLayoutWidget_2)
        self.checkBox_13.setObjectName("checkBox_13")
        self.horizontalLayout_2.addWidget(self.checkBox_13)
        self.checkBox_14 = QtWidgets.QCheckBox(self.horizontalLayoutWidget_2)
        self.checkBox_14.setObjectName("checkBox_14")
        self.horizontalLayout_2.addWidget(self.checkBox_14)
        self.checkBox_15 = QtWidgets.QCheckBox(self.horizontalLayoutWidget_2)
        self.checkBox_15.setObjectName("checkBox_15")
        self.horizontalLayout_2.addWidget(self.checkBox_15)
        self.groupBox_5 = QtWidgets.QGroupBox(self.page_2)
        self.groupBox_5.setGeometry(QtCore.QRect(300, 10, 891, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setObjectName("groupBox_5")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.groupBox_5)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 20, 871, 31))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_22 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_22.setObjectName("pushButton_22")
        self.horizontalLayout_3.addWidget(self.pushButton_22)
        self.pushButton_21 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_21.setObjectName("pushButton_21")
        self.horizontalLayout_3.addWidget(self.pushButton_21)
        self.radioButton_3 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_3)
        self.radioButton_3.setObjectName("radioButton_3")
        self.horizontalLayout_3.addWidget(self.radioButton_3)
        self.radioButton_4 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_3)
        self.radioButton_4.setObjectName("radioButton_4")
        self.horizontalLayout_3.addWidget(self.radioButton_4)
        self.pushButton_20 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_20.setObjectName("pushButton_20")
        self.horizontalLayout_3.addWidget(self.pushButton_20)
        self.pushButton_19 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_19.setObjectName("pushButton_19")
        self.horizontalLayout_3.addWidget(self.pushButton_19)
        self.pushButton_18 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_18.setObjectName("pushButton_18")
        self.horizontalLayout_3.addWidget(self.pushButton_18)
        self.stackedWidget.addWidget(self.page_2)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 271, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(290, 10, 75, 23))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/picture/image/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setObjectName("pushButton")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(370, 10, 121, 22))
        self.comboBox.setObjectName("comboBox")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(0, 30, 1201, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(1120, 10, 75, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_4.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/picture/image/setting.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon2)
        self.pushButton_4.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(1040, 10, 75, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_5.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/picture/image/download.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon3)
        self.pushButton_5.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_5.setObjectName("pushButton_5")

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Anime"))
        self.groupBox.setTitle(_translate("Form", "下载选项"))
        self.label_7.setText(_translate("Form", "显示："))
        self.label_8.setText(_translate("Form", "未选择"))
        self.label_9.setText(_translate("Form", "保存地址："))
        self.pushButton_14.setText(_translate("Form", "修改地址"))
        self.pushButton_16.setText(_translate("Form", "下载所有"))
        self.pushButton_17.setText(_translate("Form", "下载当前列表"))
        self.pushButton_15.setText(_translate("Form", "下载所有选中"))
        self.checkBox.setText(_translate("Form", "启用筛选"))
        self.groupBox_3.setTitle(_translate("Form", "筛选"))
        self.checkBox_3.setText(_translate("Form", "正常"))
        self.checkBox_6.setText(_translate("Form", ".5 集"))
        self.checkBox_5.setText(_translate("Form", "OVA"))
        self.checkBox_4.setText(_translate("Form", "SP"))
        self.checkBox_2.setText(_translate("Form", "PV"))
        self.pushButton_2.setText(_translate("Form", "全选"))
        self.pushButton_3.setText(_translate("Form", "全不选"))
        self.groupBox_2.setTitle(_translate("Form", "编辑信息"))
        self.pushButton_12.setText(_translate("Form", "名称修改"))
        self.pushButton_13.setText(_translate("Form", "查看简介"))
        self.pushButton_10.setText(_translate("Form", "保存图片"))
        self.pushButton_9.setText(_translate("Form", "保存信息至本地"))
        self.groupBox_4.setTitle(_translate("Form", "显示"))
        self.checkBox_13.setText(_translate("Form", "下载完成"))
        self.checkBox_14.setText(_translate("Form", "正在下载"))
        self.checkBox_15.setText(_translate("Form", "下载异常"))
        self.groupBox_5.setTitle(_translate("Form", "操作"))
        self.pushButton_22.setText(_translate("Form", "全选"))
        self.pushButton_21.setText(_translate("Form", "全不选"))
        self.radioButton_3.setText(_translate("Form", "所有勾选"))
        self.radioButton_4.setText(_translate("Form", "所有未勾选"))
        self.pushButton_20.setText(_translate("Form", "全部开始"))
        self.pushButton_19.setText(_translate("Form", "全部暂停"))
        self.pushButton_18.setText(_translate("Form", "全部删除"))
        self.pushButton.setText(_translate("Form", "搜索"))
        self.pushButton_4.setText(_translate("Form", "设置"))
        self.pushButton_5.setText(_translate("Form", "下载"))
import value_rc