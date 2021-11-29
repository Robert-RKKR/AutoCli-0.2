// SIDEBAR CLOSE ACTION:
var closeActiveElement = document.getElementById("page-left");
var closeToggleButton = document.getElementById("sidebar-close");

closeToggleButton.onclick = function () {
    closeActiveElement.classList.toggle("toggled");
};

// SIDEBAR SUB MENU ACTION:
var toggleButtons = document.getElementsByClassName("collapse-menu-link");
let cookies = document.cookie.split(";");

for(let i=0; i<cookies.length; i++) {
    let cookie = cookies[i].split("=");
    if(cookie[0] === "open_menu_action") {
        if(cookie[1] != "false") {
            let menu_number = parseInt(cookie[1]);
            for(let i=0; i<toggleButtons.length; i++) {
                if(i === menu_number) {
                    let toggleButton = toggleButtons[i];
                    let activeElement = toggleButtons[i].nextElementSibling;
                    
                    activeElement.classList.remove("collapse");
                }
            }
        }
    }
}

for(let i=0; i<toggleButtons.length; i++) {
    let toggleButton = toggleButtons[i];
    let activeElement = toggleButtons[i].nextElementSibling;

    toggleButton.addEventListener("click", function(event) {
        
        if(activeElement.classList.contains("collapse") === false) {
            activeElement.classList.add("collapse");
            document.cookie = 'open_menu_action=false';
        } else {
            for(let i=0; i<toggleButtons.length; i++) {
                let activeElementInside = toggleButtons[i].nextElementSibling
                activeElementInside.classList.add("collapse");
            }
            activeElement.classList.remove("collapse");
            document.cookie = 'open_menu_action=' + i;
        }  

    });
}

// CHECK ITEM ACTION:
let box_items_button = document.getElementById("check-item-button");

box_items_button.addEventListener("click", function(event) {
    let box_item_checks = document.getElementsByClassName("check-item");

    for(let i=0; i<box_item_checks.length; i++) {
        let box_item_check = box_item_checks[i]

        if(box_item_check.classList.contains("collapse") === true) {
            box_item_check.classList.remove("collapse");
        } else {
            box_item_check.classList.add("collapse");
        }

    }
})

let box_items = document.getElementsByClassName("model-item");

for(let i=0; i<box_items.length; i++) {
    let box_item = box_items[i];
    let box_item_check = box_item.getElementsByClassName("check-item");
    
    box_item.addEventListener("click", function(event) {
        box_item_check.checked = true;
    })

}

// MESSAGE CLOSE ACTION:
var messages = document.getElementsByClassName("message");

for(let i=0; i<messages.length; i++) {
    let message = messages[i];
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