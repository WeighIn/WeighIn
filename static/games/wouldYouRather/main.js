/**
 * Created by HarshayShah on 08/11/14.
 */

//allcolors = [#00008b,#654321,#5d3954,#a40000,#08457e,#cd5b45,#008b8b,#dc143c,#013220,#734f96,#3c1414,#9400d3];
allcolors = ['red','blue','BlueViolet','Brown','DarkBlue','DarkCyan','Crimson','DarkSlateGray'];

function getRandomColor() {
    return allcolors[parseInt(Math.random()*allcolors.length,10)];
}

function getInput() {
    var sampleAInput = [["eat","sleep"],["code","eat"],["netflix","party"],["cs196","sleep"]];
    return sampleAInput;
//    gets the input from backend
}

function processInput(inputArray) {
    return inputArray;
//    processes input from backend
}

function getNextTuple(i, inputArray) {
    return inputArray[i];
}

function displayTuple(ith,changeColor,proportion) {
    $('.option1 p').text(ith[0]);
    $('.option2 p').text(ith[1]);

    if (changeColor === true) {
        $('.option1').css({
            'background-color':getRandomColor()
        });
        $('.option2').css({
            'background-color':getRandomColor()
        });
        $('#progress').css({
           'width':  (proportion*100)+'%'
        });

    }
    else {
        $('.option1').css({
            'background-color': 'black'
        });
        $('.option2').css({
            'background-color': 'black'
        });
        $('.question').text("");
        $('.main').css({
            backgroundColor: 'black'
        });
    }

}

function getTextFromOption(adiv) {
    return $(adiv).find('p').text()
}



$(document).ready(function() {

    var arr = processInput(getInput());
    var i = 0;
    var ith = getNextTuple(i,arr);
    displayTuple(ith,true,0);

   var output = [];
   var choice;
    $('.option1').click(function() {
        choice = getTextFromOption(this);

        if (i < arr.length - 1 ) {
            output.push([getTextFromOption($('.option1')),getTextFromOption($('.option2')),choice]);
            displayTuple(getNextTuple(i++,arr),true,i/arr.length);
        } else {
            console.log(output); // will return once backend is setup
            displayTuple(["Thank","You"],false,1);
        }
    });
    $('.option2').click(function() {
        choice = getTextFromOption(this);

        if (i < arr.length - 1 ) {
            output.push([getTextFromOption($('.option1')),getTextFromOption($('.option2')),choice]);
            displayTuple(getNextTuple(i++,arr),true,i/arr.length);
        } else {
            console.log(output);
            displayTuple(["Thank","You"],1);
        }
    });


});