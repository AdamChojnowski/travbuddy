$(function(){
    window.filteredPeople = [];
});

function updateFilter()
{
    var params;

    renderFilter();
}

function renderFilter()
{
    var listaLudzi = $("#peopleList");
    listaLudzi.html('');
    var i;
    for(i = 0; i < window.filteredPeople.length; i++)
    {
        listaLudzi.append(renderPersonPreview(window.filteredPeople[i]));
    }
}

function renderPersonPreview(person)
{
    var html = $('<div><h3>' + person.name + ' ' + person.surname + '</h3></div>');



    return html;
}