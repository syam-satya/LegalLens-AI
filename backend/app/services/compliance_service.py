class ComplianceService:

    @staticmethod
    def check(contract):

        issues = []

        if not contract.interest_rate:

            issues.append(
                "Interest rate not disclosed"
            )

        if not contract.loan_duration_months:

            issues.append(
                "Loan tenure not disclosed"
            )

        if not contract.processing_fee:

            issues.append(
                "Processing fee not disclosed"
            )

        return issues