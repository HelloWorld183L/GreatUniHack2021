const baseApiURL = "http://127.0.0.1:5000/api"

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

    fetch(`${baseApiURL}?lat=${latitude}&lon=${longitude}`).then((response) => {
        if (response.ok) {
          return response.json();
        } else {
          throw new Error('Something went wrong');
        }
      })
      .then((responseJson) => {
        let forecastHtml = document.getElementById("forecast")
        forecastHtml.style.visibility='visible';

        console.log(responseJson);
        document.getElementById('current-value').innerHTML = "Current value: " + `${responseJson.current_value} ${responseJson.unit}`;
        document.getElementById('radiation-label').innerHTML = "Radiation label: " + responseJson.current_report.radiation_label;
        document.getElementById('minimum-value').innerHTML = "Minimum value: " + responseJson.current_report.min_value;
        document.getElementById('maximum-value').innerHTML = "Maximum value: " + responseJson.current_report.max_value;
        document.getElementById('advice').innerHTML = responseJson.current_report.advice;
        document.getElementById('description').innerHTML = responseJson.current_report.description;
      })
      .catch((error) => {
        console.log(error)
      });
}

// Little function just to check how the forecast looks...
function testFunction() {
    let forecastHtml = document.getElementById("forecast")
    forecastHtml.style.visibility='visible';
}