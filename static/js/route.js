
function bind( func, context ) {
	return function() {
		return func.apply( context, arguments );
	};
}

var lineSymbol = {
  path: google.maps.SymbolPath.FORWARD_CLOSED_ARROW
};

function RouteManager(opts){

	this.map = opts.map;
	var polyOptions = {
    strokeColor: '#ff0000',
    strokeOpacity: 1.0,
    strokeWeight: 3,
    icons: [{
    icon: lineSymbol,
    // offset: '100%'
  	}],
  }
  this.line = new google.maps.Polyline(polyOptions);
  this.line.setMap(this.map);

}		

	RouteManager.prototype.addWayPoint = function(latLng) {
		path = this.line.getPath();
		path.push(latLng);

		var marker = new google.maps.Marker({
    	position: event.latLng,
    	title: '#' + path.getLength(),
    	map: this.map
  		});
	};


	RouteManager.prototype.editEnable = function() {
		console.log('editEnable');
	};

	RouteManager.prototype.editDisable = function() {
		console.log('editDisable');
	};

	RouteManager.prototype.onMapClick = function(event) {
		this.addWayPoint(event.latLng);

		console.log(this);
	};

	RouteManager.prototype.drawEnable = function() {
		this.mapClickHandler = google.maps.event.addListener( this.map, 'click', bind( this.onMapClick, this ) );
		this.mapMouseMoveHandler = google.maps.event.addListener( this.map, 'mousemove', bind( this.onMapMouseMove, this ) );
	};


	RouteManager.prototype.drawDisable = function() {
		google.maps.event.removeListener(this.mapClickHandler);
		google.maps.event.removeListener(this.mapMouseMoveHandler);
	};

	RouteManager.prototype.onMapMouseMove = function(event) {
		
	};

Array.prototype.insertAt = function (index, item) {
  this.splice(index, 0, item);
};

