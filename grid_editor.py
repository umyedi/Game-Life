from PyQt6.QtWidgets import *
import sys

# BUG
# -> Doesn't work XD

class GridWindow(QMainWindow):
    def __init__(self):
        super(GridWindow, self).__init__()

        self.grid = []
        self.grid_width = 0
        self.grid_height = 0

        self.initUI()
        self.func_mappingSignal()

    def initUI(self):
        self.setWindowTitle('Grid Example')
        self.setGeometry(100, 100, 800, 600)

        # Create a central widget to hold the grid
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QGridLayout(central_widget)

        # Create a popup to set the dimensions of the grid
        dialog = InputDialog()
        if dialog.exec():
            self.createGrid(dialog.getInputs())

        for i in range(self.grid_height):
            for j in range(self.grid_width):
                button = QPushButton('')
                button.setFixedSize(30, 30)
                button.clicked.connect(self.toggleCellColor)
                layout.addWidget(button, i, j)
                self.grid[i][j] = button
    
    def func_mappingSignal(self):
        self.grid.clicked.connect(self.func_test)

    def createGrid(self, data):
        lenght, width = int(data[0]), int(data[1])
        for i in range(width):
            self.grid.append([])
            for _ in range(lenght):
                self.grid[i].append([0])
    
    def cell_clicked(self, item):
        cellContent = item.data()
        print(cellContent)  # test
        sf = "You clicked on {}".format(cellContent)
        print(sf)

    def toggleCellColor(self):
        button = self.sender()
        current_color = button.palette().buttonText().color()
        new_color = 'black' if current_color == 'white' else 'white'
        button.setStyleSheet(f'background-color: {new_color}; color: {new_color};')

class InputDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.first = QLineEdit(self)
        self.second = QLineEdit(self)
        buttonBox = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok, self)


        layout = QFormLayout(self)
        layout.addRow("First text", self.first)
        layout.addRow("Second text", self.second)
        layout.addWidget(buttonBox)

        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

    def getInputs(self):
        return (self.first.text(), self.second.text())



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = GridWindow()
    window.show()
    sys.exit(app.exec())

