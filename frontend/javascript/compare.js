import {
    compareContracts
}
from "./api.js";


document
.getElementById(
    "compareBtn"
)
.addEventListener(
    "click",
    async () => {

        const fileA =
        document
        .getElementById(
            "contractA"
        )
        .files[0];

        const fileB =
        document
        .getElementById(
            "contractB"
        )
        .files[0];

        if (
            !fileA ||
            !fileB
        ) {

            alert(
                "Select both contracts"
            );

            return;
        }

        const result =
        await compareContracts(
            fileA,
            fileB
        );

        renderComparison(
            result
        );
    }
);


function renderComparison(
    result
) {

    document
    .getElementById(
        "comparisonResult"
    )
    .innerHTML = `

<h2>
Comparison Result
</h2>

<p>
Interest Winner:
${result.interest_rate_winner}
</p>

<p>
Processing Fee Winner:
${result.processing_fee_winner}
</p>

<p>
Foreclosure Winner:
${result.foreclosure_winner}
</p>

<p>
Risk Winner:
${result.risk_score_winner}
</p>

<h3>
Overall Winner:
${result.overall_winner}
</h3>

<h3>
AI Recommendation
</h3>

<p>
${result.explanation}
</p>
`;
}