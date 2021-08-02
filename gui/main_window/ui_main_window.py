#IMPORT QT CORE
from qt_core import *

#IMPORT PAGES
from gui.pages.ui_pages import Ui_StackedWidget

#MAIN WINDOW
class UiMainWindow(object):
    def setup_ui(self, parent) -> None:
        if not parent.objectName():
            parent.setObjectName('MainWindow')
        
        #SET INITIAL PARAMETRS
        parent.resize(960, 540)
        parent.setMinimumSize(640, 340)

        #CREATE A CENTRAL WIDGET
        self.central_widget = QFrame()

        #LEFT MENU
        self.left_menu = QFrame()
        self.left_menu.setStyleSheet("background-color: #44475a")
        self.left_menu.setMinimumWidth(50)
        self.left_menu.setMaximumWidth(50)

        #LEFT MENU LAYOUT. TOP
        self.left_menu_layout = QVBoxLayout(self.left_menu)
        self.left_menu_layout.setContentsMargins(0,0,0,0)
        self.left_menu_layout.setSpacing(0)
        
        #LEFT. CREATE ICON FRAME
        self.left_menu_top_frame = QFrame()
        self.left_menu_top_frame.setMinimumHeight(50)
        self.left_menu_top_frame.setStyleSheet("background-color: red")

        #LEFT. CREATE SPACER
        self.menu_spacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        #LEFT. CREATE ICON FRAME BOTTOM
        self.left_menu_bottom_frame = QFrame()
        self.left_menu_bottom_frame.setMinimumHeight(49)
        self.left_menu_bottom_frame.setStyleSheet("background-color: red")

        #LABEL WITH VERSION APP
        self.version_app = QLabel("V. 0.0.1")
        self.version_app.setObjectName("version_app")
        self.version_app.setAlignment(Qt.AlignCenter)
        self.version_app.setStyleSheet("#version_app { font: 700 9pt 'Segoe UI'; color: #bfbfbf; }")

        #ADD TO MENU LAYOUT
        self.left_menu_layout.addWidget(self.left_menu_top_frame)
        self.left_menu_layout.addItem(self.menu_spacer)
        self.left_menu_layout.addWidget(self.left_menu_bottom_frame)
        self.left_menu_layout.addWidget(self.version_app)

        #CONTENT
        self.content = QFrame()
        self.content.setStyleSheet("background-color: #282a36")

        #CONTENT LAYOUT
        self.content_layout = QVBoxLayout(self.content)
        self.content_layout.setContentsMargins(0,0,0,0)
        self.content_layout.setSpacing(0)


        #TOP BAR
        self.top_bar = QFrame()
        self.top_bar.setMinimumHeight(30)
        self.top_bar.setMaximumHeight(30)
        self.top_bar.setStyleSheet(
                "background-color: #21232d; color: #6277a4"
            )
        
        #TOP BAR LAYOUT
        self.top_bar_layout = QHBoxLayout(self.top_bar)
        self.top_bar_layout.setContentsMargins(10,0,10,0)
        
        #TOP BAR LABEL LEFT
        self.top_label_left = QLabel('segue o pae')
        self.top_label_left.setStyleSheet("font: 700 9pt 'Segoe UI'")

        #TOP BAR SPACER
        self.top_spacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        #TOP BAR LABEL RIGHT
        self.top_label_right = QLabel('| home page')
        self.top_label_right.setStyleSheet("font: 700 9pt 'Segoe UI'")

        #ADD TO TOP BAR LAYOUT
        self.top_bar_layout.addWidget(self.top_label_left) #add a object(widget)
        self.top_bar_layout.addItem(self.top_spacer) #add a item
        self.top_bar_layout.addWidget(self.top_label_right) #add a object(widget)
        
        #APPLICATION PAGE
        self.pages = QStackedWidget()
        self.pages.setStyleSheet("font-size: 12pt; color: #6272a4")
        self.ui_pages = Ui_StackedWidget()
        self.ui_pages.setupUi(self.pages)
        self.pages.setCurrentWidget(self.ui_pages.page_2) #show this page and not the fist page

        #ADD TO CONTENT PAGE
        self.content_layout.addWidget(self.top_bar)
        self.content_layout.addWidget(self.pages)


        #CREAT MAIN LAYOUT
        self.main_layout = QHBoxLayout(self.central_widget)
        self.main_layout.setContentsMargins(0,0,0,0)
        self.main_layout.setSpacing(0)

        #ADD WIDGETS TO APP
        self.main_layout.addWidget(self.left_menu)
        self.main_layout.addWidget(self.content)

        #SET CENTRAL WIDGET
        parent.setCentralWidget(self.central_widget)