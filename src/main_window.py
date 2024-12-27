from PyQt5.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QListWidget, QInputDialog
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from ui_components import create_ui_components
from opengl_widget import OpenGLWidget
import random
import shapes as s

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("3D Room With PyOpenGL")
        self.setWindowIcon(QIcon("icon.png"))

        # Ana widget ve layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QHBoxLayout()
        central_widget.setLayout(main_layout)

        # Sol taraf (arayüz)
        control_layout = QVBoxLayout()
        # Get UI components
        randomize_button, reset_button, preset1_button, controls_group, light_group, camera_buttons, light_buttons, shape_controls = create_ui_components()
        up_btn, down_btn, left_btn, right_btn, zoom_in_btn, zoom_out_btn = camera_buttons

        ambient_light_btn, point_light_btn, area_light_btn, directional_light_btn, rgb_button = light_buttons

        shapes_list, add_shape_btn, remove_shape_btn = shape_controls

        control_layout.addWidget(randomize_button)
        control_layout.addWidget(reset_button)
        control_layout.addWidget(preset1_button)
        control_layout.addWidget(controls_group)
        control_layout.addWidget(light_group)
        control_layout.addStretch()

        # OpenGL ekranı
        self.opengl_widget = OpenGLWidget()
        
        # Layout'ları birleştir
        main_layout.addLayout(control_layout)
        main_layout.addWidget(self.opengl_widget)

        # Butonlara tıklama olaylarını bağla
        randomize_button.clicked.connect(self.on_randomize_button_click)
        reset_button.clicked.connect(self.on_reset_button_click)
        preset1_button.clicked.connect(self.on_preset1_button_click)
        
        # Connect camera button signals
        up_btn.clicked.connect(lambda: self.opengl_widget.move_camera("up"))
        down_btn.clicked.connect(lambda: self.opengl_widget.move_camera("down"))
        left_btn.clicked.connect(lambda: self.opengl_widget.move_camera("left"))
        right_btn.clicked.connect(lambda: self.opengl_widget.move_camera("right"))
        zoom_in_btn.clicked.connect(lambda: self.opengl_widget.move_camera("in"))
        zoom_out_btn.clicked.connect(lambda: self.opengl_widget.move_camera("out"))

        # Connect light button signals
        ambient_light_btn.pressed.connect(lambda: self.on_light_button_toggle(0))
        rgb_button.pressed.connect(self.on_rgb_button_toggle)
        point_light_btn.pressed.connect(lambda: self.on_light_button_toggle(1))
        area_light_btn.pressed.connect(lambda: self.on_light_button_toggle(2))
        directional_light_btn.pressed.connect(lambda: self.on_light_button_toggle(3))

        # add shapes to the list
        # shapes_list.addItems([shape.name for shape in self.opengl_widget.shapes])


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


    def on_randomize_button_click(self):
        print("Randomizing colors and positions")
        self.opengl_widget.randomize_shapes()
        self.opengl_widget.updateGL()

    def on_reset_button_click(self):
        print("Resetting scene")
        self.opengl_widget.reset_scene()
        self.opengl_widget.updateGL()

    def on_preset1_button_click(self):
        print("Applying Preset 1")
        self.opengl_widget.apply_preset1()
        self.opengl_widget.updateGL()

    def on_light_button_toggle(self, light_id):
        if self.opengl_widget.lights[light_id].enabled:
            self.opengl_widget.lights[light_id].disable()
        else:
            self.opengl_widget.lights[light_id].enable()
        self.opengl_widget.updateGL()

    def on_rgb_button_toggle(self):
        self.opengl_widget.lights[0].toggle_rgb_mode()
        self.opengl_widget.updateGL()

    def randomize_position(self, shape):
        # Assuming the view frustum is set with gluPerspective(45.0, aspect, 1.0, 100.0)
        # and the shapes are positioned within a cube of size 10 centered at (0, 0, -5)
        shape.set_random_position()
        shape.set_random_rotation()
