const $headerElem = $('header');
const $divRedHeader = $('DIV#red_header');

$divRedHeader.on('click', function () {
    $headerElem.css('color', '#FF0000');
});