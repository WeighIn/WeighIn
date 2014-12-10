var ctx;
var i = 0; //counter for image array[]
var gameCount = 0; //count for number of plays
var stage = 0; // 0-starting screen 1-image tagging 2-major association 3-next game (?)
var colorChoice =  (Math.random() * 6)|0; //determines which pallette

var imgArray = new Array();
imgArray = ["images/gabebob.jpg", "images/gabebob1.jpg", "images/gabebob2.jpg", "images/gabebob3.jpg", "images/gabebob4.jpg", "images/gabebob5.jpg"]; //eventually get from backend

var majorArray = new Array();
majorArray = ["Computer Science", "English", "Pre-Med"]; //eventually get from backend from a queue (?)

var attributes = new Array();
attributes = ["Brunette", "Blonde", "Ginger"];            //eventually get from backend from a queue (?)

var color = new Array(5); //array of arrays of different color pallets
for(var j=0; j<10; j++){
    color[i]= new Array(3);
}
color[0] = ["#92B2BD", "#BECCBF", "#E0DCB6"]; // SUN'S GENTLE RAYS
color[1] = ["#FFBE5C", "#FE9F4A", "#FE4A4A"]; //NOVEMBER LEAVES
color[2] = ["#65DBB9", "#1FABA8", "#006661"]; //TEAL AND GOLD
color[3] = ["#B27FCE", "#D679B2", "#EAB2CD"]; //PURPLE
color[4] = ["#02BE89", "#1FF8AC", "#A7DA5C"]; //GREEN
color[5] = ["#93A3B0", "#121631", "#555A6D"]; //GRAYS
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

    if(stage==0 && (x>=500/3 && x<=1000/3) && (y>=350 && y<=400)){
        stage=1;
    }

    if(y >= 450 && (stage==2 || stage==1)) //if one of the buttons was clicked
    {
        colorChoice = (Math.random() * 6)|0; //picks a pallete
        gameCount++;
    	var resultArray = new Array(); //index 0 is image, index 1 is the user's choice
        if(stage == 1){
            resultArray[0] = attributes[i];
        }
    	resultArray[0] = imgArray[i]; // ^^^^^^^^^^^^^^^^^
    	clearCanvas(canvas); //clears the canvas to prevent using too much memory

    	
    	
    	if(i==imgArray.length - 1) //resets image loop if past the last image
    		i=0;
    	else
    		i++;
        if(stage==2){
    	
        	if(x <= 500/3) { //button 1 was clicked
        		resultArray[1] = majorArray[0];
        	}
        	else if((x > 500/3) && (x <= 1000/3)) { //button 2 was clicked
        		resultArray[1] = majorArray[1];
            }
        	else if((x >= 1000/3) && (x <= 500)) {//button 3 was clicked
        		resultArray[1] = majorArray[2];
            }
        }
        if(stage==1) {
             if(x <= 500/3) { //button 1 was clicked
                resultArray[1] = attributes[0];
            }
            else if((x > 500/3) && (x <= 1000/3)) { //button 2 was clicked
                resultArray[1] = attributes[1];
            }
            else if((x >= 1000/3) && (x <= 500)) {//button 3 was clicked
                resultArray[1] = attributes[2];
            }
        }
        if(gameCount==5 && stage == 1) { //transition to stage 2
            stage=2;
            gameCount=0;
        }
        if(gameCount==20 && stage == 2) { //transition to stage 3
            //stage = 3;
            gameCount=0;
        }
    	
    	console.log(resultArray); //replace with "send" resultArray
    } 

	
  
  }

$(document).ready(function(){
	//Canvas stuff
	var canvas = $("#canvas")[0];
	ctx = canvas.getContext("2d");
	var w = $("#canvas").width();
	var h = $("#canvas").height();

	


	function init()
	{
		//every 90ms
		if(typeof game_loop != "undefined") clearInterval(game_loop);
		game_loop = setInterval(paint, 90);
	}
	
	init();

	function paintClickBox(x,y,width,height, color){
        ctx.fillStyle = color;
        ctx.fillRect(x,y,width,height);
    }

    function paintButtonText(text,x,y,color){
        ctx.fillStyle=color;
        ctx.font="20px Lato";
        ctx.textAlign = "center";
        ctx.fillText(text,x,y,450/3); //(text,x,y,maxWidth)
    }

	function paint()
	{
        if(stage == 0) //welcome screen
        { //clear canvas to avoid filling memory
            ctx.clearRect(0, 0, ctx.canvas.width, ctx.canvas.height);
            var image = new Image();
            ctx.drawImage(image,0,0);
            ctx.fillStyle="#000000";
            ctx.font="100px Lato";
            ctx.textAlign = "center";
            ctx.fillText("Welcome",250,250,300); //(text,x,y,maxWidth)
            paintClickBox(500/3,350,500/3,50, "#999999");
            ctx.strokeStyle="#000000";
            ctx.strokeRect(500/3,350,500/3,50);
            paintButtonText("START",1500/6,380,"#000000");

        }
        if(stage == 1)
        {
            ctx.clearRect(0, 0, ctx.canvas.width, ctx.canvas.height); //clear canvas to avoid filling memory

            var image = new Image();
            image.src = imgArray[i];
            //drawing a bunch of stuff
             ctx.drawImage(image,0,0);
            
            paintClickBox(0,450,500/3,50,color[colorChoice][0]);                        //box 1
            paintButtonText(attributes[0],500/6,480,"#FFFFFF");

            paintClickBox(500/3,450,500/3,50,color[colorChoice][1]);                    //box 2
            paintButtonText(attributes[1],1500/6,480,"#FFFFFF");

            paintClickBox(1000/3,450,500/3,50,color[colorChoice][2]);                   //box 3
            paintButtonText(attributes[2],2500/6,480,"#FFFFFF");

            //add top bar that shows progress for each stage (5 for stage 1 and 20 for stage 2)

            ctx.fillStyle="#BBBBBB";
            ctx.fillRect(0, 0, 500, 40);
            ctx.strokeStyle="#000000";
            ctx.strokeRect(0, 0, 500, 40);
            ctx.fillStyle="#1FC3AD";
            ctx.fillRect(0, 0, gameCount*100, 40);
        }
		if(stage == 2) 
		{
		    ctx.clearRect(0, 0, ctx.canvas.width, ctx.canvas.height); //clear canvas to avoid filling memory

			var image = new Image();
			image.src = imgArray[i];
			//drawing a bunch of stuff
			 ctx.drawImage(image,0,0);

            paintClickBox(0,450,500/3,50,color[colorChoice][0]);                        //box 1
            paintButtonText(majorArray[0],500/6,480,"#FFFFFF");

            paintClickBox(500/3,450,500/3,50,color[colorChoice][1]);                    //box 2
            paintButtonText(majorArray[1],1500/6,480,"#FFFFFF");

            paintClickBox(1000/3,450,500/3,50,color[colorChoice][2]);                   //box 3
            paintButtonText(majorArray[2],2500/6,480,"#FFFFFF");

			//add top bar that shows progress for each stage (5 for stage 1 and 20 for stage 2)

            ctx.fillStyle="#BBBBBB";
            ctx.fillRect(0, 0, 500, 40);
            ctx.strokeStyle="#000000";
            ctx.strokeRect(0, 0, 500, 40);
            ctx.fillStyle="#1FC3AD";
            ctx.fillRect(0, 0, gameCount*25, 40);
		}





	}
	
})