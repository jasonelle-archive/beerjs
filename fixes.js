$(document).ready(() => {

    // small fixes to the website
    const body = $(document.body);
    body.css("padding-top", "10%");
    body.css("background-color", "#F8DC3D");

    // Deface a little the website
    $(".new").html("Jasonelle Rocks!");
    $(".intro").html(`
        <h1>Jasonelle <b>Framework</b></h1>
        <h2>Native<br> Apps <span>+</span> made <br> with JSON</h2>
    `);

    $('img[src="assets/ediciones/mayo2019-cornershop.jpg"]').attr("src", "https://avatars2.githubusercontent.com/u/20961094?s=500&v=4");
    const figcaption = $('figcaption');
    figcaption.html("Jasonelle");

    // Remove Target _blank because they mess with iOS navigation
    $('a[target="_blank"]').removeAttr("target");
    
});