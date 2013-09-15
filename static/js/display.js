
			
function num(n){

	if(String(n).indexof(".") > 0){
			var num =  String(n).split('.')
			dec = num[1].substr(0,1)
			v = num[0]
			return v + '.' + dec;		
	}
	
	return n
}

function senterMap(c){
	competitor = getCompetitor(c.id)
	if(competitor != undefined){
		map.map.panTo(competitor.position);
	}
}

function display_info(data){
	// console.log(data)
	

	if ($('#display').has("#" + data.id).length == 0)	{
	
		$('#display').append(
			'<tr id='+ data.id +'>' +
				'<td ><a class="btn" onclick=senterMap(' + data.id   + ') >'+ data.yacht +' </a></td>' +
				'<td >' + data.nr +     '</td>'			+	
				'<td class="speed"></td>'			+	
				'<td class="hdg"></td>'			+	
				'<td class="mrk"></td>'			+	
			'</tr>' );
	}

	if ($('#display ' + data.id + ' .color').length == 0)	{
			competitor = getCompetitor(data.id);

			if(competitor != undefined){
				$('#' + data.id  ).css('background', competitor.getColor() )
			}
	}

	$( '#' + data.id + ' .speed').text(data.speed + ' knots');
	$( '#' + data.id + ' .hdg').text( data.hdg + ' deg');
	$( '#' + data.id + ' .mrk').text( data.distanceToMark + ' Nm');
}

