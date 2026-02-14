const form = document.getElementById("loanForm");
const result = document.getElementById("result");

form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const formData = Object.fromEntries(new FormData(form));

    const response = await fetch("/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(formData)
    });

    const data = await response.json();

    result.classList.remove("d-none");

    document.getElementById("decision").innerText = data.decision;
    document.getElementById("probText").innerText =
        "Probability: " + data.probability;

    const bar = document.getElementById("probBar");
    bar.style.width = data.percent + "%";
    bar.innerText = data.percent + "%";

    bar.className = "progress-bar " +
        (data.percent > 40 ? "bg-danger" : "bg-success");
});
