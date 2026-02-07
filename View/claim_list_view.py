from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt

class ClaimListView(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.setWindowTitle("รายการคำขอเยียวยา")
        self.setGeometry(100, 100, 900, 500)
        
        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout()
        
        # หัวข้อ
        title = QLabel("รายการคำขอเยียวยาทั้งหมด")
        title.setStyleSheet("font-size: 16px; font-weight: bold;")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)
        
        # ตาราง
        self.table = QTableWidget()
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels([
            "รหัสคำขอ", "ชื่อผู้ขอ", "รายได้/เดือน", "ประเภท", 
            "วันที่ยื่น", "สถานะ", "เงินเยียวยา"
        ])
        self.load_data()
        layout.addWidget(self.table)
        
        # ปุ่มกลับ
        back_btn = QPushButton("กลับ")
        back_btn.setStyleSheet("padding: 10px;")
        back_btn.clicked.connect(self.go_back)
        layout.addWidget(back_btn)
        
        central.setLayout(layout)
    
    def load_data(self):
        claims = self.controller.get_all_claims()
        self.table.setRowCount(len(claims))
        
        for i, c in enumerate(claims):
            self.table.setItem(i, 0, QTableWidgetItem(c['claim_id']))
            self.table.setItem(i, 1, QTableWidgetItem(c['name']))
            self.table.setItem(i, 2, QTableWidgetItem(f"{float(c['income']):,.0f}"))
            self.table.setItem(i, 3, QTableWidgetItem(c['type']))
            self.table.setItem(i, 4, QTableWidgetItem(c['date']))
            self.table.setItem(i, 5, QTableWidgetItem(c['status']))
            self.table.setItem(i, 6, QTableWidgetItem(f"{float(c['amount']):,.0f}"))

    
    def go_back(self):
        self.close()
        self.controller.main_window.show()