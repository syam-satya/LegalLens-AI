import json

from json_repair import repair_json

from app.services.llm_service import LLMService
from app.services.prompt_service import PromptService


class AIExplanationService:

    def __init__(self):

        self.llm = LLMService()

    def generate_summary(
        self,
        contract_data,
        risk_analysis,
        compliance_issues,
        retrieved_rules
    ):

        template = PromptService.load(
            "contract_summary_prompt.txt"
        )

        prompt = f"""
{template}

CONTRACT:

{contract_data}

RISK ANALYSIS:

{risk_analysis}

COMPLIANCE:

{compliance_issues}

RULES:

{retrieved_rules}

Required JSON format:

{{
  "contract_summary": "",
  "borrower_explanation": "",
  "recommendations": []
}}
"""

        try:

            response = self.llm.generate(
                prompt
            )

            response = repair_json(
                response
            )

            return json.loads(
                response
            )

        except Exception as e:

            return {
                "contract_summary":
                    "Failed to generate summary.",

                "borrower_explanation":
                    str(e),

                "recommendations": []
            }

    def simplify_contract(
        self,
        contract_text
    ):

        template = PromptService.load(
            "simplification_prompt.txt"
        )

        prompt = f"""
{template}

CONTRACT:

{contract_text}
"""

        return self.llm.generate(
            prompt
        )