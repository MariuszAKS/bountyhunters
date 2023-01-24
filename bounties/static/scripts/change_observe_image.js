function changeObserveImage(id) {
    backgroundImage = document.getElementById("bounty-observe-button-" + id).style.backgroundImage

    if (backgroundImage == "url(\"static/images/eye_closed.png\")") {
        document.getElementById("bounty-observe-button-" + id).style.backgroundImage = "url(static/images/eye_opened.png)"
    }
    else if (backgroundImage == "url(\"static/images/eye_opened.png\")") {
        document.getElementById("bounty-observe-button-" + id).style.backgroundImage = "url(static/images/eye_closed.png)"
    }
}

function test() {
    document.getElementById("bounties_container").style.backgroundColor = "red";
}