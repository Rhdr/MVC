
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QLineEdit, QPushButton, QMainWindow


class _ViewAbstract:
    def __init__(self):
        if type(self) is _ViewAbstract:
            raise Exception(Globals.errorStr_AbstractClsInstance)

    def setup_view(self, parent):
        self._createFormObjects(parent)
        self._setupLayout(parent)
        self._customizeView(parent)
        self._setLayout(parent)

    def _createFormObjects(self, parent):
        raise Exception('')

    def _setupLayout(self, parent):
        raise Exception('')

    def _customizeView(self, parent):
        raise Exception('')

    def _setLayout(self, parent):
        if isinstance(parent, QMainWindow):
            widget = QWidget()
            widget.setLayout(self.layoutMain)
            parent.setCentralWidget(widget)
        else:
            parent.setLayout(self.layoutMain)


class ViewAccount(_ViewAbstract):
    def _createFormObjects(self, parent):
        self.lbl_name = QLabel('Account Name', parent)
        self.txt_name = QLineEdit('', parent)
        self.btn_ok = QPushButton('Ok', parent)

    def _setupLayout(self, parent):
        self.layoutMain = QGridLayout(parent)
        self.layoutMain.addWidget(self.lbl_name, 0, 0)
        self.layoutMain.addWidget(self.txt_name, 0, 1)
        self.layoutMain.addWidget(self.btn_ok, 1, 0, 1, 2)

    def _customizeView(self, parent):
        parent.resize(300, 100)


class ViewSourcedoc(_ViewAbstract):
    def setup_view(self, parent):
        print("View seting up")
        self.lbl_name = QLabel('Sourcedoc Name', parent)
        self.txt_name = QLineEdit('', parent)
        self.btn_ok = QPushButton('Ok', parent)

        self.layout = QGridLayout(parent)
        self.layout.addWidget(self.lbl_name, 0, 0)
        self.layout.addWidget(self.txt_name, 0, 1)
        self.layout.addWidget(self.btn_ok, 1, 0, 1, 2)


class ViewLineitem(_ViewAbstract):
    def setup_view(self, parent):
        print("View seting up")
        self.lbl_name = QLabel('Lineitem Name', parent)
        self.txt_name = QLineEdit('', parent)
        self.btn_ok = QPushButton('Ok', parent)

        self.layout = QGridLayout(parent)
        self.layout.addWidget(self.lbl_name, 0, 0)
        self.layout.addWidget(self.txt_name, 0, 1)
        self.layout.addWidget(self.btn_ok, 1, 0, 1, 2)


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)

    # va = _ViewAbstract()
    ctrl_account = QWidget()
    view_account = ViewAccount()
    view_account.setup_view(ctrl_account)
    ctrl_account.show()

    ctrl_sourcedoc = QWidget()
    view_sourcedoc = ViewSourcedoc()
    view_sourcedoc.setup_view(ctrl_sourcedoc)
    ctrl_sourcedoc.show()

    app.exec()
