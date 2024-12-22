from PyQt5.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QListWidget, QInputDialog
from PyQt5.QtCore import Qt
from ui_components import create_ui_components
from opengl_widget import OpenGLWidget
import random
import shapes as s

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
        randomize_button, reset_button, camera_controls, light_group, camera_buttons, light_control, shape_control  = create_ui_components()
        up_btn, down_btn, left_btn, right_btn, zoom_in_btn, zoom_out_btn = camera_buttons

        ambient_light_btn, point_light_btn, area_light_btn, directional_light_btn = light_control

        shapes_list, add_shape_btn, remove_shape_btn = shape_control

        control_layout.addWidget(randomize_button)
        control_layout.addWidget(reset_button)
        control_layout.addWidget(camera_controls)
        # control_layout.addWidget(shapes_list)
        control_layout.addWidget(light_group)
        control_layout.addStretch()

        # OpenGL ekranı
        self.opengl_widget = OpenGLWidget()
        
        # Layout'ları birleştir
        main_layout.addLayout(control_layout)
        main_layout.addWidget(self.opengl_widget)

        # Butonlara tıklama olaylarını bağla
        randomize_button.clicked.connect(self.on_randomize_button_click)
        # reset_button.clicked.connect(self.on_reset_button_click)
        
        # Connect camera button signals
        up_btn.clicked.connect(lambda: self.opengl_widget.move_camera("up"))
        down_btn.clicked.connect(lambda: self.opengl_widget.move_camera("down"))
        left_btn.clicked.connect(lambda: self.opengl_widget.move_camera("left"))
        right_btn.clicked.connect(lambda: self.opengl_widget.move_camera("right"))
        zoom_in_btn.clicked.connect(lambda: self.opengl_widget.move_camera("in"))
        zoom_out_btn.clicked.connect(lambda: self.opengl_widget.move_camera("out"))

        # Connect light button signals
        ambient_light_btn.pressed.connect(lambda: self.on_light_button_toggle(0))
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

    def on_light_button_toggle(self, light_id):
        if self.opengl_widget.lights[light_id].enabled:
            self.opengl_widget.lights[light_id].disable()
        else:
            self.opengl_widget.lights[light_id].enable()
        self.opengl_widget.updateGL()



    # def on_reset_button_click(self):
    #     pass

    # def on_add_shape_button_click(self):
    #     # open a dialog to select a shape
    #     shape, ok = QInputDialog.getItem(self, "Select Shape", "Shape:", ["Cube", "Sphere", "Pyramid"], 0, False)
    #     if not ok:
    #         return

    #     # create the selected shape
    #     if shape == "Cube":
    #         shape = s.Cube()
    #     elif shape == "Sphere":
    #         shape = s.Sphere()
    #     elif shape == "Pyramid":
    #         shape = s.Pyramid()
    #     else:
    #         return

    #     # add the selected shape to the list
    #     self.opengl_widget.shapes.addItem(shape.name)
    #     self.opengl_widget.shapes.append(shape)
    #     self.opengl_widget.randomize_position(shape)
    #     self.opengl_widget.updateGL()

    def randomize_position(self, shape):
        # Assuming the view frustum is set with gluPerspective(45.0, aspect, 1.0, 100.0)
        # and the shapes are positioned within a cube of size 10 centered at (0, 0, -5)
        shape.set_random_position()
        shape.set_random_rotation()

