# -*- coding: utf-8 -*-
"""
 Sorry It's a project done in a hurry, I don't have time for explanation but it's quite simple to understand I think.
 The Goal is to split à pdf in multiple pages, and its only do that.
 It miss some error management, maybe later.
 At least it's PEP8 compliant (the other file is generated, don't judge).
"""
import sys

from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PyPDF2 import PdfFileReader, PdfFileWriter

from mainwindow import Ui_MainWindow


class PdfSplitter:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.MainWindow = QMainWindow()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)

        self.ui.toolButton.clicked.connect(self.ask_file)
        self.ui.pushButton.clicked.connect(self.process)

        self.MainWindow.show()
        sys.exit(self.app.exec_())

    def ask_file(self):
        file = QFileDialog.getOpenFileName(
            parent=self.MainWindow,
            caption='Choisissez le fichier à séparer',
            filter='Fichier PDF (*.pdf)'
        )
        if file:
            self.ui.lineEdit.setText(file[0])

    def process(self):
        file = self.ui.lineEdit.text()
        pdf = PdfFileReader(file)
        for page in range(pdf.getNumPages()):
            pdf_writer = PdfFileWriter()
            pdf_writer.addPage(pdf.getPage(page))

            output = f"{'/'.join(file.split('/')[:-1])}/Page {page+1}.pdf"
            with open(output, 'wb') as output_pdf:
                pdf_writer.write(output_pdf)
        msg = QMessageBox()
        msg.setText(f"Fichier créer dans {'/'.join(file.split('/')[:-1])}")
        msg.setWindowTitle('Terminé')
        msg.exec_()


if __name__ == "__main__":
    p = PdfSplitter()
