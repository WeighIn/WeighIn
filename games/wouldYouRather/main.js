/**
 * Created by HarshayShah on 08/11/14.
 */

function getInput() {
    var sampleAInput = [["eat","sleep"],["code","eat"],["netflix","party"]];
    return sampleAInput;
}


function processInput(inputArray) {
    return inputArray;
}

function getNextTuple(i, inputArray) {
    return inputArray[i];
}

function displayTuple(ith) {
    $('.option1 p').text(ith[0]);
    $('.option2 p').text(ith[1]);
}
function getTextFromOption(adiv) {
    return $(adiv).find('p').text()
}


$(document).ready(function() {

    var arr = processInput(getInput());
    var i = 0;
    var ith = getNextTuple(i,arr);
    displayTuple(ith);

   var output = [];
   var choice;
    $('.option1').click(function() {
        choice = getTextFromOption(this);
        output.push([getTextFromOption($('.option1')),getTextFromOption($('.option2')),choice]);

        if (i < arr.length -1 ) {
            displayTuple(getNextTuple(++i,arr));
        } else {
            console.log(output);
            displayTuple(["Thank","You"]);
             // will return this once backend is connected
        }
    });
    $('.option2').click(function() {
        choice = getTextFromOption(this);
        output.push([getTextFromOption($('.option1')),getTextFromOption($('.option2')),choice]);
        if (i < arr.length -1 ) {
            displayTuple(getNextTuple(++i,arr));
        } else {
            console.log(output);
            displayTuple(["Thank","You"]);
        }
    });



});