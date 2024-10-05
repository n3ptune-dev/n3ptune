import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolBar, QAction, QLineEdit, QSplitter, QTextEdit, QWidget, QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage
from PyQt5.QtCore import QSize, QUrl, Qt
from PyQt5.QtGui import QIcon, QPalette, QColor

class CustomPage(QWebEnginePage):
    def __init__(self, console_log_function):
        super().__init__()
        self.console_log_function = console_log_function

    # Overriding the method to capture JavaScript console logs
    def javaScriptConsoleMessage(self, level, message, line, source_id):
        log_message = f"JS Console [{level}]: {message} (Line: {line}, Source: {source_id})"
        self.console_log_function(log_message)  # Log to the console

    # Overriding to log network requests (not all, but useful for API requests or navigations)
    def acceptNavigationRequest(self, url, _type, isMainFrame):
        log_message = f"Navigation: {url.toString()}"
        self.console_log_function(log_message)  # Log to the console
        return super().acceptNavigationRequest(url, _type, isMainFrame)

class CustomBrowser(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up the main window
        self.setWindowTitle('Custom Dark Mode Browser with Console')
        self.setGeometry(300, 150, 1280, 720)
        
        # Main layout using QSplitter (left: browser, right: console)
        splitter = QSplitter(Qt.Horizontal)
        
        # Set up the browser
        self.browser = QWebEngineView()
        self.page = CustomPage(self.log_to_console)  # Use custom page to capture logs
        self.browser.setPage(self.page)
        self.browser.setUrl(QUrl("http://icyplus.neocities.org/search"))

        # Set up the console (QTextEdit widget to log messages)
        self.console = QTextEdit()
        self.console.setReadOnly(True)  # Make the console read-only
        
        # Add the browser and console to the splitter
        splitter.addWidget(self.browser)
        splitter.addWidget(self.console)
        splitter.setSizes([800, 400])  # Initial sizes for the browser and console

        # Set splitter as the central widget of the main window
        self.setCentralWidget(splitter)

        # Apply dark mode and set up the toolbar
        self.apply_dark_mode()
        self.create_navbar()

        # Set custom background image for the browser
        self.set_background_image('SolarBalls Banner Colorized v3.png')  # Change to your image

    def apply_dark_mode(self):
        # Dark mode colors
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(28, 28, 46))  # Dark Blueish-Black Background
        palette.setColor(QPalette.Button, QColor(28, 28, 46))  # Dark Buttons
        palette.setColor(QPalette.Base, QColor(35, 35, 52))    # Slightly Lighter Background
        palette.setColor(QPalette.Text, QColor(90, 155, 211))  # Light Blue Text
        self.setPalette(palette)

        # Console Dark Mode
        self.console.setStyleSheet("background-color: #1C1C2E; color: #5A9BD3;")

    def create_navbar(self):
        # Create a toolbar for navigation
        navbar = QToolBar()
        self.addToolBar(navbar)

        # Back button
        back_btn = QAction(QIcon('back.png'), 'Back', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        # Forward button
        forward_btn = QAction(QIcon('forward.png'), 'Forward', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        # Refresh button
        refresh_btn = QAction(QIcon('refresh.png'), 'Refresh', self)
        refresh_btn.triggered.connect(self.browser.reload)
        navbar.addAction(refresh_btn)

        # Home button
        home_btn = QAction(QIcon('home.png'), 'Home', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        # URL bar
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)
        self.browser.urlChanged.connect(self.update_url)

    def navigate_home(self):
        self.browser.setUrl(QUrl("http://www.google.com"))

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())

    def set_background_image(self, image_path):
        """Apply custom background image via CSS."""
        custom_css = f"""
        body {{
            background-image: url({image_path});
            background-size: cover;
            background-position: center;
        }}
        """
        self.browser.page().runJavaScript(f"""
            var style = document.createElement('style');
            style.type = 'text/css';
            style.innerHTML = `{custom_css}`;
            document.head.appendChild(style);
        """)

    def log_to_console(self, message):
        """Function to append log messages to the console."""
        self.console.append(message)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CustomBrowser()
    window.show()
    sys.exit(app.exec_())
