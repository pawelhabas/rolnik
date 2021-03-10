from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QGridLayout, QButtonGroup
from PyQt5.QtWidgets import QPushButton, QMessageBox
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPlainTextEdit
from PyQt5.QtCore import Qt
from fukcje import funkcje as f


class MyWindow(QWidget):
    przyciski = []
    przyciski.append({'nazwa': 'Nazwa przycisku', 'enable': True})
    buttons = []
    stat_labels = []
    stat_labels_war = {'portfel': '0', 'zwierzeta': '2', 'karma': '3', 'spichlerz': '4'}

    def __init__(self, parent=None):
        super().__init__(parent)

        self.interfejs()

    def ustaw_stat_war(self, ktore, war):
        if ktore == 'portfel':
            self.stat_war_portfel.setText(str(war))
        if ktore == 'zwierzeta':
            self.stat_war_zwierzeta.setText(war)
        if ktore == 'karma':
            self.stat_war_karma.setText(war)
        if ktore == 'spichlerz':
            self.stat_war_spichlerz.setText(war)
        print(f"Ustaw: {ktore} -> {war}")
        return

    def interfejs(self):

        #   Utworzenie układu tabelarycznego
        ukladT = QGridLayout()
        #   przyciski
        # for i in range(0, len(self.przyciski)):
        #     self.buttons.append(QPushButton(self.przyciski[i]['nazwa'], self))
        #     self.buttons[i].setEnabled(self.przyciski[i]['enable'])
        #     ukladT.addWidget(self.buttons[i], i, 0)

        #   pola tekstowe
        self.ta_main = QPlainTextEdit(self)

        self.stat_labels.append(QLabel(text="Portfel"))
        self.stat_labels.append(QLabel(text="Zwierzęta"))
        self.stat_labels.append(QLabel(text="Karma"))
        self.stat_labels.append(QLabel(text="Spichlerz"))
        for i in range(0, len(self.stat_labels)):
            ukladT.addWidget(self.stat_labels[i], 0, i)

        self.stat_war_portfel = QLabel(text=self.stat_labels_war['portfel'])
        self.stat_war_zwierzeta = QLabel(text=self.stat_labels_war['zwierzeta'])
        self.stat_war_karma = QLabel(text=self.stat_labels_war['karma'])
        self.stat_war_spichlerz = QLabel(text=self.stat_labels_war['spichlerz'])

        ukladT.addWidget(self.stat_war_portfel, 1, 0)
        ukladT.addWidget(self.stat_war_zwierzeta, 1, 1)
        ukladT.addWidget(self.stat_war_karma, 1, 2)
        ukladT.addWidget(self.stat_war_spichlerz, 1, 3)

        #   Ustawienie parametrów pól
        self.ta_main.setReadOnly(True)
        self.ta_main.resize(1180, 600)
        self.ta_main.insertPlainText("Start")

        ukladT.addWidget(self.ta_main, 2, 0, 3, len(self.stat_labels))

        # przypisanie utworzonego układu do okna
        self.setLayout(ukladT)

        self.setGeometry(50, 50, 800, 600)  # OKNO (pozycja X, pozycja Y, wielkość x, wielkość y)
        self.setWindowTitle("Okno Window")

        self.btn_grp = QButtonGroup()
        self.btn_grp.setExclusive(True)
        for but in self.buttons:
            self.btn_grp.addButton(but)

        self.btn_grp.buttonClicked.connect(self.on_click)

    def pobierz_stan(self):
        self.stat_war_portfel.setText(str(f.pobierz_stan('portfel')))
        self.stat_war_zwierzeta.setText(str(f.pobierz_stan('zwierzeta')))
        self.stat_war_karma.setText(str(f.pobierz_stan('karmy')))
        self.stat_war_spichlerz.setText(str(f.pobierz_stan('spichlerz')))

    def on_click(self, btn):
        self.ta_main.clear()
        self.ta_main.appendPlainText(str(btn.text()))

    def koniec(self):
        self.close()

    def pokaz(self):
        self.show()
        # print('START')

    def closeEvent(self, event):

        # odp = QMessageBox.question(
        #     self, 'Komunikat',
        #     "Czy na pewno koniec?",
        #     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        #
        # if odp == QMessageBox.Yes:
        #     event.accept()
        # else:
        #     event.ignore()

        event.accept()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

# if __name__ == '__main__':
#     import sys
#
#     app = QApplication(sys.argv)
#     okno = MyWindow()
#     sys.exit(app.exec_())
