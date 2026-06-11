export function renderRiskChart(
    riskScore
) {

    const ctx =
        document.getElementById(
            "riskChart"
        );

    new Chart(
        ctx,
        {

            type: "doughnut",

            data: {

                labels: [
                    "Risk",
                    "Safe"
                ],

                datasets: [

                    {
                        data: [
                            riskScore,
                            100 - riskScore
                        ]
                    }
                ]
            }
        }
    );
}