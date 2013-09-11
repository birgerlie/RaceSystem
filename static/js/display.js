
			
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
	console.log(data)
	if ($('#display').has("#" + data.id).length == 0)	{
		var competitor_id = data.id;
		$('#display').append(
			'<tr id='+ data.id +'>' +
				'<td ><a  onclick=senterMap(' + competitor_id   + ') >'+ data.id +' </a></td>' +
				'<td >' + data.nr +     '</td>'			+	
				'<td class="speed"></td>'			+	
				'<td class="hdg"></td>'			+	
			'</tr>' );
	}

	if ($('#display ' + data.id + ' .color').length == 0)	{
			competitor = getCompetitor(data.id);
			if(competitor != undefined){
				$('#display #' + data.id).css('text', competitor.getColor() )
			}
	}

	$( '#' + data.id + ' .speed').text(data.speed + ' knots');
	$( '#' + data.id + ' .hdg').text( data.hdg + ' deg');
}

