export function riskColor(
    level
) {

    if (level === "HIGH")
        return "red";

    if (level === "MEDIUM")
        return "orange";

    return "green";
}