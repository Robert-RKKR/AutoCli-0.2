// SIDEBAR CLOSE ACTION:
var closeActiveElement = document.getElementById("page-left");
var closeToggleButton = document.getElementById("sidebar-close");

closeToggleButton.onclick = function () {
    closeActiveElement.classList.toggle("toggled");
};

// SIDEBAR SUB MENU ACTION:
var toggleButtons = document.getElementsByClassName("collapse-menu-link");

for(let i=0; i<toggleButtons.length; i++) {
    let toggleButton = toggleButtons[i]
    let activeElement = toggleButtons[i].nextElementSibling

    toggleButton.addEventListener("click", function(event) {
        
        if(activeElement.classList.contains("collapse") === false) {
            activeElement.classList.add("collapse");
        } else {
            for(let i=0; i<toggleButtons.length; i++) {
                let activeElementInside = toggleButtons[i].nextElementSibling
                activeElementInside.classList.add("collapse");
            }
            activeElement.classList.remove("collapse");
        }  

    });
}

// MESSAGE CLOSE ACTION:
var messages = document.getElementsByClassName("message");

for(let i=0; i<messages.length; i++) {
    let message = messages[i]
    let closeButton = message.getElementsByClassName("message-close")[0];
    
    closeButton.addEventListener("click", function(event) {
        message.parentElement.removeChild(message);
    })

}

// FILTER CLOSE ACTION:
var activeElement = document.getElementById("model-filter");
var toggleButton = document.getElementById("model-filter-button");

toggleButton.onclick = function () {

    if(activeElement.classList.contains("collapse") === false) {
        activeElement.classList.add("collapse");
    } else {
        activeElement.classList.remove("collapse");
    }
};