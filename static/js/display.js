
			
function num(n){
	var num =  String(n).split('.')
	console.log(num)
	dec = num[1].substr(0,1)


	v = num[0]

	return v + '.' + dec;

}

function display_info(data){
	// console.log(data)
	
	if ($('#display').has("#" + data.id).length == 0)	{
		$('#display').append('<div class="well coolbox" id='+data.id +'><table style="width:100%"><tbody><tr class="lead"><td ><h4>'+data.id+'</h4></td><td class="speed"></td><td class="hdg"></td> <td > </td></tr></tbody></table></div>');
	}

	$( '#' + data.id + ' .speed').text(num(data.speed) + ' knots');
	$( '#' + data.id + ' .hdg').text(num(data.hdg) + ' deg');

	console.log('')
}

