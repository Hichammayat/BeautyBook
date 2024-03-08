document.addEventListener("DOMContentLoaded", function() {
  // Sélectionner le formulaire
  const form = document.querySelector('.registration-form');

  form.addEventListener('submit', function(e) {
      e.preventDefault(); // Empêche la soumission standard du formulaire

      // Création de l'objet FormData à partir du formulaire
      const formData = new FormData(form);

      // Conversion des données du formulaire en objet JSON
      const userData = {
          email: formData.get('email'),
          password: formData.get('password'),
          first_name: formData.get('first_name'),
          last_name: formData.get('last_name'),
          phone_number: formData.get('phone_number'),
          user_type: formData.get('user_type'),
          // Ajoutez ici d'autres champs si nécessaire
      };

      // Envoi de la requête POST à l'API pour ajouter un utilisateur
      fetch('http://localhost:5001/api/v1/users', {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json',
          },
          body: JSON.stringify(userData), // Conversion de l'objet utilisateur en chaîne JSON
      })
      .then(response => {
          if (response.ok) {
              return response.json(); // Traite la réponse en JSON si la requête a réussi
          }
          throw new Error('Network response was not ok.'); // Lance une erreur si la requête a échoué
      })
      .then(data => {
          console.log(data); // Affiche les données de réponse (l'utilisateur ajouté)
          // Ici, vous pouvez rediriger l'utilisateur ou afficher un message de succès
      })
      .catch(error => {
          console.error('There has been a problem with your fetch operation:', error);
      });
  });
});
