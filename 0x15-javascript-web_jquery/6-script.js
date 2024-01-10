const $headerElem = $('header');
const $updateHeaderElem = $('DIV#update_header');

$updateHeaderElem.on('click', () => {
    $headerElem.text('New Header!!!');
});