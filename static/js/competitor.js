

var competitors = []


function getCompetitor(id){
  var retval = undefined;
  for (var i = 0; i < competitors.length ;i++) {    
        if(competitors[i].id == id){
        retval =  competitors[i];
        break;
      }
    };
    return retval;
}


function random_color() {
    var letters = '0123456789ABCDEF'.split('');
    var color = '#';
    for (var i = 0; i < 6; i++ ) {
        color += letters[Math.round(Math.random()*1000000 %15)];
    }
    
    return color;
}

 shape =  {
      coord: [1, 1, 1, 20, 18, 20, 18 , 1],
      type: 'poly'
  };

function Competitor(data, position){
  
	this.color = random_color();
	this.position = position;
	this.id = data.id;
  this.nr = data.nr
  this.skipper = data.skipper
  this.current_mark = undefined;
  this.marks_rounded = []
	this.line  = undefined;
	this.path = [];
	this.symbol = {
    path: google.maps.SymbolPath.CIRCLE,
    scale: 2,
    strokeColor: this.color
  };
  this.path.push(this.position);
  
   competitors.push(this);
}

Competitor.prototype.setTargetMark = function(mark) {
  this.current_mark = mark
};

Competitor.prototype.getTargetMark = function() {
  return this.current_mark
};



distance = function(lat1, lon1, lat2, lon2) {
    
    var radlat1 = Math.PI * lat1/180
    var radlat2 = Math.PI * lat2/180
    var radlon1 = Math.PI * lon1/180
    var radlon2 = Math.PI * lon2/180
    var theta = lon1-lon2
    var radtheta = Math.PI * theta/180
    var dist = Math.sin(radlat1) * Math.sin(radlat2) + Math.cos(radlat1) * Math.cos(radlat2) * Math.cos(radtheta);
    dist = Math.acos(dist)
    dist = dist * 180/Math.PI
    dist = dist * 60 * 1.1515
    
    return dist * 0.8684 
}

Competitor.prototype.distanceToMark = function(){
  if(this.getTargetMark() == undefined)
      return -1;
  
  return distance(this.position.lat(), this.position.lng(), this.getTargetMark().lat, this.getTargetMark().lng ) 
}




Competitor.prototype.getColor = function() {
  return this.color;
};


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
  this.position = newpos;

	if(this.line === undefined){

		this.line = new google.maps.Polyline({
		    path: this.path,
		    strokeColor:  this.getColor(),
		    strokeOpacity: 1,
		    strokeWeight: 2,
        click:  function(){ alert('test')},
        shape:shape,
		    icons: [{
		      icon: this.symbol,
		      offset: '100%',
		    }],
		    map: map.map
		});
	}
  
  this.animate();	
};

Competitor.prototype.animate = function() {
	var count = 0;
    var offsetId  = 0;
    len = competitors.length;
    
    offsetId = window.setInterval(function() {
    
      count = (count + 1) ;
      if (count < 100){
      	 for (var i = 0; i < len; i++) {
          if(competitors[i].line != undefined){
            var icons = competitors[i].line.get('icons');
            icons[0].offset = '100%'
            competitors[i].line.set('icons', icons);
          }

      	};
      }
      else{
          window.clearInterval(offsetId);
      }
  }, 20);
};
