
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
    strokeColor: '#ffee10',
    strokeOpacity: 1.0,
    strokeWeight: 2,
    clickable:false,
    editable:true,
    geodesic:true,
    icons: [{
    icon: lineSymbol,
    // offset: '100%'
  	}],
  }
  this.opts = opts;
  this.lastLatLng = undefined;
  this.line = new google.maps.Polyline(polyOptions);
  this.line.setMap(this.map);
  this.length = 0;

  google.maps.event.addListener(this.line.getPath() , 'insert_at', bind( this.pathChangeHandler, this ) );
  google.maps.event.addListener(this.line.getPath() , 'remove_at', bind( this.pathChangeHandler, this ));
  google.maps.event.addListener(this.line.getPath() , 'set_at', bind( this.pathChangeHandler, this ));
  
 	}

	RouteManager.prototype.pathChangeHandler = function(event) {
		if(typeof this.onRouteChange === 'function'){
			setTimeout(this.onRouteChange, 1);
		}
	};

	RouteManager.prototype.onRouteChange = function(first_argument) {
		
	};

	RouteManager.prototype.addWayPoint = function(latLng) {
		path = this.line.getPath();
		path.push(latLng);
  		this.lastLatLng = latLng
	}; 	

	RouteManager.prototype.onMapClick = function(event) {
		this.addWayPoint(event.latLng);
	};

	RouteManager.prototype.drawEnable = function() {
		this.mapClickHandler = google.maps.event.addListener( this.map, 'click', bind( this.onMapClick, this ) );
		// this.mapMouseMoveHandler = google.maps.event.addListener( this.map, 'mousemove', bind( this.onMapMouseMove, this ) );
	};


	RouteManager.prototype.drawDisable = function() {
		google.maps.event.removeListener(this.mapClickHandler);
		google.maps.event.removeListener(this.mapMouseMoveHandler);
	};

	RouteManager.prototype.onMapMouseMove = function(event) {
		this.updateDrawingLine(this.lastLatLng , event.latLng);
	};

	RouteManager.prototype.updateDrawingLine = function(start, end) {
		if(start && end){
			// this.drawingLine.setPath([start, end])
		}
	};

	RouteManager.prototype.createRoute = function(){
		return WayPoint.createRoute(this.line.getPath())
	};

	function WayPoint(){
		this.latLng = undefined;
		this.bearing = 0.0;
		this.distance = 0.0;
		this.name = '-';
		this.index = -1




		this.toString = function(){
			return this.name + ' hdg:'  + num(this.bearing) + ', ' + num((this.distance/1000) / 0.539957 ,0) + 'nm, lat:' + num(this.latLng.lat(),2) + ' lng:' + num(this.latLng.lng(),2);
		}
	}

	function num(n, decimal_count){
		if(decimal_count == undefined){decimal_count = 1}
		if(n === undefined || n == 0.0){
			return 0;
		}
		
		var num =  String(n).split('.')
		if(decimal_count == 0){
			return num[0];
		}
		dec = num[1].substr(0,decimal_count)
		
		v = num[0]
		
	return v + '.' + dec;
}

	WayPoint.createRoute = function(points) {
		waypoints = []
		waypoints.distance = 0

		if (points.length == 0)
			return waypoints 

		wp = new WayPoint()
		wp.latLng = points.getAt(0)
		wp.name =  'Mark 1'
		wp.index = 0
		waypoints.push(wp)		
		distance = 0;

		for (var i = 1; i < points.length; i++) {
				start = points.getAt(i-1)
				end = points.getAt(i)
				wp = new WayPoint()
				wp.latLng = end
				wp.name =  'Mark ' + (i + 1).toString()
				wp.index = i
				wp.bearing =google.maps.geometry.spherical.computeHeading(start, end);
				if(wp.bearing < 0){wp.bearing+=360}
				wp.distance= google.maps.geometry.spherical.computeDistanceBetween(start,end);
				waypoints.push(wp)
				distance += wp.distance;
			};		
			waypoints.distance = distance;
			waypoints[waypoints.length -1].name  = 'Finish'
			return waypoints
	};


