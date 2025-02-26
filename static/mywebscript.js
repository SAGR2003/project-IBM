let RunSentimentAnalysis = () => {
    let textToAnalyze = document.getElementById("textToAnalyze").value;

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4) {
            if (this.status == 200) {
                document.getElementById("system_response").innerHTML = xhttp.responseText;
            } else if (this.status == 400) {
                let response = JSON.parse(xhttp.responseText.replace(/'/g, '"')); // Convertir la cadena a JSON
                document.getElementById("system_response").innerHTML = response.error;
            }
        }
    };
    xhttp.open("GET", "/emotionDetector?textToAnalyze=" + textToAnalyze, true);
    xhttp.send();
}
