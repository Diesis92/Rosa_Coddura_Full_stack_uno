$(document).ready(function() {

    $.ajax({
        url: "http://localhost:5000/studenti/",   // <-- indirizzo API su porta 5000, in caso cambiare
        method: "GET",
        dataType: "json",

        success: function(data) {

            console.log(data); // DEBUG

            var html = "<ul>";

            $.each(data, function(index, item) {
                html += "<li>" + item.nome + "</li>";
            });

            html += "</ul>";

            $("#contenitore").html(html);
        },

        error: function(err) {
            console.error("Errore:", err);
        }
    });

});