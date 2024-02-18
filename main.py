import sys
import os
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QPainter, QBrush, QColor
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QGraphicsScene, QGraphicsView, QGraphicsRectItem, QVBoxLayout, QWidget, QLineEdit, QInputDialog, QGraphicsTextItem, QFileDialog


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(791, 637)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        # Control Side - Buttons
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setText("Add command block")

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setText("Add mouse block")

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setText("Add keyboard block")

        self.saveButton = QPushButton(self.centralwidget)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setText("Save")

        self.openButton = QPushButton(self.centralwidget)
        self.openButton.setObjectName(u"openButton")
        self.openButton.setText("Open from File")

        self.layout = QVBoxLayout(self.centralwidget)
        self.layout.addWidget(self.pushButton)
        self.layout.addWidget(self.pushButton_2)
        self.layout.addWidget(self.pushButton_3)
        self.layout.addStretch()  # Add stretch to push buttons to the top
        self.layout.addWidget(self.saveButton)  # Save button
        self.layout.addWidget(self.openButton)  # Open button

        # View Side - Graphics View
        self.view = QGraphicsView(self.centralwidget)
        self.view.setGeometry(300, 50, 450, 500)
        self.scene = QGraphicsScene()
        self.view.setScene(self.scene)

        self.layout.addWidget(self.view)
        MainWindow.setCentralWidget(self.centralwidget)

        # List to store block information
        self.block_list = []

        self.retranslateUi(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle("MainWindow")


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Connect buttons to slots
        self.pushButton.clicked.connect(self.add_command_block)
        self.pushButton_2.clicked.connect(self.add_mouse_block)
        self.pushButton_3.clicked.connect(self.add_keyboard_block)
        self.saveButton.clicked.connect(self.save_block_list)
        self.openButton.clicked.connect(self.open_from_file)
        self.runButton = QPushButton(self.centralwidget)
        self.runButton.setObjectName(u"runButton")
        self.runButton.setText("Run")
        self.layout.addWidget(self.runButton)
        self.runButton.clicked.connect(self.run_application)

        # Adding the "Wait" button
        self.waitButton = QPushButton(self.centralwidget)
        self.waitButton.setObjectName(u"waitButton")
        self.waitButton.setText("Wait")
        self.layout.addWidget(self.waitButton)
        self.waitButton.clicked.connect(self.add_wait_block)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.resume_execution)

    def add_wait_block(self):
        seconds, ok = QInputDialog.getInt(self, "Enter Wait Time", "Enter wait time in seconds:")
        if ok:
            self.add_block(3, f"Wait: {seconds} seconds", QColor(255, 255, 0))  # Yellow color for wait block
            self.block_list.append((3, seconds))
            self.wait_time = seconds
            self.start_wait_timer()

    def start_wait_timer(self):
        self.timer.start(self.wait_time * 1000)  # Convert seconds to milliseconds

    def resume_execution(self):
        self.timer.stop()
        print(f"Wait: {self.wait_time} seconds completed.")
        # Continue with the rest of the execution if needed

    def run_application(self):
        print("Run")
        print(self.block_list)
        for t in self.block_list:
            print(t)
            if t[0] == 3:
                self.start_wait_timer()
            if t[0] == 1:
                pass
            if t[0] == 2:
                pass

            if t[0] == 0:
                os.system(t[1])

    def add_command_block(self):
        commands, ok = QInputDialog.getText(self, "Enter Commands", "Enter commands to be run:")
        if ok and commands:
            self.add_block(0, commands, QColor(0, 255, 0))  # Green color for command block

    def add_mouse_block(self):
        x, ok1 = QInputDialog.getInt(self, "Enter X Coordinate", "Enter X coordinate:")
        y, ok2 = QInputDialog.getInt(self, "Enter Y Coordinate", "Enter Y coordinate:")
        if ok1 and ok2:
            self.add_block(1, (x, y), QColor(255, 0, 0))  # Red color for mouse block

    def add_keyboard_block(self):
        text, ok = QInputDialog.getText(self, "Enter Text", "Enter text to be typed:")
        if ok and text:
            self.add_block(2, text, QColor(0, 0, 255))  # Blue color for keyboard block

    def add_block(self, block_type, content, color):
        rect_item = QGraphicsRectItem(0, 0, 100, 50)
        rect_item.setBrush(QBrush(color))  # Assign color based on block type
        rect_item.setPos(0, len(self.scene.items()) * 60)  # Adjust the position based on existing items
        text_item = QGraphicsTextItem(str(content))  # Display content in the block
        text_item.setPos(10, len(self.scene.items()) * 60 + 10)  # Adjust the position for text
        self.scene.addItem(rect_item)
        self.scene.addItem(text_item)

        # Append block information to the list
        self.block_list.append((block_type, content))

        # Print the updated block list to the console
        print("Updated Block List:", self.block_list)

    def save_block_list(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Save Block List", "", "Text Files (*.txt);;All Files (*)")
        if file_path:
            with open(file_path, 'w') as file:
                for block_type, content in self.block_list:
                    file.write(f"{block_type}: {content}\n")
            print(f"Block list saved to: {file_path}")

    def open_from_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Block List from File", "", "Text Files (*.txt);;All Files (*)")
        if file_path:
            self.clear_scene()  # Clear existing blocks
            self.block_list = []  # Clear existing block list
            with open(file_path, 'r') as file:
                for line in file:
                    parts = line.strip().split(':')
                    if len(parts) == 2:
                        block_type = int(parts[0])
                        content = parts[1].strip()
                        if block_type == 0:
                            color = QColor(0, 255, 0)  # Green for command block
                        elif block_type == 1:
                            color = QColor(255, 0, 0)  # Red for mouse block
                        elif block_type == 2:
                            color = QColor(0, 0, 255)  # Blue for keyboard block
                        else:
                            color = QColor(0, 0, 0)  # Default color if type is unknown
                        self.add_block(block_type, content, color)
                        self.block_list.append((block_type, content))
            print(f"Block list loaded from: {file_path}")

    def clear_scene(self):
        self.scene.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MyMainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
