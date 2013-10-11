var sock;

function socketConnection(){

	sock = new WebSocket("ws://" + server_address + "/sock");
	
	sock.onopen = function(){ console.log("Connected websocket"); };
	sock.onerror = function(e){ console.log("Websocket error " + e); };
	sock.onmessage = function(evt){
	    var data = JSON.parse(evt.data);
	   	var min_dist = 0.5

	    if(raceId === data.race){

		//console.log(data);
		display_info(data);	
		
		pos = new google.maps.LatLng(data.lat, data.lng)
		exist = false;

		for (var i = 0; i < competitors.length ;i++) {		
			if(competitors[i].id === data.id){
				competitor = competitors[i]

				competitor.setPosition(pos);	
				exist = true;
				
				if(competitor.getTargetMark() == undefined){
					competitor.setTargetMark(marks[0])
					competitor.mark_index = 0
				}
				else{
				
					distanceToMark = competitor.distanceToMark()
					data.distanceToMark = distanceToMark;
					console.log(competitor.current_mark);
					if( distanceToMark < min_dist) //we assume mark rounding when we are closer than 10 meters
					{	
						competitor.mark_index +=1
						competitor.setTargetMark(marks[competitor.mark_index % marks.length])
						data.mark = competitor.getTargetMark().name;
					}
				}
				data.mark = competitor.getTargetMark().name;
				display_info(data);					
			}
		};

		if (!exist && competitors.length < 30000){
			new Competitor(data, pos);
		}
	}
	}	
}
