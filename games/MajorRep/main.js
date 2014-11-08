var ctx;
var i = 0; //counter for image array[]
var count = 0; //count for number of plays



var imgArray = new Array();
imgArray = ["gabebob.jpg", "gabebob1.jpg", "gabebob2.jpg", "gabebob3.jpg", "gabebob4.jpg", "gabebob5.jpg"]; //eventually get from backend

var majorArray = new Array();
majorArray = ["Computer Science", "English", "Pre-Med"]; //eventually get from backend from a queue (?)

var attributes = new Array();
attributes = ["Brunette", "Blonde", "Ginger"];

canvas.addEventListener("mousedown", getPosition, false);

function Timer(settings)
{
    this.settings = settings;
    this.timer = null;
 
    this.fps = settings.fps || 30;
    this.interval = Math.floor(1000/30);
    this.timeInit = null;
         
    return this;
}
 
Timer.prototype = 
{   
    run: function()
    {
        var $this = this;
         
        this.settings.run();
        this.timeInit += this.interval;
 
        this.timer = setTimeout(
            function(){$this.run()}, 
            this.timeInit - (new Date).getTime()
        );
    },
     
    start: function()
    {
        if(this.timer == null)
        {
            this.timeInit = (new Date).getTime();
            this.run();
        }
    },
     
    stop: function() 
    {
        clearTimeout(this.timer);
        this.timer = null;
    }
}


function clearCanvas(cnv) {
  var ctx = cnv.getContext('2d');     // gets reference to canvas context
  ctx.beginPath();    // clear existing drawing paths
  ctx.save();         // store the current transformation matrix

  // Use the identity matrix while clearing the canvas
  ctx.setTransform(1, 0, 0, 1, 0, 0);
  ctx.clearRect(0, 0, cnv.width, cnv.height);

  ctx.restore();        // restore the transform
}

function getPosition(event)
  {
    
    var x = new Number();
    var y = new Number();
    var canvas = document.getElementById("canvas");

    if (event.x != undefined && event.y != undefined)
    {
      x = event.x;
      y = event.y;
    }
    else 
    {
      x = event.clientX + document.body.scrollLeft +
          document.documentElement.scrollLeft;
      y = event.clientY + document.body.scrollTop +
          document.documentElement.scrollTop;
    }

    x-=canvas.offsetLeft;
    y-=canvas.offsetTop;

    if(y >= 450) //if one of the buttons was clicked
    {
    	var resultArray = new Array(); //index 0 is image, index 1 is the user's choice
    	resultArray[0] = imgArray[i]; // ^^^^^^^^^^^^^^^^^
    	clearCanvas(canvas); //clears the canvas to prevent using too much memory
    	
    	
    	if(i==imgArray.length - 1) //resets image loop if past the last image
    		i=0;
    	else
    		i++;

    	
    	if(x <= 500/3) //button 1 was clicked
    		resultArray[1] = majorArray[0];
    		
    	else if((x > 500/3) && (x <= 1000/3)) //button 2 was clicked
    		resultArray[1] = majorArray[1];
    	else if((x >= 1000/3) && (x <= 500)) //button 3 was clicked
    		resultArray[1] = majorArray[2];
    	
    	console.log(resultArray); //replace with "send" resultArray
    } 

	
  
  }

$(document).ready(function(){
	//Canvas stuff
	var canvas = $("#canvas")[0];
	ctx = canvas.getContext("2d");
	var w = $("#canvas").width();
	var h = $("#canvas").height();

	var stage = 2;
	
	function amountTime() 
	{
		var timeNow = Date.now() - timeSinceStart;
		console.log(timeNow);
	}

	function init()
	{
		//every 90ms
		if(typeof game_loop != "undefined") clearInterval(game_loop);
		game_loop = setInterval(paint, 90);

		var timerLoop = window.setInterval(amountTime(), 100);

	}
	
	init();

	

	function paint()
	{
		if(stage == 2) 
		{
		    ctx.clearRect(0, 0, ctx.canvas.width, ctx.canvas.height); //clear canvas to avoid filling memory

			var image = new Image();
			image.src = imgArray[i];
			//drawing a bunch of stuff
			ctx.drawImage(image,0,0);
			ctx.fillStyle="#FF0000";
			ctx.fillRect(0, 450, 500/3, 50);
			ctx.fillStyle="#FFFFFF";
			ctx.font="20px Lato";
			ctx.textAlign="center";
			ctx.fillText(majorArray[0],500/6,480, 450/3);
			ctx.fillStyle="#00ff00";
			ctx.fillRect(500/3, 450, 500/3, 50);
			ctx.fillStyle="#FFFFFF";
			ctx.font="20px Lato";
			ctx.textAlign="center";
			ctx.fillText(majorArray[1],1500/6,480, 450/3);
			ctx.fillStyle="#0000FF";
			ctx.fillRect(1000/3, 450, 500/3, 50);
			ctx.fillStyle="#FFFFFF";
			ctx.font="20px Lato";
			ctx.textAlign="center";
			ctx.fillText(majorArray[2],2500/6,480, 450/3);

			//add top bar that shows progress for each stage (5 for stage 1 and 20 for stage 2)
		}




	}
	
})