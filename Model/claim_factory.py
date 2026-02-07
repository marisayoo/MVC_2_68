from Model.claim_model import Claim
from Model.low_claim_model import LowIncomeClaim
from Model.high_claim_model import HighIncomeClaim

class ClaimFactory:

    def create_claim(claim_id, claimant_id, income):

        if income < 6500:
            return LowIncomeClaim(claim_id, claimant_id, income)

        elif income >= 50000:
            return HighIncomeClaim(claim_id, claimant_id, income)

        else:
            return Claim(claim_id, claimant_id, income)
