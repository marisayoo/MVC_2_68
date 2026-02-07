from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QFormLayout, QMessageBox
from View.claim_list_view import ClaimListView

class SubmitClaimView(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.setWindowTitle("ยื่นคำขอเยียวยา")
        self.setGeometry(100, 100, 450, 250)
        
        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout()
        
        # หัวข้อ
        title = QLabel("ยื่นคำขอเยียวยา")
        title.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(title)
        
        # ฟอร์ม
        form = QFormLayout()
        self.claimant_id = QLineEdit()
        self.first_name = QLineEdit()
        self.last_name = QLineEdit()
        self.income = QLineEdit()
        
        form.addRow("รหัสผู้ขอ:", self.claimant_id)
        form.addRow("ชื่อ:", self.first_name)
        form.addRow("นามสกุล:", self.last_name)
        form.addRow("รายได้/เดือน:", self.income)
        layout.addLayout(form)
        
        # ปุ่ม
        submit_btn = QPushButton("คำนวณและยื่นคำขอ")
        submit_btn.setStyleSheet("padding: 10px;")
        submit_btn.clicked.connect(self.submit)
        layout.addWidget(submit_btn)
        
        back_btn = QPushButton("กลับ")
        back_btn.setStyleSheet("padding: 10px;")
        back_btn.clicked.connect(self.go_back)
        layout.addWidget(back_btn)
        
        central.setLayout(layout)
    
    def submit(self):
        # ตรวจสอบข้อมูล
        if not all([self.claimant_id.text(), self.first_name.text(), 
                    self.last_name.text(), self.income.text()]):
            QMessageBox.warning(self, "ข้อผิดพลาด", "กรุณากรอกข้อมูลให้ครบ")
            return
        
        # ส่งข้อมูลไป Controller
        amount, error = self.controller.submit_claim(
            self.claimant_id.text(),
            self.first_name.text(),
            self.last_name.text(),
            self.income.text()
        )
        
        if error:
            QMessageBox.warning(self, "ข้อผิดพลาด", error)
            return
        
        self.close()
        self.claim_list_view = ClaimListView(self.controller)
        self.claim_list_view.show()
    
    def go_back(self):
        self.close()
        self.controller.back_to_main()