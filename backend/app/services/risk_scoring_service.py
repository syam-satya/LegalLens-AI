from app.schemas.risk_schema import (
    RiskAnalysis,
    RiskFinding
)


class RiskScoringService:

    @staticmethod
    def analyze(contract):

        score = 0

        findings = []

        # Interest Rate

        if (
            contract.interest_rate and
            contract.interest_rate > 15
        ):
            score += 25

            findings.append(
                RiskFinding(
                    title="High Interest Rate",
                    severity="HIGH",
                    explanation=(
                        "Interest rate exceeds "
                        "15% annually."
                    )
                )
            )

        # Floating Interest

        if (
            contract.interest_type ==
            "FLOATING"
        ):
            score += 15

            findings.append(
                RiskFinding(
                    title="Floating Interest",
                    severity="MEDIUM",
                    explanation=(
                        "EMI may increase "
                        "over time."
                    )
                )
            )

        # Foreclosure

        if contract.foreclosure_charges:

            score += 10

            findings.append(
                RiskFinding(
                    title="Foreclosure Charges",
                    severity="MEDIUM",
                    explanation=(
                        "Loan closure penalty "
                        "detected."
                    )
                )
            )

        # Processing Fee

        if (
            contract.processing_fee and
            contract.processing_fee > 10000
        ):
            score += 15

            findings.append(
                RiskFinding(
                    title="High Processing Fee",
                    severity="MEDIUM",
                    explanation=(
                        "Processing fee appears "
                        "higher than normal."
                    )
                )
            )

        score = min(score, 100)

        if score >= 70:
            level = "HIGH"

        elif score >= 40:
            level = "MEDIUM"

        else:
            level = "LOW"

        return RiskAnalysis(
            score=score,
            level=level,
            findings=findings
        )