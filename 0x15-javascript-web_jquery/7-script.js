const characterUri = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
const $charaterDiv = $('DIV#character');

$.ajax({
    url: characterUri,
    dataType: 'json'
}).done((data) => {
    $charaterDiv.text(data.name);
});