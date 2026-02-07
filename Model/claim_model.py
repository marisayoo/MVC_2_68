# Claim ประเภททั่วไป คือผู้ที่มีรายได้ >= 6500 บาท และ <= 50000 บาทต่อเดือน 
# จะได้เงินเยียวยาตามรายได้ต่อเดือน แต่ไม่เกิน 20000 บาท

class Claim:
    
    def __init__(self, claim_id, claimant_id, monthly_income):
        self.claim_id = claim_id
        self.claimant_id = claimant_id
        self.monthly_income = monthly_income
        self.claimant_type = "middle"
    
    def calculate_compensation(self):
        if 6500 <= self.monthly_income <= 50000:
            compensation = min(self.monthly_income, 20000)
            return compensation
        return 0
    
    # เลข 8 หลัก โดยตัวแรกไม่ขึ้นต้นด้วย 0
    def validate_claim_id(self):
        claim_id_str = str(self.claim_id)
        return (claim_id_str.isdigit() and 
                len(claim_id_str) == 8 and 
                claim_id_str[0] != '0')