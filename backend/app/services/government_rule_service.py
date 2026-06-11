from pathlib import Path


class GovernmentRuleService:

    @staticmethod
    def load_rule_files():

        base_path = Path(
            "app/data/government_rules"
        )

        texts = []

        for file_path in base_path.rglob("*.txt"):

            with open(
                file_path,
                "r",
                encoding="utf-8"
            ) as file:

                texts.append(
                    {
                        "filename":
                            file_path.name,

                        "content":
                            file.read()
                    }
                )

        return texts