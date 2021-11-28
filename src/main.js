const baseApiURL = "http://localhost:5000/api/"

function setUserLocation() {
    var geoSuccess = function(position) {
        document.getElementById('latitude').value = position.coords.latitude;
        document.getElementById('longitude').value = position.coords.longitude;
    };
    navigator.geolocation.getCurrentPosition(geoSuccess);
};

async function onLocationSubmit() {
    let longitude = document.getElementById("longitude").value;
    let latitude = document.getElementById("latitude").value;

    let response = await fetch(`${baseApiURL}?lat=${latitude}&lon=${longitude}`);
    let data = await response.json();
    let parsedData = JSON.parse(data);

    let forecastHtml = document.getElementById("forecast")
    forecastHtml.style.visibility='visible';
    
    document.getElementById('current-value').innerHTML = "Current value: " + parsedData.current_value;
    document.getElementById('radiation-label').innerHTML = "Radiation label: " + parsedData.forecast_report.radiation_label;
    document.getElementById('minimum-value').innerHTML = "Minimum value: " + parsedData.forecast_report.min_value;
    document.getElementById('maximum-value').innerHTML = "Maximum value: " + parsedData.forecast_report.max_value;
    document.getElementById('advice').innerHTML = parsedData.forecast_report.advice;
    document.getElementById('description').innerHTML = parsedData.forecast_report.description;
}

// Little function just to check how the forecast looks...
function testFunction() {
    let forecastHtml = document.getElementById("forecast")
    forecastHtml.style.visibility='visible';
}