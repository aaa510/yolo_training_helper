from PyQt5.QtWidgets import QDialog, QVBoxLayout, QTextEdit, QPushButton
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtGui import QFont
from ollama import chat


# AIWorker类，继承自QThread，用于在后台线程中处理与AI的交互
class AIWorker(QThread):
    update_signal = pyqtSignal(str)  # 自定义信号，用于更新UI上的聊天内容

    def __init__(self, user_input):
        super().__init__()
        self.user_input = user_input  # 接收用户输入

    def run(self):
        try:
            # 使用Ollama API与AI模型进行对话，启动流式响应
            stream = chat(
                model='deepseek-r1:latest',
                messages=[{'role': 'user', 'content': self.user_input}],
                stream=True,
            )

            # 遍历返回的流式数据，逐块接收消息
            for chunk in stream:
                content = chunk['message']['content']
                self.update_signal.emit(content)  # 将接收到的内容通过信号发射到UI
        except Exception as e:
            self.update_signal.emit(f"\n[Error] {str(e)}")  # 如果出现异常，发射错误信息


# DeepSeek 聊天对话框
class ChatDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("DeepSeek 帮助中心")  # 设置窗口标题
        self.resize(600, 500)  # 设置窗口大小

        # 设置全局字体
        font = QFont("黑体", 10)
        self.setFont(font)

        layout = QVBoxLayout()  # 创建垂直布局

        # 聊天显示框
        self.chat_display = QTextEdit()
        self.chat_display.setReadOnly(True)
        self.chat_display.setStyleSheet("""
            background-color: #f0f0f0;
            padding: 10px;
            border: 1px solid #AAB7B8;
        """)

        # 输入框
        self.input_area = QTextEdit()
        self.input_area.setMaximumHeight(100)
        self.input_area.setPlaceholderText("输入您的问题...")
        self.input_area.setStyleSheet("""
            background-color: white;
            padding: 10px;
            border: 1px solid #AAB7B8;
        """)

        # 发送按钮
        self.send_btn = QPushButton("提问", self)
        self.send_btn.setFixedHeight(30)
        self.send_btn.clicked.connect(self.send_message)  # 点击按钮时调用send_message

        # 将组件添加到布局中
        layout.addWidget(self.chat_display)
        layout.addWidget(self.input_area)
        layout.addWidget(self.send_btn)
        self.setLayout(layout)

    def send_message(self):
        # 获取用户输入的文本并去掉空白
        user_input = self.input_area.toPlainText().strip()
        if not user_input:
            return  # 如果输入为空，返回

        # 在聊天窗口中显示用户输入的消息
        self._append_message("You", user_input)
        self.input_area.clear()  # 清空输入框

        # 在聊天窗口中显示“思考中...”提示
        self._append_message("Bot", "思考中...", is_streaming=True)

        # 启动后台线程，处理与AI的对话
        self.ai_thread = AIWorker(user_input)
        self.ai_thread.update_signal.connect(self.update_bot_response)  # 连接信号和槽函数
        self.ai_thread.finished.connect(self.finalize_response)  # 连接线程完成后的槽函数
        self.ai_thread.start()  # 启动线程

    def _append_message(self, sender, message, is_streaming=False):
        # 获取文本光标，确保内容插入到聊天窗口的末尾
        cursor = self.chat_display.textCursor()
        cursor.movePosition(cursor.End)

        # 设置消息的前缀和颜色
        if sender == "You":
            prefix = "\nYou: "
            color = "#333333"  # 用户消息颜色
        else:
            prefix = "\nBot: "
            color = "#2196F3" if not is_streaming else "#888888"  # 机器人消息颜色

        # 插入消息
        cursor.insertText(prefix)
        cursor.insertHtml(f'<span style="color:{color}">{message}</span>')
        self.chat_display.ensureCursorVisible()  # 确保文本框显示最新内容

    def update_bot_response(self, content):
        # 如果聊天框正在显示“思考中...”提示，则替换为实际响应内容
        current_text = self.chat_display.toPlainText()
        if current_text.endswith("思考中..."):
            self.chat_display.setPlainText(current_text[:-4] + content)
        else:
            # 否则直接插入新的消息
            cursor = self.chat_display.textCursor()
            cursor.movePosition(cursor.End)
            cursor.insertText(content)
        self.chat_display.ensureCursorVisible()

    def finalize_response(self):
        # 确保最后有换行符，使聊天内容整洁
        current = self.chat_display.toPlainText()
        if not current.endswith("\n"):
            self.chat_display.append("")