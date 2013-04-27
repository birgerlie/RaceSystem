

var competitors = []

function Competitor(id, position, color){
	if(color === undefined){
		color = function() {
    var letters = '0123456789ABCDEF'.split('');
    var color = '#';
    for (var i = 0; i < 6; i++ ) {
        color += letters[Math.round(Math.random() * competitors.length)];
    }
    return color;
}
	}

	this.position=position;
	this.id = id;
	this.color = color;
	this.line  = undefined;
	this.path = [];
	this.symbol = {
    path: google.maps.SymbolPath.CIRCLE,
    scale: 8,
    strokeColor: this.color   
  };
  this.path.push(this.position);
  
   competitors.push(this);
  // competitors[this.id] = this
  // console.log(competitors)
}

Competitor.prototype.toString = function() {
	return (this.id + ' ' + this.color);
};

Competitor.prototype.setSymbol = function(symbol) {
	this.symbol = symbol;
};

Competitor.prototype.getSymbol = function() {
	return this.symbol;
};

Competitor.prototype.setPosition = function(newpos) {
	
	this.path.push(newpos)

	if(this.line === undefined){

		this.line = new google.maps.Polyline({
		    path: this.path,
		    strokeColor: "#F4B741",
		    strokeOpacity: 0.5,
		    strokeWeight: 2,
		    icons: [{
		      icon: this.symbol,
		      offset: '100%'
		    }],
		    map: map.map
		});
	}
  
  // mLat = 0
  // mLng = 0
  
  // for (var i = 0; i < competitors.length; i++) {
  // 	if(competitors[i].position)
  // }

  this.animate();	

};

Competitor.prototype.animate = function() {
	var count = 0;
    var offsetId  = 0;
    
    offsetId = window.setInterval(function() {
    
      count = (count + 1) ;
      if (count < 100){
      	
      	for (var i = 0; i < competitors.length; i++) {
      		var icons = competitors[i].line.get('icons');
      		icons[0].offset = '100%' //(count / 2) + '%';		
      		competitors[i].line.set('icons', icons);

      	};
       // this.line.set('icons', icons);
      }
      else{
          window.clearInterval(offsetId);
      }
  }, 20);
};
