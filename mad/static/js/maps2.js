function initMap() {
  // The location of Colombo
  var colombo = { lat: 6.927079, lng: 79.861244 };

  // The map, centered at Colombo
  var map = new google.maps.Map(document.getElementById("map"), {
    zoom: 12,
    center: colombo,
    draggable:true
  });

 //adding the marker
  var marker = new google.maps.Marker({
    position: colombo,
    map: map,
    draggable:false
  });

  const drawingManager = new google.maps.drawing.DrawingManager({
    drawingMode: google.maps.drawing.OverlayType.MARKER,
    drawingControl: true,
    drawingControlOptions: {
      position: google.maps.ControlPosition.TOP_CENTER,
      drawingModes: [
        google.maps.drawing.OverlayType.MARKER,
        google.maps.drawing.OverlayType.CIRCLE,
        google.maps.drawing.OverlayType.POLYGON,
        google.maps.drawing.OverlayType.POLYLINE,
        google.maps.drawing.OverlayType.RECTANGLE,
      ],
    },
    markerOptions: {
      icon: "https://developers.google.com/maps/documentation/javascript/examples/full/images/beachflag.png",
    },
    circleOptions: {
      fillColor: "#ffff00",
      fillOpacity: 1,
      strokeWeight: 5,
      clickable: false,
      editable: true,
      zIndex: 1,
    },
  });

  drawingManager.setMap(map);

  marker.setMap(map);
}