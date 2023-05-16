function resultReload() {
    const Http = new XMLHttpRequest();
    const urlSearchParams = new URLSearchParams();
    urlSearchParams.set('age', ((document.getElementById("age") || {}).value) || "");
    urlSearchParams.set('teeth', ((document.getElementById("teeth") || {}).value) || "");
    urlSearchParams.set('prosthodontics', ((document.getElementById("prosthodontics") || {}).checked) || "");
    urlSearchParams.set('orto', ((document.getElementById("orto") || {}).checked) || "");

    Http.open("GET", location.href.split('?')[0] + 'calculate?' + urlSearchParams.toString());
    Http.send();
    Http.onreadystatechange = (e) => {
        document.getElementById("results").innerHTML = Http.responseText
    }
}