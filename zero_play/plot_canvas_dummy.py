from PySide2.QtCore import Qt
from PySide2.QtWidgets import QLabel, QWidget
from sqlalchemy.orm import Session


class PlotCanvasDummy(QLabel):
    """ A dummy view to use when Matplotlib is not installed. """
    def __init__(self, parent: QWidget):
        super().__init__('Matplotlib is not installed.', parent)
        self.setAlignment(Qt.AlignCenter)

    def requery(self, db_session: Session):
        pass
