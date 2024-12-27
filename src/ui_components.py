# src/ui_components.py
from PyQt5.QtWidgets import QGroupBox, QVBoxLayout, QPushButton, QHBoxLayout, QListWidget
from PyQt5.QtCore import Qt

def create_camera_controls():
    camera_group = QGroupBox("Camera")
    camera_layout = QVBoxLayout()

    up_button = QPushButton("↑")
    down_button = QPushButton("↓")
    left_button = QPushButton("←")
    right_button = QPushButton("→")
    zoom_in_button = QPushButton("+")
    zoom_out_button = QPushButton("-")

    for button in [up_button, down_button, left_button, right_button, zoom_in_button, zoom_out_button]:
        button.setMaximumWidth(40)
        button.setMaximumHeight(40)

    center_row = QHBoxLayout()
    center_row.addWidget(left_button)
    center_row.addWidget(right_button)

    camera_layout.addWidget(up_button, alignment=Qt.AlignCenter)
    camera_layout.addLayout(center_row)
    camera_layout.addWidget(down_button, alignment=Qt.AlignCenter)

    zoom_row = QHBoxLayout()
    zoom_row.addWidget(zoom_in_button)
    zoom_row.addWidget(zoom_out_button)

    camera_layout.addLayout(zoom_row)

    camera_group.setLayout(camera_layout)
    camera_group.setMinimumWidth(100)

    return camera_group, [up_button, down_button, left_button, right_button, zoom_in_button, zoom_out_button]

def create_light_controls():
    light_group = QGroupBox("Lights")
    light_layout = QVBoxLayout()

    ambient_light_row = QHBoxLayout()
    ambient_light_button = QPushButton("Ambient Light", checkable=True)
    rgb_button = QPushButton("RGB", checkable=True)
    ambient_light_row.addWidget(ambient_light_button)
    ambient_light_row.addWidget(rgb_button)

    point_light_button = QPushButton("Point Light", checkable=True)
    area_light_button = QPushButton("Area Light", checkable=True)
    directional_light_button = QPushButton("Directional Light", checkable=True)

    for button in [ambient_light_button, point_light_button, area_light_button, directional_light_button, rgb_button]:
        button.setMaximumWidth(120)

    light_layout.addLayout(ambient_light_row)
    light_layout.addWidget(point_light_button)
    light_layout.addWidget(area_light_button)
    light_layout.addWidget(directional_light_button)

    light_group.setLayout(light_layout)
    light_group.setMaximumWidth(160)

    return light_group, [ambient_light_button, point_light_button, area_light_button, directional_light_button, rgb_button]

def create_ui_components():
    controls_group = QGroupBox("Controls")
    controls_group.setMaximumWidth(120)

    controls_layout = QVBoxLayout()

    randomize_button = QPushButton("Random")
    reset_button = QPushButton("Reset")
    preset1_button = QPushButton("Preset 1", checkable=True)

    randomize_button.setMaximumWidth(100)
    reset_button.setMaximumWidth(100)
    preset1_button.setMaximumWidth(100)

    camera_group, camera_buttons = create_camera_controls()
    light_group, light_buttons = create_light_controls()

    shapes_list = QListWidget()
    shapes_list.setMaximumWidth(120)

    add_shape_button = QPushButton("+")
    remove_shape_button = QPushButton("-")

    controls_layout.addWidget(randomize_button)
    controls_layout.addWidget(reset_button)
    controls_layout.addWidget(preset1_button)
    controls_layout.addWidget(camera_group)
    controls_layout.addWidget(light_group)
    controls_layout.addStretch()

    controls_group.setLayout(controls_layout)

    return randomize_button, reset_button, preset1_button, controls_group, light_group, camera_buttons, light_buttons, [shapes_list, add_shape_button, remove_shape_button]
