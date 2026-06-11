import json

from app.services.llm_service import (
    LLMService
)

from app.services.prompt_service import (
    PromptService
)


class AIAnalysisService:

    def __init__(self):

        self.llm = LLMService()

    def analyze(
        self,
        contract_data,
        retrieved_rules
    ):

        template = (
            PromptService.load_prompt(
                "risk_analysis_prompt.txt"
            )
        )

        prompt = f"""
{template}

CONTRACT DATA:

{contract_data}

RELEVANT RULES:

{retrieved_rules}
"""

        response = self.llm.generate(
            prompt
        )

        return json.loads(response)