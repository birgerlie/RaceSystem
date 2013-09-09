var sock;

function socketConnection(){
	sock = new WebSocket("ws://../sock");

	 sock = new WebSocket("ws://ec2-50-112-26-56.us-west-2.compute.amazonaws.com:8080/sock");
	 //sock = new WebSocket("ws://localhost:8080/sock");
	
	sock.onopen = function(){ console.log("Connected websocket"); };
	sock.onerror = function(){ console.log("Websocket error"); };
	sock.onmessage = function(evt){
	    var data = JSON.parse(evt.data);
		console.log(data);
		display_info(data);	
		
		pos = new google.maps.LatLng(data.lat, data.lng)
		exist = false;

		for (var i = 0; i < competitors.length ;i++) {		
			if(competitors[i].id === data.id){
				competitors[i].setPosition(pos);	
			}
		};

		if (!exist && competitors.length < 3){
			new Competitor(data, pos);
		
		}
	}	
}
