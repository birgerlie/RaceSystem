

route = []

function addMark(id){
		var marker = new google.maps.Marker({
    	position: map.getCenter(),
    	map: map.map,
    	draggable: true,
    	title:'FooBar'

  	});

	if(id=='start'){
		marker.title= 'Start'
	}
	else if(id =='end'){
		console.log('end')
		marker.title= 'End'
	}
	else{
		console.log('other')
		marker.title= 'Marker ' + route.length
	}
	
	route.push(marker)
}