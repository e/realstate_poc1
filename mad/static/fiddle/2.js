/**
 * @license
 * Copyright 2019 Google LLC. All Rights Reserved.
 * SPDX-License-Identifier: Apache-2.0
 */
// This example requires the Drawing library. Include the libraries=drawing
// parameter when you first load the API. For example:
// <script src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&libraries=drawing">
function initMap() {
  const map = new google.maps.Map(document.getElementById("map"), {
    center: { lat: -34.397, lng: 150.644 },
    zoom: 8,
  });
  var lastShape;

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



  google.maps.event.addListener(drawingManager, 'overlaycomplete', function(e) {
            if (lastShape != undefined) {
                    lastShape.setMap(null);
            }

            lastShape = e.overlay;
            lastShape.type = e.type;

            // create marker
            var m1 = new google.maps.Marker({
                position: new google.maps.LatLng(-25.165, 133.769),
                map: map,
                title: 'Hello Australia!'
            });

            if (lastShape.type == google.maps.drawing.OverlayType.RECTANGLE) {

                lastBounds = lastShape.getBounds();

                document.getElementById('bounds').innerHTML = lastBounds.toString();

                // determine if marker1 is inside bounds:
                if (lastBounds.contains(m1.getPosition())) {
                     document.getElementById('inside').innerHTML = 'Yup!';
                } else {
                     document.getElementById('inside').innerHTML = 'Nope...';
                }

            } else if (lastShape.type == google.maps.drawing.OverlayType.POLYGON) {

                document.getElementById('bounds').innerHTML = 'N/A';

                // determine if marker is inside the polygon:
                // (refer to: https://developers.google.com/maps/documentation/javascript/reference#poly)
                if (google.maps.geometry.poly.containsLocation(m1.getPosition(), lastShape)) {
                     document.getElementById('inside').innerHTML = 'Yup!';
                } else {
                     document.getElementById('inside').innerHTML = 'Nope...';
                }

            }

  });




  drawingManager.setMap(map);
}

window.initMap = initMap;
