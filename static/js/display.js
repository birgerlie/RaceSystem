
			
function num(n){
	var num =  String(n).split('.')
	dec = num[1].substr(0,1)

	v = num[0]

	return v + '.' + dec;
}


comp = undefined
function senterMap(c){
	
	competitor = getCompetitor(c.id)
	comp = competitor
	if(competitor != undefined){
		// alert('set map pos ' + c.id)	
		map.map.panTo(competitor.position);
	}

	
}

function display_info(data){
	// console.log(data)
	
	if ($('#display').has("#" + data.id).length == 0)	{

		var competitor_id =data.id;
		$('#display').append('<div class="well coolbox" id='+data.id +'><a  onclick=senterMap(' + competitor_id   + ') ><table style="width:100%"><tbody>' +
			'<tr ><td class="foo" ><div class="icon-move"></div> </td>  <td ><h4>'+data.id+'</h4></td><td class="speed number"></td><td class="hdg number"></td> <td > </td></tr></tbody></table></a></div>');
	}

	if ($('#display ' + data.id + ' .color').length == 0)	{
			competitor = getCompetitor(data.id);
			if(competitor != undefined){
				$('#display #' + data.id).css('border-color', competitor.getColor() )

			}
			
	}


	


	$( '#' + data.id + ' .speed').text(num(data.speed) + ' knots');
	$( '#' + data.id + ' .hdg').text(num(data.hdg) + ' deg');


}

