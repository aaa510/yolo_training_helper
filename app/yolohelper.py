import re
import sys
import time
import subprocess

import yaml
from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import *
import os
from PyInstaller.utils.hooks import collect_submodules
from PyQt5 import QtCore

from setParDialog import ChatDialog

hiddenimports = collect_submodules('PyQt5.Qt')
from yolohelperGUI import UI_MainWindow

class MainWindow(QtWidgets.QMainWindow, UI_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)


        self.yaml_file_name = ""
        self.ImagesButton.clicked.connect(self.select_directory)

        # 连接按钮的点击信号到槽函数
        self.addButton.clicked.connect(self.add_category)
        self.removeButton.clicked.connect(self.remove_category)
        self.saveButton.clicked.connect(self.save_to_yaml)
        self.TransButton.clicked.connect(self.convert_command)
        self.helpAction.triggered.connect(self.open_chat_dialog)



    def select_directory(self):
        # 打开文件夹选择对话框
        folder_path = QFileDialog.getExistingDirectory(self, "选择文件夹")

        if folder_path:
            # 更新路径文本框
            self.lineEdit1.setText(folder_path)
            self.folder_path = folder_path  # 保存路径

    # 槽函数：将输入框内容添加到列表框
    def add_category(self):
        category_name = self.lineEdit2.text().strip()
        if category_name:  # 确保输入框不是空的
            self.listWidget.addItem(category_name)
            self.lineEdit2.clear()  # 添加后清空输入框

    # 槽函数：删除当前选中的类别
    def remove_category(self):
        selected_items = self.listWidget.selectedItems()
        if selected_items:  # 确保有选中的项
            for item in selected_items:
                self.listWidget.takeItem(self.listWidget.row(item))

    def save_to_yaml(self):
        try:
            # 获取程序所在的根目录
            base_dir = os.path.dirname(os.path.abspath(__file__))

            # 指定保存的文件夹路径
            save_dir = os.path.join(base_dir, 'yolov5', 'data')

            # 如果文件夹不存在，创建它
            os.makedirs(save_dir, exist_ok=True)

            # 添加时间戳生成唯一文件名
            timestamp = time.strftime('%Y%m%d_%H%M%S')
            self.yaml_file_name = f'data_{timestamp}.yaml'  # 保存文件名
            yaml_file_path = os.path.join(save_dir, self.yaml_file_name)

            # 创建 YAML 内容字典
            yaml_content = {
                'path': '',
                'train': '',
                'val': '',
                'test': '',
                'names': {}
            }

            # 设置路径信息
            yaml_content['train'] = os.path.join(self.lineEdit1.text(), 'images', 'train')  # 训练集路径
            yaml_content['val'] = os.path.join(self.lineEdit1.text(), 'images', 'val')  # 验证集路径

            # 添加类别信息
            for i in range(self.listWidget.count()):
                class_name = self.listWidget.item(i).text()  # 获取列表中的类别名
                yaml_content['names'][i] = class_name  # 添加到 YAML 内容

            # 保存 YAML 文件
            with open(yaml_file_path, 'w') as yaml_file:
                yaml.dump(yaml_content, yaml_file)

            # 提示保存成功
            QMessageBox.information(self, "成功", f"信息已保存至: {yaml_file_path}")

        except Exception as e:
            QMessageBox.critical(self, "错误", f"保存文件时出错: {str(e)}")

    def convert_command(self):
        try:
            selected_model = self.comboBox.currentText()
            selected_batch = self.comboBox2.currentText()
            selected_size = self.comboBox1.currentText()
            selected_epochs = self.lineEdit3.text()
            selected_optimizer = self.comboBox4.currentText()
            selected_hyp = self.comboBox3.currentText()
            selected_workers = self.lineEdit7.text()
            selected_project = self.lineEdit8.text()
            selected_name = self.lineEdit9.text()


            # 获取矩形训练的选项
            rect_training_option = self.comboBox5.currentText()

            # 设置矩形训练的参数
            if rect_training_option == "启用":
                rect_option = "--rect"  # 矩形训练选项
            else:
                rect_option = ""  # 不启用矩形训练

            current_dir = os.path.dirname(os.path.abspath(__file__))
            python_executable = os.path.join('C:\\Users\\13272\\anaconda3\\envs\\yolov5', 'python.exe')
            train_script = os.path.join(current_dir, 'yolov5', 'train.py')

            # 构建命令
            command = (
                f'"{python_executable}" -u "{train_script}" '
                f'--weights {selected_model}.pt '
                f'--data data/{self.yaml_file_name} '
                f'--img {selected_size} '
                f'--batch {selected_batch} '
                f'--epochs {selected_epochs} '
                f'{rect_option}'  # 添加矩形训练选项
                f' --optimizer {selected_optimizer}'
                f' --hyp data/hyps/{selected_hyp}.yaml '
                f'--workers {selected_workers} '
                f'--project {selected_project} '
                f'--name {selected_name}'





            )

            self.textEdit.setPlainText(command)
            self.textEdit1.clear()

            # 启动训练进程
            self.process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                            cwd=os.path.join(current_dir, 'yolov5'))

            # 设置定时器定期检查输出
            self.timer = QTimer(self)
            self.timer.timeout.connect(self.read_output)
            self.timer.start(50)  # 每50毫秒检查一次

        except Exception as e:
            QMessageBox.critical(self, "错误", f"生成命令时出错: {str(e)}")

    # def read_output(self):
    #     if self.process.poll() is not None:
    #         self.timer.stop()  # 停止定时器
    #
    #     output = self.process.stdout.readline()
    #     if output:
    #         ansi_escape = re.compile(r'\x1B\[[0-?9;]*[mK]')
    #         clean_output = ansi_escape.sub('', output.decode('utf-8').strip())  # 去除ANSI序列
    #         self.textEdit1.append(clean_output)

    def read_output(self):
        if self.process.poll() is not None:
            self.timer.stop()  # 停止定时器

        output = self.process.stdout.readline()
        if output:
            ansi_escape = re.compile(r'\x1B\[[0-?9;]*[mK]')
            try:
                # 尝试使用utf-8解码，并忽略无法解码的字符
                clean_output = ansi_escape.sub('', output.decode('utf-8', errors='ignore').strip())
            except UnicodeDecodeError:
                # 如果发生解码错误，使用latin-1作为备选
                clean_output = ansi_escape.sub('', output.decode('latin-1', errors='ignore').strip())

            self.textEdit1.append(clean_output)
    def open_chat_dialog(self):
            # 创建并显示聊天对话框
            self.chat_dialog = ChatDialog()
            self.chat_dialog.exec_()  # 以模态对话框形式显示







if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.setWindowTitle('YOLO训练助手')

    window.show()
    app.exec()
