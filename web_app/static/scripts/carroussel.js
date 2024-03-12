document.addEventListener('DOMContentLoaded', function () {
    var currentIndex = 0; // L'index du slide actuellement visible
    var items = document.querySelectorAll('.carousel figure'); // Tous les éléments du carrousel
    var itemCount = items.length; // Le nombre total d'éléments du carrousel

    // Fonction pour mettre à jour le carrousel à l'élément suivant/précédent
    function updateCarousel(move) {
        // Cache tous les éléments
        items.forEach(function (item) {
            item.style.display = 'none';
        });

        // Met à jour l'index actuel avec le déplacement demandé
        currentIndex += move;

        // Si l'index est hors limites, le ramène dans la plage valide
        if (currentIndex >= itemCount) {
            currentIndex = 0;
        } else if (currentIndex < 0) {
            currentIndex = itemCount - 1;
        }

        // Affiche l'élément actuel
        items[currentIndex].style.display = 'block';
    }

    // Initialise le carrousel pour afficher le premier élément
    updateCarousel(0);

    // Attache les gestionnaires d'événements aux flèches
    document.querySelector('.arrow.left').addEventListener('click', function() {
        updateCarousel(-1);
    });

    document.querySelector('.arrow.right').addEventListener('click', function() {
        updateCarousel(1);
    });
});
