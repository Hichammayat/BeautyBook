BeautyBook

BeautyBook is a platform designed to streamline the connection between beauty professionals and clients, enhancing the booking and tutorship experience within the beauty industry.

Features:
Professional Profiles: Detailed profiles of beauty professionals showcasing their services, experience, and ratings.

Direct Contact Booking: Clients interested in a professional's services can send their personal information through the platform, facilitating direct communication for appointment scheduling.

Market-Specific Customization: Tailored for the Moroccan market initially, BeautyBook can be adapted for use in other regions, addressing local preferences and needs.

Technologies Used:
Python: Backend development using the Flask framework.
HTML/CSS: Frontend design and styling.
JavaScript: Frontend interactivity and user experience enhancements.
MySQL: Database management.
Git: Version control and collaboration.

Installation:
Clone the repository:
git clone <repository_url>
Install dependencies:
pip install -r requirements.txt
Set up the database:

Modify the SQLALCHEMY_DATABASE_URI in app.py to point to your MySQL database.
Run the following commands in your terminal:
python
>>> from app import db
>>> db.create_all()
>>> exit()
Run the application:
python app.py
Access the application in your web browser at http://localhost:5000.

Usage:
Visit the website to explore beauty professionals' profiles.
Interested clients can send their personal information through the platform to schedule appointments directly with professionals.
Contributing:
Contributions are welcome! Feel free to open an issue or submit a pull request.

License:
This project is licensed under the MIT License. See the LICENSE file for details.