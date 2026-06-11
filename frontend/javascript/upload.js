import {
    uploadContract
}
from "./api.js";


const uploadBtn =
document.getElementById(
    "uploadBtn"
);

uploadBtn.addEventListener(
    "click",
    async () => {

        const file =
        document.getElementById(
            "contractFile"
        ).files[0];

        if (!file) {

            alert(
                "Please select a PDF"
            );

            return;
        }

        document.getElementById(
            "status"
        ).innerText =
        "Uploading...";

        try {

            const result =
            await uploadContract(
                file
            );

            sessionStorage.setItem(
                "analysis",
                JSON.stringify(
                    result
                )
            );

            window.location.href =
                "result.html";

        } catch (error) {

            console.error(
                error
            );

            document.getElementById(
                "status"
            ).innerText =
            "Upload Failed";
        }
    }
);