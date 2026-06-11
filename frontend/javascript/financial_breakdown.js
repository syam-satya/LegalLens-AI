export function displayFinancials(
    contract
) {

    document.getElementById(
        "interestRate"
    ).innerText =
        contract.interest_rate || "N/A";

    document.getElementById(
        "processingFee"
    ).innerText =
        contract.processing_fee || "N/A";

    document.getElementById(
        "foreclosure"
    ).innerText =
        contract.foreclosure_charges || "N/A";
}