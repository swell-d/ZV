function resultReload() {
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