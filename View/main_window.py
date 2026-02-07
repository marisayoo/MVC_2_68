from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QMessageBox
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.controller = None
        self.setWindowTitle("ระบบคำนวณเงินเยียวยาของรัฐ")
        self.setGeometry(100, 100, 500, 400)
        
        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout()
        
        # หัวข้อ
        title = QLabel("ระบบคำนวณเงินเยียวยาของรัฐ")
        title.setStyleSheet("font-size: 18px; font-weight: bold; margin: 20px;")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)
        
        # ===== Login Section =====
        layout.addWidget(QLabel("Username:"))
        self.username = QLineEdit()
        self.username.setText("admin")
        layout.addWidget(self.username)

        layout.addWidget(QLabel("Password:"))
        self.password = QLineEdit()
        self.password.setText("1234")
        layout.addWidget(self.password)

        login_btn = QPushButton("เข้าสู่ระบบ (เจ้าหน้าที่)")
        login_btn.setMinimumWidth(30)
        login_btn.clicked.connect(self.login_officer)
        layout.addWidget(login_btn)

        line = QLabel("-----------")
        title.setStyleSheet("font-size: 18px; font-weight: bold; margin: 10px;")
        line.setAlignment(Qt.AlignCenter)
        layout.addWidget(line)

        citizen_btn = QPushButton("เข้าสู่ระบบในฐานะประชาชน")
        citizen_btn.clicked.connect(self.login_citizen)
        layout.addWidget(citizen_btn)

        self.menu = QWidget()
        menu_layout = QVBoxLayout()
        
        btn1 = QPushButton("ดูรายการคำขอเยียวยา")
        btn1.clicked.connect(self.open_claim_list)
        menu_layout.addWidget(btn1)
        
        btn2 = QPushButton("ยื่นคำขอเยียวยา")
        btn2.clicked.connect(self.open_submit_claim)
        menu_layout.addWidget(btn2)
        
        self.menu.setLayout(menu_layout)
        self.menu.hide()
        layout.addWidget(self.menu)
        
        layout.addStretch()
        central.setLayout(layout)

    def open_claim_list(self):
        from View.claim_list_view import ClaimListView
        self.hide()
        self.claim_list_view = ClaimListView(self.controller)
        self.claim_list_view.show()

    def open_submit_claim(self):
        from View.submit_claim_view import SubmitClaimView
        self.hide()
        self.submit_claim_view = SubmitClaimView(self.controller)
        self.submit_claim_view.show()

    def login_officer(self):
        if self.username.text() == "admin" and self.password.text() == "1234":
            self.controller.current_user = "officer"
            self.menu.show()
        else:
            QMessageBox.warning(self, "ผิดพลาด", "Username หรือ Password ไม่ถูกต้อง")

    def login_citizen(self):
        self.controller.current_user = "citizen"
        self.menu.show()
    
    def set_controller(self, controller):
        self.controller = controller
