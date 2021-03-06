from PyQt4 import QtGui
import sys

class PrettyWidget(QtGui.QWidget):

    def __init__(self):
        super(PrettyWidget, self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(600, 300, 400, 200)
        self.setWindowTitle('Table')

        # Grid Layout
        grid = QtGui.QGridLayout()
        self.setLayout(grid)

        # Data
        data = {'Kitty': ['1', '2', '3', '3'],
                'Cat': ['4', '5', '6', '2'],
                'Meow': ['7', '8', '9', '5'],
                'Purr': ['4', '3', '4', '8'],
                'Furr': ['5', '5', '4', '4'],
                'Curr': ['6', '6', '6', '6'],
                }

        # Create Empty 5x5 Table
        table = QtGui.QTableWidget(self)
        table.setRowCount(4)
        table.setColumnCount(len(data.keys()))

        # Enter data onto Table
        horHeaders = []
        for n, key in enumerate(sorted(data.keys())):
            horHeaders.append(key)
            for m, item in enumerate(data[key]):
                newitem = QtGui.QTableWidgetItem(item)
                table.setItem(m, n, newitem)

        # Add Header
        table.setHorizontalHeaderLabels(horHeaders)

        # Adjust size of Table
        table.resizeColumnsToContents()
        table.resizeRowsToContents()

        # Add Table to Grid
        grid.addWidget(table, 0, 0)

        self.show()

def main():
    app = QtGui.QApplication(sys.argv)
    w = PrettyWidget()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()