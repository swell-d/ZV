function resultReload() {
    const prosthodontics = ((document.getElementById("prosthodontics") || {}).checked) || "";
    const prosthodontics_full_obj = document.getElementById("prosthodontics_full");
    const prosthodontics_full_block = document.getElementById("prosthodontics_full_block");
    if (prosthodontics == "") {
        prosthodontics_full_obj.checked = false;
        prosthodontics_full_block.classList.add("d-none");
    } else {
        prosthodontics_full_block.classList.remove("d-none");
    }

    const Http = new XMLHttpRequest();
    const urlSearchParams = new URLSearchParams();
    urlSearchParams.set('age', ((document.getElementById("age") || {}).value) || "");
    urlSearchParams.set('teeth', ((document.getElementById("teeth") || {}).value) || "");
    urlSearchParams.set('prosthodontics', ((document.getElementById("prosthodontics") || {}).checked) || "");
    urlSearchParams.set('prosthodontics_full', ((document.getElementById("prosthodontics_full") || {}).checked) || "");
    urlSearchParams.set('orto', ((document.getElementById("orto") || {}).checked) || "");
    urlSearchParams.set('unlimited', ((document.getElementById("unlimited") || {}).checked) || "");

    Http.open("GET", location.href.split('?')[0] + 'calculate?' + urlSearchParams.toString());
    Http.send();
    Http.onreadystatechange = (e) => {
        document.getElementById("results").innerHTML = Http.responseText;
    }
    window.history.pushState('', '', location.href.split('?')[0] + '?' + urlSearchParams.toString());
}