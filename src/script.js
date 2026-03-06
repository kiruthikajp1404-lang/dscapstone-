async function generatePrediction() {

    try {

        const title = document.getElementById("title").value;
        const author = document.getElementById("author").value;
        const ratingsCount = parseFloat(document.getElementById("ratingsCount").value);
        const averageRating = parseFloat(document.getElementById("averageRating").value);

        // Print title & author immediately
        document.getElementById("resultTitle").innerText = title;
        document.getElementById("resultAuthor").innerText = author;

        const response = await fetch("http://127.0.0.1:8000/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                RatingsCount: ratingsCount,
                AverageRating: averageRating
            })
        });

        const data = await response.json();

        if (data.prediction) {
            document.getElementById("prediction").innerText =
                data.prediction[0].toFixed(2);
        } else {
            document.getElementById("prediction").innerText =
                "Error: " + JSON.stringify(data);
        }

    } catch (error) {
        document.getElementById("prediction").innerText =
            "Server not connected!";
    }
}