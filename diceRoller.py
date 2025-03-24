import sys
import random
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout

class DiceRoller(QWidget):
    def __init__(self):
        super().__init__()

        #Die Size
        self.DieSize = 6
        
        #App Layout
        self.setWindowTitle("Dice Roller")
        self.setGeometry(100, 100, 600, 400)
        self.layout = QVBoxLayout()
        
        #Instruction Text
        self.label = QLabel("Select a die to roll:", self)
        self.label.setStyleSheet("font-size: 16px; text-align: Right;")
        self.layout.addWidget(self.label)


        #Second layout to manage die options
        self.button_layout = QHBoxLayout()

        #Buttons for Die Options
        self.buttonD4 = QPushButton("D4 ", self)
        self.buttonD4.setStyleSheet("font-size: 14px; padding: 10px;")
        self.buttonD4.setFixedSize(50, 50)
        self.buttonD4.clicked.connect(lambda:self.change_die(4))
        self.button_layout.addWidget(self.buttonD4)

        self.buttonD6 = QPushButton("D6 ", self)
        self.buttonD6.setStyleSheet("font-size: 14px; padding: 10px;")
        self.buttonD6.setFixedSize(50, 50)
        self.buttonD6.clicked.connect(lambda:self.change_die(6))
        self.button_layout.addWidget(self.buttonD6)

        self.buttonD8 = QPushButton("D8 ", self)
        self.buttonD8.setStyleSheet("font-size: 14px; padding: 10px;")
        self.buttonD8.setFixedSize(50, 50)
        self.buttonD8.clicked.connect(lambda:self.change_die(8))
        self.button_layout.addWidget(self.buttonD8)

        self.buttonD10 = QPushButton("D10", self)
        self.buttonD10.setStyleSheet("font-size: 14px; padding: 10px;")
        self.buttonD10.setFixedSize(50, 50)
        self.buttonD10.clicked.connect(lambda:self.change_die(10))
        self.button_layout.addWidget(self.buttonD10)

        self.buttonD12 = QPushButton("D12", self)
        self.buttonD12.setStyleSheet("font-size: 14px; padding: 10px;")
        self.buttonD12.setFixedSize(50, 50)
        self.buttonD12.clicked.connect(lambda:self.change_die(12))
        self.button_layout.addWidget(self.buttonD12)

        self.buttonD20 = QPushButton("D20", self)
        self.buttonD20.setStyleSheet("font-size: 14px; padding: 10px;")
        self.buttonD20.setFixedSize(50, 50)
        self.buttonD20.clicked.connect(lambda:self.change_die(20))
        self.button_layout.addWidget(self.buttonD20)

        self.layout.addLayout(self.button_layout)

        #Current Die Selected Text
        self.currDiceLabel = QLabel(f"Current Dice: {self.DieSize}", self)
        self.currDiceLabel.setStyleSheet("font-size: 16px; text-align: Right;")
        self.layout.addWidget(self.currDiceLabel)

        #Roll Dice Button and Display Result
        self.button = QPushButton("Roll Dice", self)
        self.button.setStyleSheet("font-size: 14px; padding: 10px;")
        self.button.clicked.connect(self.roll_dice)
        self.layout.addWidget(self.button)
        
        self.result_label = QLabel("", self)
        self.result_label.setStyleSheet("font-size: 20px; font-weight: bold; text-align: center;")
        self.layout.addWidget(self.result_label)
        
        self.setLayout(self.layout)

    def change_die(self, newSize):
        self.DieSize = newSize
        self.currDiceLabel.setText(f"Current Dice: {self.DieSize}")
    
    def roll_dice(self):
        roll = random.randint(1, self.DieSize)
        self.result_label.setText(f"You rolled a {roll}!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DiceRoller()
    window.show()
    sys.exit(app.exec())
