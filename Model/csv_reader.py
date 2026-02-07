import csv
import os

class CSVReader:
    def __init__(self):
        base_path = os.path.join(os.path.dirname(__file__), '..', 'Database')
        self.claimants_file = os.path.join(base_path, 'claimants.csv')
        self.claims_file = os.path.join(base_path, 'claims.csv')
        self.compensations_file = os.path.join(base_path, 'compensations.csv')
    
    def add_claimant(self, claimant_id, first_name, last_name, monthly_income, claimant_type):
        with open(self.claimants_file, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([claimant_id, first_name, last_name, monthly_income, claimant_type])

    def add_claim(self, claim_id, claimant_id, submit_date, status):
        with open(self.claims_file, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([claim_id, claimant_id, submit_date, status])

    def add_compensation(self, claim_id, compensation_amount, calculation_date):
        with open(self.compensations_file, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([claim_id, compensation_amount, calculation_date])
    
    def get_all_claims(self):

        with open(self.claims_file, encoding='utf-8') as f:
            claims = list(csv.DictReader(f))

        with open(self.claimants_file, encoding='utf-8') as f:
            claimants = {c['claimant_id']: c for c in csv.DictReader(f)}

        with open(self.compensations_file, encoding='utf-8') as f:
            compensations = {c['claim_id']: c for c in csv.DictReader(f)}

        result = []

        for claim in claims:
            claimant = claimants.get(claim['claimant_id'])
            compensation = compensations.get(claim['claim_id'])

            if claimant and compensation:
                result.append({
                    'claim_id': claim['claim_id'],
                    'name': f"{claimant['first_name']} {claimant['last_name']}",
                    'income': claimant['monthly_income'],
                    'type': claimant['claimant_type'],
                    'date': claim['submit_date'],
                    'status': claim['status'],
                    'amount': compensation['compensation_amount']
                })

        return result
    
    def get_new_claim_id(self):

        with open(self.claims_file, encoding='utf-8') as f:
            claims = list(csv.DictReader(f))

        if not claims:
            return "10000001"

        max_id = max(int(c['claim_id']) for c in claims)
        return str(max_id + 1)