from PyQt5.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QListWidget
from PyQt5.QtCore import Qt
from ui_components import create_ui_components
from opengl_widget import OpenGLWidget
import random

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("3D Room With PyOpenGL")

        # Ana widget ve layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QHBoxLayout()
        central_widget.setLayout(main_layout)

        # Sol taraf (arayüz)
        control_layout = QVBoxLayout()
        # Get UI components
        button1, button2, slider, camera_controls, camera_buttons = create_ui_components()
        up_btn, down_btn, left_btn, right_btn = camera_buttons

        control_layout.addWidget(button1)
        control_layout.addWidget(button2)
        control_layout.addWidget(slider)
        control_layout.addWidget(camera_controls)
        control_layout.addStretch()

        # OpenGL ekranı
        self.opengl_widget = OpenGLWidget()
        
        # Layout'ları birleştir
        main_layout.addLayout(control_layout)
        main_layout.addWidget(self.opengl_widget)

        # Butonlara tıklama olaylarını bağla
        button1.clicked.connect(self.on_button1_click)
        
        # Connect camera button signals
        up_btn.clicked.connect(lambda: self.opengl_widget.move_camera("up"))
        down_btn.clicked.connect(lambda: self.opengl_widget.move_camera("down"))
        left_btn.clicked.connect(lambda: self.opengl_widget.move_camera("left"))
        right_btn.clicked.connect(lambda: self.opengl_widget.move_camera("right"))

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_W:
            self.opengl_widget.move_camera("up")
        elif event.key() == Qt.Key_S:
            self.opengl_widget.move_camera("down")
        elif event.key() == Qt.Key_A:
            self.opengl_widget.move_camera("left")
        elif event.key() == Qt.Key_D:
            self.opengl_widget.move_camera("right")
        event.accept()


    def on_button1_click(self):
        print("Randomizing colors and positions")
        self.opengl_widget.randomize_shapes()
        
        self.opengl_widget.updateGL()

    def randomize_position(self, shape):
        # Assuming the view frustum is set with gluPerspective(45.0, aspect, 1.0, 100.0)
        # and the shapes are positioned within a cube of size 10 centered at (0, 0, -5)
        shape.set_random_position()
        shape.set_random_rotation()

