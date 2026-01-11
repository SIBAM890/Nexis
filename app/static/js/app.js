scanForm.addEventListener("submit", async (e) => {
    e.preventDefault();

    const query = document.getElementById("username").value.trim();
    const imageFile = document.getElementById("image").files[0];

    const formData = new FormData();
    if (query) formData.append("query", query);
    if (imageFile) formData.append("image", imageFile);

    const response = await fetch("/scan", {
        method: "POST",
        body: formData
    });

    const data = await response.json();

    output.textContent = JSON.stringify(
        data.intelligence,
        null,
        2
    );

    let maxRisk = 0;
    Object.values(data.intelligence.risk_overview || {}).forEach(r => {
        maxRisk = Math.max(maxRisk, r.score || 0);
    });

    riskBar.style.width = `${Math.min(maxRisk * 10, 100)}%`;

    riskText.textContent =
        maxRisk >= 8 ? "CRITICAL" :
        maxRisk >= 6 ? "HIGH" :
        maxRisk >= 4 ? "MODERATE" : "LOW";

    timeline.textContent = JSON.stringify(
        data.intelligence.timeline,
        null,
        2
    );
});