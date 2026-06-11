import {
    renderRiskChart
}
from "./charts.js";

import {
    riskColor
}
from "./risk_display.js";

import {
    displayFinancials
}
from "./financial_breakdown.js";

const analysis =
JSON.parse(
    sessionStorage.getItem(
        "analysis"
    )
);

if (!analysis) {

    window.location.href =
        "upload.html";
}

document.getElementById(
    "summary"
).innerText =
analysis.contract_summary ||
"No Summary";

document.getElementById(
    "riskScore"
).innerText =
analysis.risk?.score ||
0;

const riskLevel =
analysis.risk?.level ||
"LOW";

const levelElement =
document.getElementById(
    "riskLevel"
);

levelElement.innerText =
riskLevel;

levelElement.style.color =
riskColor(
    riskLevel
);

/* Risk Findings */

const findingsList =
document.getElementById(
    "riskFindings"
);

(
    analysis.risk?.findings || []
)
.forEach(
    finding => {

        const li =
        document.createElement(
            "li"
        );

        li.innerText =
        finding.title ||
        finding;

        findingsList.appendChild(
            li
        );
    }
);

/* Compliance */

const complianceList =
document.getElementById(
    "compliance"
);

(
    analysis.compliance || []
)
.forEach(
    item => {

        const li =
        document.createElement(
            "li"
        );

        li.innerText =
        item;

        complianceList.appendChild(
            li
        );
    }
);

/* Recommendations */

const recommendationList =
document.getElementById(
    "recommendations"
);

(
    analysis.recommendations || []
)
.forEach(
    item => {

        const li =
        document.createElement(
            "li"
        );

        li.innerText =
        item;

        recommendationList.appendChild(
            li
        );
    }
);

displayFinancials(
    analysis.contract_data || {}
);

renderRiskChart(
    analysis.risk?.score || 0
);