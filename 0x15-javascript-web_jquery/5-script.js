const $listElem = $('ul.my_list');
const $addItemElem = $('DIV#add_item');

$addItemElem.on('click', () => {
    $listElem.append('<li>Item</li>');
});