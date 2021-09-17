from PyQt5.QtWidgets import QWidget, QMainWindow, QDialog

from models import DomainCRUDModel
from views import ViewLineitem


class _ControllerAbstract:
    # def __init__(self, session_manager, model_dict, view_dict):
    def __init__(self, concrete_cls, model_dict, view_dict, session_manager=None):
        # if type(self) is _ControllerAbstract:
        #    raise Exception('Globals.errorStr_AbstractClsMethod')
        self.__concrete_cls = concrete_cls
        self.__before_load(model_dict, view_dict, session_manager)
        self.__concrete_cls._on_load()
        self.__concrete_cls._load_model_data()
        self.__concrete_cls._view_customize()
        self.__concrete_cls._connect_signals()

    def __before_load(self, model_dict, view_dict, session_manager):
        self.__concrete_cls._model_dict = model_dict
        self.__concrete_cls._view_dict = view_dict
        self.__concrete_cls._session_manager = session_manager

    def _on_load(self):
        raise Exception('Globals.errorStr_AbstractClsMethod')

    def _load_model_data(self):
        raise Exception('Globals.errorStr_AbstractClsMethod')

    def _view_customize(self):
        raise Exception('Globals.errorStr_AbstractClsMethod')

    def _connect_signals(self):
        raise Exception('Globals.errorStr_AbstractClsMethod')


class ControllerAbstract_QWidget(QWidget):
    def __init__(self, model_dict, view_dict, session_manager=None, parent=None):
        if type(self) is ControllerAbstract_QWidget:
            raise
        else:
            super().__init__(parent)
            _ControllerAbstract(self, model_dict, view_dict, session_manager)


class ControllerAbstract_QMainWindow(QMainWindow):
    def __init__(self, model_dict, view_dict, session_manager=None, parent=None):
        if type(self) is ControllerAbstract_QWidget:
            raise
        else:
            super().__init__(parent)
            _ControllerAbstract(self, model_dict, view_dict, session_manager)


class ControllerAbstract_QDialog(QDialog):
    def __init__(self, model_dict, view_dict, session_manager=None, parent=None):
        if type(self) is ControllerAbstract_QWidget:
            raise
        else:
            super().__init__(parent)
            _ControllerAbstract(self, model_dict, view_dict, session_manager)


class ControllerAccount(ControllerAbstract_QWidget):
    def __init__(self, model_dict, view_dict, session_manager=None, parent=None):
        super().__init__(model_dict, view_dict, session_manager, parent)
        print('__init__.Controller')

    def _on_load(self):
        print('_on_load')
        self.model = self._model_dict['model']
        self.view = self._view_dict['view']
        self.view.setup_view(self)

    def _load_model_data(self):
        print('_load_model_data')

    def _view_customize(self):
        print('_view_customize')
        self.show()

    def _connect_signals(self):
        print('_connect_signals')


class ControllerSourcedoc(ControllerAbstract_QDialog):
    def __init__(self, model_dict, view_dict, session_manager=None, parent=None):
        super().__init__(model_dict, view_dict, session_manager, parent)

    def _on_load(self):
        print('_on_load')
        self.model = self._model_dict['model']
        self.view = self._view_dict['view']
        self.view.setup_view(self)

        lineitem_view = ViewLineitem()
        lineitem_model = DomainCRUDModel()
        self.lineitem_ctrl = ControllerLineitem({'model': lineitem_model},
                                                {'view': lineitem_view})

    def _load_model_data(self):
        print('_load_model_data')

    def _view_customize(self):
        print('_view_customize')
        self.show()

    def _connect_signals(self):
        print('_connect_signals')
        self.view.btn_ok.clicked.connect(self.on_ok)

    def on_ok(self):
        print(self.view.txt_name.text())
        self.lineitem_ctrl.save_sourcedoc('2020/05/03', 1)


class ControllerLineitem(ControllerAbstract_QWidget):
    def __init__(self, model_dict, view_dict, session_manager=None, parent=None):
        super().__init__(model_dict, view_dict, session_manager, parent)

    def _on_load(self):
        print('_on_load')
        self.model = self._model_dict['model']
        self.view = self._view_dict['view']
        self.view.setup_view(self)

    def _load_model_data(self):
        print('_load_model_data')

    def _view_customize(self):
        print('_view_customize')
        self.show()

    def _connect_signals(self):
        print('_connect_signals')

    def save_sourcedoc(self, date, sourcedoc_type):
        print('lineitem - saving sourcedoc')
        sd = self.model.create_sourcedoc(date, sourcedoc_type)
        self.model.create_lineitem('a', 'b', sd, 900, 0)


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    from models import DomainCRUDModel
    from views import ViewAccount, ViewSourcedoc

    app = QApplication(sys.argv)

    # i = ControllerAbstract_QWidget('', '', '')
    model = DomainCRUDModel()
    view_account = ViewAccount()
    view_sourcedoc = ViewSourcedoc()
    ctrlA = ControllerAccount({'model': model}, {'view': view_account})
    ctrlB = ControllerSourcedoc({'model': model}, {'view': view_sourcedoc})

    app.exec()
