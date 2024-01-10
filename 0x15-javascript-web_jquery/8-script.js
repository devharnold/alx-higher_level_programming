const moviesUri = 'https://swapi-api.alx-tools.com/api/films/?format=json';
const $movieList = $('ul#list_movies');

$.ajax({
    url: moviesUri,
    datatype: 'json'
}).done((data) => {
    const movies = data.results;
    for (let i=0; i < movies.length; ++i) {
        const movieTitle = movies[i].titile;
        const element = `<li>${movieTitle}`;
        $movieList.append(element);
    }
});