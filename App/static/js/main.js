// SIDEBAR CLOSE ACTION:
var activeElement = document.getElementById("page-left");
var toggleButton = document.getElementById("sidebar-close");

toggleButton.onclick = function () {
    activeElement.classList.toggle("toggled");
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