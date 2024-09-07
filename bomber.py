/*
## Steps to use
1) Open web.whatsapp.com
2) Select the contact whom you want to send these messages
3) Open console and paste this script.
4) You can tweak DELAY, TOTAL_MESSAGES and message as per your need ;)
*/

var DELAY = 1000 // in milliseconds
var TOTAL_MESSAGES = 100 
var message = "You are a Rockstar!";

var messageBox = $('footer .copyable-text.selectable-text');
window.InputEvent = window.Event || window.InputEvent;
var event = new InputEvent('input', {bubbles: true});

var messageBomber = function(i,$){
    setTimeout(function(){
        messageBox.innerHTML = message;
        messageBox.dispatchEvent(event);
        $('footer [data-testid=send]').parentElement.click();
    },DELAY)
}


for(i=1; i<=TOTAL_MESSAGES; i++){
    messageBomber(i,$)
}