const API_BASE =
    "http://127.0.0.1:8000";


export async function uploadContract(
    file
) {

    const formData =
        new FormData();

    formData.append(
        "file",
        file
    );

    const response =
        await fetch(
            `${API_BASE}/upload-and-analyze`,
            {
                method: "POST",
                body: formData
            }
        );

    return await response.json();
}

export async function compareContracts(
    fileA,
    fileB
) {

    const formData =
    new FormData();

    formData.append(
        "contract_a",
        fileA
    );

    formData.append(
        "contract_b",
        fileB
    );

    const response =
    await fetch(
        "http://127.0.0.1:8000/compare-contracts",
        {
            method: "POST",
            body: formData
        }
    );

    return await response.json();
}