from Model.csv_reader import CSVReader
from Model.claim_factory import ClaimFactory
from datetime import datetime

class Controller:
    def __init__(self, main_window):
        self.main_window = main_window
        self.db = CSVReader()

    def submit_claim(self, claimant_id, first_name, last_name, monthly_income):
        try:
            income = float(monthly_income)
        except:
            return None, "รายได้ต้องเป็นตัวเลข"

        claim_id = self.db.get_new_claim_id()
        claim_factory = ClaimFactory.create_claim(claim_id, claimant_id, income)

        if not claim_factory.validate_claim_id():
            return None, "รหัสคำขอไม่ถูกต้อง (ต้องเป็นเลข 8 หลัก และไม่ขึ้นต้นด้วย 0)"

        compensation = claim_factory.calculate_compensation()
        claimant_type = claim_factory.claimant_type
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # บันทึกข้อมูล
        self.db.add_claimant(claimant_id, first_name, last_name, income, claimant_type)
        self.db.add_claim(claim_id, claimant_id, date, "calculated")
        self.db.add_compensation(claim_id, compensation, date)

        return compensation, None

    def get_all_claims(self):
        return self.db.get_all_claims()