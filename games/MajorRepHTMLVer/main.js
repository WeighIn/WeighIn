
function getInput() {
    var sampleAInput = [["Computer Science","English", "Dance"],["Electrical Engineering","Animal Science", "History"],["Anthropology","Pre-Med", "Astronomy"]];
    return sampleAInput;
}

function getRandColors() {
    var color = new Array(5); //array of arrays of different color pallets
    for(var j=0; j<10; j++){
        color[j]= new Array(3);
    }
    color[0] = ["#92B2BD", "#BECCBF", "#E0DCB6"]; // SUN'S GENTLE RAYS
    color[1] = ["#FFBE5C", "#FE9F4A", "#FE4A4A"]; //NOVEMBER LEAVES
    color[2] = ["#65DBB9", "#1FABA8", "#006661"]; //TEAL AND GOLD
    color[3] = ["#B27FCE", "#D679B2", "#EAB2CD"]; //PURPLE
    color[4] = ["#02BE89", "#1FF8AC", "#A7DA5C"]; //GREEN
    color[5] = ["#93A3B0", "#121631", "#555A6D"]; //GRAYS

    var colorChoice = (Math.random() * 6)|0;
    return color[colorChoice];
}

function getRandImg() {
    var imgArray = new Array();
    imgArray = ["images/gabebob.jpg", "images/gabebob1.jpg", "images/gabebob2.jpg", "images/gabebob3.jpg", "images/gabebob4.jpg", "images/gabebob5.jpg"]; //eventually get from backend
    var imgChoice = (Math.random() * 6)|0;
    return imgArray[imgChoice];

}


function processInput(inputArray) {
    return inputArray;
}

function getNextTuple(i, inputArray) {
    return inputArray[i];
}

function displayTuple(ith, colorArray) {
    $('.option1 p').text(ith[0]);
    $('.option1').css("background-color", colorArray[0]);
    $('.option2 p').text(ith[1]);
    $('.option2').css("background-color", colorArray[1]);
    $('.option3 p').text(ith[2]);
    $('.option3').css("background-color", colorArray[2]);
}
function getTextFromOption(adiv) {
    return $(adiv).find('p').text();
}
function getThisImage() {
    return $('.img').attr("src");
}


$(document).ready(function() {

    var arr = processInput(getInput());
    var i = 0; // for majors
    var ith = getNextTuple(i,arr);
    var colorArray = getRandColors();
    
    displayTuple(ith, colorArray);

   var output = [];
   var choice;
   var image;
    $('.option1').click(function() {
        choice = getTextFromOption(this);
        image = getThisImage();
        output.push([image, choice]);              
        console.log(output);
        if (i == arr.length - 1)
            i = 0;
        if (i < arr.length - 1) {
            displayTuple(getNextTuple(++i,arr), getRandColors());
            $('.img').attr("src",getRandImg())
        }
    });
    $('.option2').click(function() {
        choice = getTextFromOption(this);
        image = getThisImage();
        output.push([image, choice]);              
        console.log(output);            
        if (i == arr.length - 1)
            i = 0;
        if (i < arr.length -1 ) {
            displayTuple(getNextTuple(++i,arr), getRandColors());
            $('.img').attr("src",getRandImg())
        } 

    });
    $('.option3').click(function() {
        choice = getTextFromOption(this);
        image = getThisImage();
        output.push([image, choice]);              
        console.log(output);
        if (i == arr.length - 1)
            i = 0;
        if (i < arr.length -1 ) {
            displayTuple(getNextTuple(++i,arr), getRandColors());
            $('.img').attr("src",getRandImg())
        } 
    });



});