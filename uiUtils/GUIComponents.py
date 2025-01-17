from PySide6 import QtWidgets, QtCore, QtGui 
import Assets


TABEL_BUTTON_STYLE = """
    QPushButton{ 
        background-color: rgba(255,255,255,0);
        min-height:0px; min-width:0px; 
        width:auto;
        qproperty-iconSize: 24px;
        } 
    """

SIDEBAR_BUTTON_SELECTED_STYLE = """
QPushButton{
	color: #ffffff;
	min-height: 40px;
	text-align: left;
    margin-left:15px;
	icon-size:25px;
	background-color:rgba(0,0,0,0);

    color:rgb(255, 205, 5);
    font-size:14px;
    font-weight:bold;
    }

"""


SIDEBAR_BUTTON_STYLE = """
QPushButton{
	color: #ffffff;
	min-height: 40px;
	text-align: left;
    margin-left:15px;
	icon-size:25px;
	background-color:rgba(0,0,0,0);
    }

    QPushButton:hover{
    font-size:14px; 
    font-weight:bold;
}
"""




class editButton(QtWidgets.QPushButton):

    def __init__(self, *a, **kw):
        super(editButton, self).__init__(*a, **kw)
        self._icon_normal = QtGui.QIcon(':/assets/Assets/icons/icons8-edit-table-50.png')
        self._icon_over = QtGui.QIcon(':/assets/Assets/icons/icons8-edit-hover-table-50.png')
        self.setStyleSheet(TABEL_BUTTON_STYLE)
        self.setIcon(self._icon_normal)

    def enterEvent(self, event):
        self.setIcon(self._icon_over)
        #return super(editButton, self).enterEvent(event)

    def leaveEvent(self, event):
        self.setIcon(self._icon_normal)
        #return super(editButton, self).enterEvent(event)



class deleteButton(QtWidgets.QPushButton):

    def __init__(self, *a, **kw):
        super(deleteButton, self).__init__(*a, **kw)
        self._icon_normal = QtGui.QIcon(':/assets/Assets/icons/icons8-remove-table-50.png')
        self._icon_over = QtGui.QIcon(':/assets/Assets/icons/icons8-remove-hover-table-50.png')
        self.setStyleSheet(TABEL_BUTTON_STYLE)
        self.setIcon(self._icon_normal)

    def enterEvent(self, event):
        self.setIcon(self._icon_over)
        #return super(deleteButton, self).enterEvent(event)

    def leaveEvent(self, event):
        self.setIcon(self._icon_normal)
        #return super(deleteButton, self).enterEvent(event)



class tabelCheckbox(QtWidgets.QCheckBox):

    def __init__(self, *a, **kw):
        super(tabelCheckbox, self).__init__(*a, **kw)
        

    def set_size(self, w, h):
        self.setStyleSheet(f"""QCheckBox::indicator 
                                {{
                               width :{w}px;
                               height :{h}px;
                               }}""")

        #self.setMaximumWidth(h+5)
        #self.setMaximumWidth(w+5)



