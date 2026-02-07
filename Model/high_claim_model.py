# Claim ประเภทผู้มีรายได้สูง คือผู้ที่มีรายได้ >= 50000 บาทต่อเดือน
# จะได้เงินเยียวยาตามรายได้ต่อเดือน หารด้วย 5 แต่ไม่เกิน 20000 บาท

class HighIncomeClaim:
    
    def __init__(self, claim_id, claimant_id, monthly_income):
        self.claim_id = claim_id
        self.claimant_id = claimant_id
        self.monthly_income = monthly_income
        self.claimant_type = "high"
    
    def calculate_compensation(self):
        if self.monthly_income >= 50000:
            compensation = min(self.monthly_income/5, 20000)
            return compensation
        return 0
    
    # เลข 8 หลัก โดยตัวแรกไม่ขึ้นต้นด้วย 0
    def validate_claim_id(self):
        claim_id_str = str(self.claim_id)
        return (claim_id_str.isdigit() and 
                len(claim_id_str) == 8 and 
                claim_id_str[0] != '0')