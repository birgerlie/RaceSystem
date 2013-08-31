
			
function num(n){
	var num =  String(n).split('.')
	dec = num[1].substr(0,1)

	v = num[0]

	return v + '.' + dec;
}

function senterMap(c){
	competitor = getCompetitor(c.id)
	if(competitor != undefined){
		map.map.panTo(competitor.position);
	}
}

function display_info(data){
	
	if ($('#display').has("#" + data.id).length == 0)	{
		var competitor_id = data.id;
		$('#display').append(
			'<tr id='+ data.id +'>' +
				'<td ><a  onclick=senterMap(' + competitor_id   + ') >'+ data.id +' </a></td>' +
				'<td >' + data.nr +     '</td>'			+	
				'<td class="speed">bar1</td>'			+	
				'<td class="hdg"></td>'			+	
			'</tr>' );
	}

	if ($('#display ' + data.id + ' .color').length == 0)	{
			competitor = getCompetitor(data.id);
			if(competitor != undefined){
				$('#display #' + data.id).css('text', competitor.getColor() )
			}
	}

	$( '#' + data.id + ' .speed').text(num(data.speed) + ' knots');
	$( '#' + data.id + ' .hdg').text(num(data.hdg) + ' deg');
}

