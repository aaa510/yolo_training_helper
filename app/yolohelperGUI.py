# -*- coding: utf-8 -*-
import sys
from tkinter import font
from PyQt5.QtCore import Qt  # 确保导入 Qt 模块
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QVBoxLayout, QMainWindow, QTextEdit, QLabel, QToolButton, \
    QComboBox, QListWidget, QLineEdit, QPushButton
from PyQt5.QtGui import *
from pyqt5_plugins.examplebuttonplugin import QtGui



class UI_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 500)

        font = QFont("黑体", 10)  # 设置字体为黑体，大小为10
        MainWindow.setFont(font)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        MainWindow.setMenuBar(self.menubar)

        # 添加“文件”菜单
        self.menu = QtWidgets.QMenu("文件", self.menubar)
        self.menubar.addMenu(self.menu)

        # 添加“类别”按钮
        self.helpAction = QtWidgets.QAction("帮助", MainWindow)
        self.menu.addAction(self.helpAction)

        # 设置中心窗口和主布局
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        MainWindow.setCentralWidget(self.centralwidget)
        self.mainLayout = QVBoxLayout(self.centralwidget)  # 主垂直布局



        # Images目录布局
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.ImagesLabelsLayout = QHBoxLayout(self.groupBox)  # 水平布局用于标签和文本框

        # 创建并添加标签
        self.ImagesLabel = QLabel("Images目录:", self.groupBox)
        self.ImagesLabelsLayout.addWidget(self.ImagesLabel)

        # 创建并添加单行文本框
        self.lineEdit1 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit1.setFixedHeight(30)  # 调整单行文本框的高度
        self.ImagesLabelsLayout.addWidget(self.lineEdit1)

        # 创建并添加工具按钮
        self.ImagesButton = self.create_tool_button(self.groupBox, "选择")
        self.ImagesLabelsLayout.addWidget(self.ImagesButton)

        # 添加 groupBox 到主布局
        self.mainLayout.addWidget(self.groupBox)

        #类别名的布局
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.clsLabelsLayout = QHBoxLayout(self.groupBox)  # 水平布局用于标签和文本框

        # 创建并添加标签
        self.clsLabel = QLabel("类别", self.groupBox)
        self.clsLabelsLayout.addWidget(self.clsLabel)


        # 创建并添加输入框
        self.lineEdit2 = QLineEdit(self.groupBox)
        self.lineEdit2.setFixedHeight(30)  # 调整单行文本框的高度
        self.clsLabelsLayout.addWidget(self.lineEdit2)

        # 创建并添加加号按钮
        self.addButton = QPushButton("+", self.groupBox)
        self.addButton.setFixedHeight(30)  # 调整按钮的高度
        self.clsLabelsLayout.addWidget(self.addButton)

        # 创建并添加减号按钮
        self.removeButton = QPushButton("-", self.groupBox)
        self.removeButton.setFixedHeight(30)  # 调整按钮的高度
        self.clsLabelsLayout.addWidget(self.removeButton)

        # 添加 groupBox 到主布局
        self.mainLayout.addWidget(self.groupBox)

        # 列表的布局
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.ListLayout = QVBoxLayout(self.groupBox)

        # 创建并添加列表框，用于显示类别名
        self.listWidget = QListWidget(self.groupBox)
        self.listWidget.setFixedHeight(50)
        self.ListLayout.addWidget(self.listWidget)

        #保存按钮
        self.saveButton = QPushButton("保存", self.groupBox)
        self.saveButton.setFixedHeight(30)  # 调整按钮的高度
        self.ListLayout.addWidget(self.saveButton)

        self.mainLayout.addWidget(self.groupBox)





        #训练超参数的布局
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.SizeLayout = QHBoxLayout(self.groupBox)  # 水平布局用于标签和文本框

        # 训练超参数标题
        self.titleLabel = QLabel("训练超参数设置", self.groupBox)  # 标题标签
        self.titleLabel.setStyleSheet(
            "border: 1px solid #AAB7B8; background-color: #D5DBDB; font-weight: bold; font-size: 16px; color: #34495E; padding: 5px;")

        self.SizeLayout.addWidget(self.titleLabel, alignment=Qt.AlignLeft | Qt.AlignTop)  # 左上角对齐
        self.SizeLayout.addSpacing(10)  # 添加间距
        # 创建并添加标签
        self.SizeLabel = QLabel("模型输入宽高", self.groupBox)
        self.SizeLayout.addWidget(self.SizeLabel)




        # 创建并添加下拉框
        self.comboBox1 = QComboBox(self.groupBox)
        self.comboBox1.setFixedHeight(30)  # 调整下拉框的高度
        self.comboBox1.addItems(["320", "416", "512", "640","768","896", "1024"])  # 添加常用的输入尺寸选项
        self.SizeLayout.addWidget(self.comboBox1)
        # 添加 groupBox 到主布局
        self.mainLayout.addWidget(self.groupBox)

        #batch
        # 创建并添加标签
        self.BatchLabel = QLabel("批大小(Batch)", self.groupBox)
        self.SizeLayout.addWidget(self.BatchLabel)

        # 创建并添加下拉框
        self.comboBox2 = QComboBox(self.groupBox)
        self.comboBox2.setFixedHeight(30)  # 调整下拉框的高度
        self.comboBox2.addItems(["16", "32", "64", "128", "216", "512"])  # 添加常用的输入尺寸选项
        self.SizeLayout.addWidget(self.comboBox2)


        #Epochs
        self.EpochsLabel = QLabel("EPOCHS", self.groupBox)
        self.SizeLayout.addWidget(self.EpochsLabel)
        # 创建并添加下拉框
        self.lineEdit3 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit3.setFixedHeight(30)  # 调整单行文本框的高度
        self.lineEdit3.setFixedWidth(80)
        self.lineEdit3.setText("100")
        self.SizeLayout.addWidget(self.lineEdit3)


        # 优化器
        # self.OptimizerLabel = QLabel("优化器", self.groupBox)
        # self.SizeLayout.addWidget(self.OptimizerLabel)
        #
        # self.comboBox4 = QComboBox(self.groupBox)
        # self.comboBox4.setFixedHeight(30)  # 调整下拉框的高度
        # self.comboBox4.addItems(['SGD', 'Adam', 'AdamW'])  # 添加常用的输入尺寸选项
        #
        # # 设置默认值为“Adam”
        # self.comboBox4.setCurrentText("Adam")
        #
        # self.SizeLayout.addWidget(self.comboBox4)


        #矩形
        self.RectLabel = QLabel("矩形训练", self.groupBox)
        self.SizeLayout.addWidget(self.RectLabel)

        self.comboBox5 = QComboBox(self.groupBox)
        self.comboBox5.setFixedHeight(30)  # 调整下拉框的高度
        self.comboBox5.addItems(['启用', '禁止'])  # 添加常用的输入尺寸选项


        self.comboBox5.setCurrentText("禁止")

        self.SizeLayout.addWidget(self.comboBox5)

        #早停耐心值
        self.PatienceLabel = QLabel("早停耐心值", self.groupBox)
        self.SizeLayout.addWidget(self.PatienceLabel)
        # 创建并添加下拉框
        self.lineEdit6 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit6.setText("100")
        self.lineEdit6.setFixedHeight(30)  # 调整单行文本框的高度
        self.lineEdit6.setFixedWidth(80)
        self.lineEdit6.setReadOnly(True)


        self.SizeLayout.addWidget(self.lineEdit6)




        #model
        self.ModelLabel = QLabel("模型版本", self.groupBox)
        self.SizeLayout.addWidget(self.ModelLabel)
        # 创建并添加下拉框
        self.comboBox = QComboBox(self.groupBox)
        self.comboBox.setFixedHeight(30)  # 调整下拉框的高度
        self.comboBox.addItems(["yolov5s", "yolov5n", "yolov5l", "yolov5m","yolov5x"])  # 添加常用的输入尺寸选项
        self.SizeLayout.addWidget(self.comboBox)

        # 添加 groupBox 到主布局
        self.mainLayout.addWidget(self.groupBox)

        # 优化超参数
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.LrLayout = QHBoxLayout(self.groupBox)  # 水平布局用于标签和文本框

        # 训练超参数标题
        self.titleLabel = QLabel("优化超参数设置", self.groupBox)  # 标题标签
        self.titleLabel.setStyleSheet(
            "border: 1px solid #AAB7B8; background-color: #D5DBDB; font-weight: bold; font-size: 16px; color: #34495E; padding: 5px;")

        self.LrLayout.addWidget(self.titleLabel, alignment=Qt.AlignLeft | Qt.AlignTop)  # 左上角对齐
        self.LrLayout.addSpacing(10)  # 添加间距

        self.hyp_values = {
            "hyp.Objects365": {
                "lr0": "0.00258", "lrf": "0.17", "momentum": "0.779", "weight_decay": "0.00058"
            },
            "hyp.scratch-high": {
                "lr0": "0.01", "lrf": "0.1", "momentum": "0.937", "weight_decay": "0.0005"
            },
            "hyp.scratch-low": {
                "lr0": "0.01", "lrf": "0.01", "momentum": "0.937", "weight_decay": "0.0005"
            },
            "hyp.scratch-med": {
                "lr0": "0.01", "lrf": "0.1", "momentum": "0.937", "weight_decay": "0.0005"
            },
            "hyp.VOC": {
                "lr0": "0.00334", "lrf": "0.15135", "momentum": "0.74832", "weight_decay": "0.00025"
            }
        }

        # 指定hyp文件
        self.hypLabel = QLabel("超参数配置文件", self.groupBox)
        self.LrLayout.addWidget(self.hypLabel)

        self.comboBox3 = QComboBox(self.groupBox)
        self.comboBox3.setFixedHeight(30)
        self.comboBox3.addItems(list(self.hyp_values.keys()))
        self.comboBox3.setCurrentText("hyp.scratch-low")
        self.LrLayout.addWidget(self.comboBox3)

        # 函数生成标签和输入框
        def create_param_input(label_text, param_key):
            label = QLabel(label_text, self.groupBox)
            line_edit = QLineEdit(self.groupBox)
            line_edit.setFixedHeight(30)
            line_edit.setFixedWidth(100)
            line_edit.setReadOnly(True)  # 设置为只读
            line_edit.setText(self.hyp_values["hyp.scratch-low"][param_key])
            self.LrLayout.addWidget(label)
            self.LrLayout.addWidget(line_edit)
            return line_edit

        # 创建各参数输入框
        self.lineEdit4 = create_param_input("初始学习率", "lr0")
        self.lineEdit5 = create_param_input("最终学习率", "lrf")
        self.momentumEdit = create_param_input("SGD动量", "momentum")
        self.weightDecayEdit = create_param_input("权重衰减", "weight_decay")

        self.mainLayout.addWidget(self.groupBox)

        # 定义更新参数值的函数
        def update_hyp_values():
            current_hyp = self.comboBox3.currentText()
            values = self.hyp_values.get(current_hyp, self.hyp_values["hyp.scratch-low"])
            self.lineEdit4.setText(values["lr0"])
            self.lineEdit5.setText(values["lrf"])
            self.momentumEdit.setText(values["momentum"])
            self.weightDecayEdit.setText(values["weight_decay"])

        # 连接信号到槽函数，当选择发生变化时更新参数值
        self.comboBox3.currentTextChanged.connect(update_hyp_values)


        #其它超参数
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.BesideLayout = QHBoxLayout(self.groupBox)  # 水平布局用于标签和文本框

        # 训练超参数标题
        self.titleLabel = QLabel("其它超参数设置", self.groupBox)  # 标题标签
        self.titleLabel.setStyleSheet(
            "border: 1px solid #AAB7B8; background-color: #D5DBDB; font-weight: bold; font-size: 16px; color: #34495E; padding: 5px;")

        self.BesideLayout.addWidget(self.titleLabel, alignment=Qt.AlignLeft | Qt.AlignTop)  # 左上角对齐
        self.BesideLayout.addSpacing(10)  # 添加间距
        # 创建并添加标签

        # 优化器
        self.OptimizerLabel = QLabel("优化器", self.groupBox)
        self.BesideLayout.addWidget(self.OptimizerLabel)

        self.comboBox4 = QComboBox(self.groupBox)
        self.comboBox4.setFixedHeight(30)  # 调整下拉框的高度
        self.comboBox4.addItems(['SGD', 'Adam', 'AdamW'])  # 添加常用的输入尺寸选项


        self.comboBox4.setCurrentText("Adam")

        self.BesideLayout.addWidget(self.comboBox4)

        #最大线程数
        self.WorkersLabel = QLabel("最大线程数", self.groupBox)
        self.BesideLayout.addWidget(self.WorkersLabel)

        self.lineEdit7 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit7.setFixedHeight(30)  # 调整单行文本框的高度
        self.lineEdit7.setFixedWidth(80)
        self.lineEdit7.setText("8")
        self.BesideLayout.addWidget(self.lineEdit7)

        # project
        self.ProjectLabel = QLabel("保存到", self.groupBox)
        self.BesideLayout.addWidget(self.ProjectLabel)

        self.lineEdit8 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit8.setFixedHeight(30)  # 调整单行文本框的高度
        self.lineEdit8.setFixedWidth(300)
        self.lineEdit8.setText("runs/train")
        self.BesideLayout.addWidget(self.lineEdit8)
        #name
        self.NameLabel = QLabel("项目名称", self.groupBox)
        self.BesideLayout.addWidget(self.NameLabel)

        self.lineEdit9 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit9.setFixedHeight(30)  # 调整单行文本框的高度
        self.lineEdit9.setFixedWidth(100)
        self.lineEdit9.setText("exp")
        self.BesideLayout.addWidget(self.lineEdit9)

        #图像缓存方式
        self.CacheLabel = QLabel("缓存方式", self.groupBox)
        self.BesideLayout.addWidget(self.CacheLabel)

        self.lineEdit10 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit10.setFixedHeight(30)  # 调整单行文本框的高度
        self.lineEdit10.setFixedWidth(100)
        self.lineEdit10.setText("RAM")
        self.lineEdit10.setReadOnly(True)

        self.BesideLayout.addWidget(self.lineEdit10)


        # 添加 groupBox 到主布局
        self.mainLayout.addWidget(self.groupBox)



        #输出框
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.OutputLayout = QVBoxLayout(self.groupBox)


        self.textEdit = QTextEdit(self.groupBox)
        self.textEdit.setFixedHeight(60)
        self.OutputLayout.addWidget(self.textEdit)  # 将文本编辑框添加到布局中


        self.TransButton = QPushButton("开始训练", self.groupBox)
        self.TransButton.setFixedHeight(30)  # 调整按钮的高度
        self.OutputLayout.addWidget(self.TransButton)

        self.mainLayout.addWidget(self.groupBox)

        #训练进度
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.ProcessLayout = QVBoxLayout(self.groupBox)  # 水平布局用于标签和文本框

        # 创建并添加标签
        self.ProcessLabel = QLabel("训练进度", self.groupBox)
        self.ProcessLayout.addWidget(self.ProcessLabel)

        self.textEdit1 = QTextEdit(self.groupBox)
        self.textEdit1.setFixedHeight(250)  # 固定高度
        self.ProcessLayout.addWidget(self.textEdit1)  # 将文本编辑框添加到布局中

        # 增加拉伸项以占据剩余空间
        self.ProcessLayout.addStretch(1)

        self.mainLayout.addWidget(self.groupBox)


    def create_tool_button(self, parent, text):
        """创建工具按钮"""

        button = QToolButton(parent)
        button.setText(text)
        return button

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "YOLO训练助手"))

if __name__ == "__main__":
    app = QApplication(sys.argv)  # 创建QApplication实例
    MainWindow = QMainWindow()  # 创建主窗口
    ui = UI_MainWindow()  # 创建UI对象
    ui.setupUi(MainWindow)  # 设置UI
    MainWindow.show()  # 显示主窗口
    sys.exit(app.exec_())  # 运行主循环
