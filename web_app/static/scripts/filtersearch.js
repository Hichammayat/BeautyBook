function searchProfessionals() {
    const cityName = document.getElementById('search').value;
    fetch(`http://localhost:5001/api/v1/professionals/city/${cityName}`)
        .then(response => {
            if (!response.ok) {
                throw new Error('City not found');
            }
            return response.json();
        })
        .then(professionals => {
            const carousel = document.querySelector('.carousel');
            carousel.innerHTML = ''; // Vide le carousel avant d'ajouter les nouveaux résultats
            professionals.forEach(professional => {
                const figure = document.createElement('figure');
                figure.innerHTML = `
                    <img src="https://source.unsplash.com/featured/?beauty" alt="Beauty Professional" />
                    <div class="carousel-content">
                        <h3>${professional.first_name} ${professional.last_name}</h3>
                        <p>${professional.biography}</p>
                        <a href="/profile/${professional.id}" target="_blank">View Profile</a>
                    </div>
                `;
                carousel.appendChild(figure);
            });
        })
        .catch(error => {
            console.error('Error:', error);
        });
}

document.querySelector('button[type="submit"]').addEventListener('click', function(event) {
    event.preventDefault();
    searchProfessionals();
});