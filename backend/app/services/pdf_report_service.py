from pathlib import Path
from datetime import datetime
import uuid

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak
)

from reportlab.lib.styles import (
    getSampleStyleSheet,
    ParagraphStyle
)

from reportlab.lib import colors


class PDFReportService:

    REPORT_DIR = Path("app/reports")

    @classmethod
    def generate(
        cls,
        analysis_result: dict
    ):

        cls.REPORT_DIR.mkdir(
            parents=True,
            exist_ok=True
        )

        report_id = str(uuid.uuid4())[:8]

        generated_at = (
            datetime.now()
            .strftime("%d-%m-%Y %H:%M")
        )

        report_path = (
            cls.REPORT_DIR /
            f"report_{report_id}.pdf"
        )

        doc = SimpleDocTemplate(
            str(report_path)
        )

        styles = getSampleStyleSheet()

        high_style = ParagraphStyle(
            "high",
            parent=styles["BodyText"],
            textColor=colors.red
        )

        medium_style = ParagraphStyle(
            "medium",
            parent=styles["BodyText"],
            textColor=colors.orange
        )

        low_style = ParagraphStyle(
            "low",
            parent=styles["BodyText"],
            textColor=colors.green
        )

        content = []

        # --------------------------------------------------
        # COVER PAGE
        # --------------------------------------------------

        content.append(
            Paragraph(
                "LegalLens AI",
                styles["Title"]
            )
        )

        content.append(
            Paragraph(
                "Loan & Contract Risk Analysis Report",
                styles["Heading2"]
            )
        )

        content.append(
            Spacer(1, 30)
        )

        content.append(
            Paragraph(
                f"Report ID: {report_id}",
                styles["BodyText"]
            )
        )

        content.append(
            Paragraph(
                f"Generated: {generated_at}",
                styles["BodyText"]
            )
        )

        content.append(
            PageBreak()
        )

        # --------------------------------------------------
        # CONTRACT SUMMARY
        # --------------------------------------------------

        content.append(
            Paragraph(
                "Contract Summary",
                styles["Heading1"]
            )
        )

        content.append(
            Paragraph(
                analysis_result.get(
                    "contract_summary",
                    "N/A"
                ),
                styles["BodyText"]
            )
        )

        content.append(
            Spacer(1, 20)
        )

        # --------------------------------------------------
        # RISK ASSESSMENT
        # --------------------------------------------------

        risk = analysis_result.get(
            "risk",
            {}
        )

        content.append(
            Paragraph(
                "Risk Assessment",
                styles["Heading1"]
            )
        )

        content.append(
            Paragraph(
                f"Risk Score: {risk.get('score', 0)}",
                styles["BodyText"]
            )
        )

        risk_level = risk.get(
            "level",
            "LOW"
        )

        if risk_level == "HIGH":
            level_style = high_style

        elif risk_level == "MEDIUM":
            level_style = medium_style

        else:
            level_style = low_style

        content.append(
            Paragraph(
                f"Risk Level: {risk_level}",
                level_style
            )
        )

        content.append(
            Spacer(1, 15)
        )

        # --------------------------------------------------
        # RISK FINDINGS
        # --------------------------------------------------

        content.append(
            Paragraph(
                "Risk Findings",
                styles["Heading2"]
            )
        )

        findings = risk.get(
            "findings",
            []
        )

        if findings:

            for item in findings:

                content.append(
                    Paragraph(
                        f"<b>{item.get('title', 'Risk')}</b>",
                        styles["BodyText"]
                    )
                )

                content.append(
                    Paragraph(
                        item.get(
                            "explanation",
                            "No explanation available."
                        ),
                        styles["BodyText"]
                    )
                )

                content.append(
                    Spacer(1, 8)
                )

        else:

            content.append(
                Paragraph(
                    "No risk findings detected.",
                    styles["BodyText"]
                )
            )

        content.append(
            PageBreak()
        )

        # --------------------------------------------------
        # ANALYSIS OVERVIEW
        # --------------------------------------------------

        content.append(
            Paragraph(
                "Analysis Overview",
                styles["Heading1"]
            )
        )

        content.append(
            Paragraph(
                f"Risk Score: {risk.get('score', 0)}",
                styles["BodyText"]
            )
        )

        content.append(
            Paragraph(
                f"Risk Level: {risk.get('level', 'LOW')}",
                styles["BodyText"]
            )
        )

        content.append(
            Paragraph(
                f"Findings Count: {len(findings)}",
                styles["BodyText"]
            )
        )

        content.append(
            Spacer(1, 20)
        )

        # --------------------------------------------------
        # COMPLIANCE
        # --------------------------------------------------

        content.append(
            Paragraph(
                "Compliance Findings",
                styles["Heading2"]
            )
        )

        compliance = analysis_result.get(
            "compliance",
            []
        )

        if compliance:

            for item in compliance:

                content.append(
                    Paragraph(
                        f"• {item}",
                        styles["BodyText"]
                    )
                )

        else:

            content.append(
                Paragraph(
                    "No compliance issues found.",
                    styles["BodyText"]
                )
            )

        content.append(
            PageBreak()
        )

        # --------------------------------------------------
        # RBI RULES
        # --------------------------------------------------

        content.append(
            Paragraph(
                "Relevant RBI Rules",
                styles["Heading1"]
            )
        )

        rules = analysis_result.get(
            "rules",
            []
        )

        if rules:

            for rule in rules:

                content.append(
                    Paragraph(
                        str(rule),
                        styles["BodyText"]
                    )
                )

                content.append(
                    Spacer(1, 8)
                )

        else:

            content.append(
                Paragraph(
                    "No relevant rules retrieved.",
                    styles["BodyText"]
                )
            )

        content.append(
            PageBreak()
        )

        # --------------------------------------------------
        # RECOMMENDATIONS
        # --------------------------------------------------

        content.append(
            Paragraph(
                "Recommendations",
                styles["Heading1"]
            )
        )

        recommendations = analysis_result.get(
            "recommendations",
            []
        )

        if recommendations:

            for recommendation in recommendations:

                content.append(
                    Paragraph(
                        f"• {recommendation}",
                        styles["BodyText"]
                    )
                )

        else:

            content.append(
                Paragraph(
                    "No recommendations available.",
                    styles["BodyText"]
                )
            )

        content.append(
            Spacer(1, 20)
        )

        # --------------------------------------------------
        # SIMPLIFIED CONTRACT
        # --------------------------------------------------

        content.append(
            Paragraph(
                "Simplified Contract",
                styles["Heading1"]
            )
        )

        content.append(
            Paragraph(
                analysis_result.get(
                    "simplified_contract",
                    "N/A"
                ),
                styles["BodyText"]
            )
        )

        doc.build(
            content
        )

        return str(
            report_path
        )