const baseApiURL = "http://localhost:5000/api/"

async function onLocationSubmit() {
    let longitude = document.getElementById("longitude");
    let latitude = document.getElementById("latitude");

    let response = await fetch(`${baseApiURL}?lat=${latitude}&lon=${longitude}`);
    let data = await response.text();
    console.log(data);
}