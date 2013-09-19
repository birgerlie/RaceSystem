
var index = 0;
var initialColor = '#0000ff';
var route;
function initialize(){
	// var path = new google.maps.MVCArray();
			var polyOptions = {
			  strokeColor: initialColor,
			  strokeOpacity: 0.6,
			  strokeWeight: 3,
			  clickable: true,
			  geodesic: false,
			  map: map.map
			}
		

			
		route = new RouteManager(polyOptions);
		route.drawEnable();
	}
