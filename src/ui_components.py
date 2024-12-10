# src/ui_components.py
from PyQt5.QtWidgets import (QPushButton, QSlider, QVBoxLayout, 
                           QHBoxLayout, QWidget, QGroupBox)
from PyQt5.QtCore import Qt

def create_ui_components():
    # Create a group box for controls
    controls_group = QGroupBox("Controls")
    controls_group.setMaximumWidth(120)  # Limit width
    
    controls_layout = QVBoxLayout()
    
    # Main buttons - make them smaller
    button1 = QPushButton("Random")
    button2 = QPushButton("Reset")
    
    # Camera controls in compact layout
    camera_group = QGroupBox("Camera")
    camera_layout = QVBoxLayout()
    
    up_btn = QPushButton("↑")
    down_btn = QPushButton("↓")
    left_btn = QPushButton("←")
    right_btn = QPushButton("→")

    
    # Make buttons smaller
    for btn in [up_btn, down_btn, left_btn, right_btn]:
        btn.setMaximumWidth(40)
        btn.setMaximumHeight(40)
    
    # Arrange camera buttons
    center_row = QHBoxLayout()
    center_row.addWidget(left_btn)
    center_row.addWidget(right_btn)
    
    camera_layout.addWidget(up_btn, alignment=Qt.AlignCenter)
    camera_layout.addLayout(center_row)
    camera_layout.addWidget(down_btn, alignment=Qt.AlignCenter)
    
    camera_group.setLayout(camera_layout)
    camera_group.setMinimumWidth(100)
    
    # Add all components to main layout
    controls_layout.addWidget(button1)
    controls_layout.addWidget(button2)
    controls_layout.addWidget(camera_group)
    controls_layout.addStretch()
    
    controls_group.setLayout(controls_layout)

    return button1, button2, None, controls_group, (up_btn, down_btn, left_btn, right_btn)