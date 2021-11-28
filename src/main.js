const baseApiURL = "http://127.0.0.1:5000/api"
const baseForecastUrl = "http://127.0.0.1:5000/forecast"

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
    let forecastDate = new Date(document.getElementById("forecast-date").value);

    let currentDate = getRawDate(new Date());
    let upperBoundDate = getRawDate(new Date());
    upperBoundDate.setDate(upperBoundDate.getDate() + 7);

    if (forecastDate < currentDate || forecastDate > upperBoundDate) {
      alert("Invalid date input! Please enter a date input that is valid.");
      return;
    }

    let formattedForecastDate = `${forecastDate.getFullYear()}-${forecastDate.getMonth()+1}-${forecastDate.getDate()} ${forecastDate.toLocaleTimeString()}`;
    fetch(`${baseForecastUrl}?lat=${latitude}&lon=${longitude}&forecast_date=${formattedForecastDate}`).then((response) => {
        if (response.ok) {
          return response.json();
        } else {
          throw new Error('Something went wrong');
        }
      })
      .then((responseJson) => setHtmlValues(responseJson))
      .catch((error) => console.log(error));
}

function setHtmlValues(responseJson) {
    let forecastHtml = document.getElementById("forecast")
    forecastHtml.style.visibility='visible';
    console.log(responseJson);

    document.getElementById('current-value').innerHTML  = "Current value: " + `${responseJson.current_value} ${responseJson.unit}`;
    document.getElementById('radiation-label').innerHTML = "Radiation label: " + responseJson.current_report.radiation_label;
    document.getElementById('minimum-value').innerHTML = "Minimum value: " + responseJson.current_report.min_value;
    document.getElementById('maximum-value').innerHTML = "Maximum value: " + responseJson.current_report.max_value;
    document.getElementById('advice').innerHTML = responseJson.current_report.advice;
    document.getElementById('description').innerHTML = responseJson.current_report.description;
}

function getRawDate(date) {
  let rawDate = date.getFullYear()+'/'+(date.getMonth()+1)+'/'+date.getDate();
  return new Date(rawDate);
}