// Loads the Google Map onto profile
function profileMap() {
  let mapProp = { // map view begins zoomed out
    center: new google.maps.LatLng(0, 0),
    zoom: 1,
  };
  let map = new google.maps.Map(document.getElementById("googleMap"), mapProp);
  for (let i = 0; i < countries.length; i++) { 
    let marker = new google.maps.Marker({ // add a marker for each country visited, based on capital coordinates
        position: new google.maps.LatLng(countries[i].lat, countries[i].long),
        map: map,
    });
  }
}