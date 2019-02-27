
#Create a simple window demo
# import sys
# from PyQt5.QtWidgets import QApplication,QWidget
#
# if __name__=='__main__':
#     app=QApplication(sys.argv)
#     w=QWidget()
#     w.resize(250,150)
#     w.move(300,300)
#     w.setWindowTitle('MyWindow')
#     w.show()
#     sys.exit(app.exec_())


#Add a icon for window

# import sys
# from PyQt5.QtWidgets import QApplication,QWidget
# from PyQt5.QtGui import QIcon
#
# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         self.setGeometry(300,300,300,220)
#         self.resize(600,600)
#         self.setWindowTitle('Icon')
#         self.setWindowIcon(QIcon('./images/Icon.png'))
#         self.show()
#
# if __name__=='__main__':
#     app=QApplication(sys.argv)
#     ex=Example()
#     sys.exit(app.exec_())


#Tooltip demo

# import sys
# from PyQt5.QtGui import QIcon
# from PyQt5.QtWidgets import (QWidget,QToolTip,
#                 QPushButton,QApplication)
# from PyQt5.QtGui import QFont
#
# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         self.setWindowTitle('Icon')
#         self.setWindowIcon(QIcon('./image/Icon.png'))
#         QToolTip.setFont(QFont('SansSerif',10))
#         self.setToolTip('This is a <b>QWidget</b> widget')
#         btn=QPushButton('Button',self)
#         btn.setToolTip('This is a <b>QPushButton</b> widget')
#         btn.resize(btn.sizeHint())
#         btn.move(50,50)
#
#         self.setGeometry(300,300,300,200)
#         self.setWindowTitle('ToolTips')
#         self.show()
#
# if __name__=='__main__':
#     app=QApplication(sys.argv)
#     ex=Example()
#     sys.exit(app.exec_())

#MessageBox demo

# import sys
# from PyQt5.QtWidgets import QWidget,QMessageBox,QApplication
#
# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         self.setGeometry(300,300,250,150)
#         self.setWindowTitle('Message Box')
#         self.show()
#
#     def closeEvent(self,event):
#         reply=QMessageBox.question(self,'Message',
#             "Are you sure to quit ?",QMessageBox.Yes|
#             QMessageBox.No,QMessageBox.Yes)
#         if reply==QMessageBox.Yes:
#             event.accept()
#         else:
#             event.ignore()
#
# if __name__=='__main__':
#     app=QApplication(sys.argv)
#     ex=Example()
#     sys.exit(app.exec_())

# import sys
# from PyQt5.QtWidgets import QWidget,QPushButton,QApplication
# from PyQt5.QtCore import QCoreApplication
#
# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         qbtn=QPushButton('Quit',self)
#         qbtn.clicked.connect(QCoreApplication.instance().quit)
#         qbtn.resize(qbtn.sizeHint())
#         qbtn.move(50,50)
#
#         self.setGeometry(300,300,250,150)
#         self.setWindowTitle('Quit button')
#         self.show()
#
# if __name__=='__main__':
#     app=QApplication(sys.argv)
#     ex=Example()
#     sys.exit(app.exec_())

# import sys
# from PyQt5.QtWidgets import QWidget,QDesktopWidget,QApplication
#
# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         self.resize(250,150)
#         self.center()
#
#         self.setWindowTitle('Center')
#         self.show()
#
#     def center(self):
#         qr=self.frameGeometry()
#         cp=QDesktopWidget().availableGeometry().center()
#         qr.moveCenter(cp)
#         self.move(qr.topLeft())
#
# if __name__=='__main__':
#     app=QApplication(sys.argv)
#     ex=Example()
#     sys.exit(app.exec_())


#Toobar Demo

# import sys
# from PyQt5.QtWidgets import QMainWindow,QApplication
#
# class Example(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         self.statusBar().showMessage('Ready')
#         self.setGeometry(300,300,250,150)
#         self.setWindowTitle('StatusBar')
#         self.show()
#
# if __name__=='__main__':
#     app=QApplication(sys.argv)
#     ex=Example()
#     sys.exit(app.exec_())
#
# import sys
# from PyQt5.QtWidgets import QMainWindow,QAction,qApp,QApplication
# from PyQt5.QtGui import QIcon
#
# class Example(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         exitAction=QAction(QIcon('./images/Icon.png'),'&Exit',self)
#         exitAction.setShortcut('Ctrl+Q')
#         exitAction.setStatusTip('Exit application')
#         exitAction.triggered.connect(qApp.quit)
#
#         self.statusBar()
#
#         menubar=self.menuBar()
#         fileMenu=menubar.addMenu('&File')
#         fileMenu.addAction(exitAction)
#
#         self.setGeometry(300,300,300,200)
#         self.setWindowTitle('Menubar')
#         self.show()
#
# if __name__=='__main__':
#     app=QApplication(sys.argv)
#     ex=Example()
#     sys.exit(app.exec_())