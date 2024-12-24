
# Welcome to My Portfolio Website

Welcome to my Portfolio Website project! This dynamic web application is designed to showcase your work, experience, projects, certifications, skills, blog posts, and publications—just like I'm using it. It's fully customizable through a backend administration interface, allowing you to add and modify content even after deployment.

## Features

- **Showcase Your Work**: Display projects, skills, certifications, and blog posts.
- **Admin Interface**: Easily add, modify, and delete content through Django's powerful admin panel.
- **Dynamic Sections**: Includes pages for your portfolio, projects, experience, education, and more.
- **Responsive Design**: Optimized for viewing on desktops, tablets, and mobile devices.
- **Customizable**: Fully flexible content through the admin panel.

## Directory Structure

```
└── J0-Y0-GO2COD-FS-03/
    ├── manage.py
    ├── portfolio_app/
    │   ├── models.py
    │   ├── __init__.py
    │   ├── urls.py
    │   ├── tests.py
    │   ├── apps.py
    │   ├── migrations/
    │   │   ├── 0014_rename_social_logo_sociallink_logo.py
    │   │   ├── 0003_project_slug.py
    │   │   ├── 0018_rename_job_title_experience_position.py
    │   │   ├── 0009_alter_skill_description_alter_skill_logo.py
    │   │   ├── 0002_tag_created_at.py
    │   │   ├── 0020_alter_jobtask_task.py
    │   │   ├── 0013_rename_intro_profile_sub_heading.py
    │   │   ├── 0007_certifications_certificate_link.py
    │   │   ├── __init__.py
    │   │   ├── 0004_profile_delete_about.py
    │   │   ├── 0017_sociallink_your_address.py
    │   │   ├── 0005_education_address_education_website.py
    │   │   ├── 0008_skill_logo.py
    │   │   ├── 0015_remove_sociallink_username_url_and_more.py
    │   │   ├── 0010_alter_skill_logo_alter_sociallink_social_logo.py
    │   │   ├── 0012_profile_heading.py
    │   │   ├── 0016_remove_sociallink_your_address.py
    │   │   ├── 0011_alter_skill_name_alter_sociallink_username_url.py
    │   │   ├── 0006_certifications.py
    │   │   ├── 0001_initial.py
    │   │   └── 0019_jobtask.py
    │   ├── admin.py
    │   ├── views.py
    │   └── templates/
    │       ├── index.html
    │       ├── components/
    │       │   ├── social_account.html
    │       │   ├── footer.html
    │       │   ├── pin.html
    │       │   ├── button_contact.html
    │       │   └── navbar.html
    │       ├── base.html
    │       └── pages/
    │           ├── contact.html
    │           ├── projects.html
    │           ├── landing.html
    │           ├── about.html
    │           ├── experience.html
    │           ├── education.html
    │           └── projects_detail.html
    ├── core/
    │   ├── settings.py
    │   ├── __init__.py
    │   ├── urls.py
    │   ├── asgi.py
    │   └── wsgi.py
    ├── media/
    │   ├── skill_logos/
    │   │   ├── _I3A9309_2.JPG
    │   │   └── _I3A9309_2_rfMqbQ1.JPG
    │   └── social_logos/
    ├── Pipfile
    ├── LICENSE
    ├── README.md
    └── static/
        ├── img/
        │   ├── p.PNG
        │   ├── c.PNG
        │   ├── recept delivery srervice.docx
        │   ├── d.PNG
        │   └── aos-master.zip
        ├── style/
        │   ├── sass/
        │   │   ├── _navbar.scss
        │   │   ├── _education.scss
        │   │   ├── _about.scss
        │   │   ├── _theme.scss
        │   │   ├── _project.scss
        │   │   ├── style.scss
        │   │   ├── _button_contact.scss
        │   │   └── _experience.scss
        │   └── css/
        │       └── style.css
        └── js/
```

## Installation

### Prerequisites

Make sure you have the following installed:

- Python 3.x
- Django
- PostgreSQL or MySQL

### Backend Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/J0-Y0/GO2COD-FS-03.git
   cd J0-Y0-GO2COD-FS-03
   ```

2. Install Python dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up the database:

   - Create a PostgreSQL or MySQL database.
   - Update `DATABASES` in `core/settings.py` with your database credentials.

4. Apply migrations:

   ```bash
   python manage.py migrate
   ```

5. Create a superuser for the admin panel:

   ```bash
   python manage.py createsuperuser
   ```

6. Run the backend server:

   ```bash
   python manage.py runserver
   ```

### Frontend Setup

1. Navigate to the `static/` directory:

   ```bash
   cd static
   ```

2. Install npm dependencies (if applicable):

   ```bash
   npm install
   ```

3. Start the frontend development server:

   ```bash
   npm start
   ```

   The frontend will be available at `http://localhost:3000`.

## Usage

- Access the admin panel at `http://localhost:8000/admin` to manage your portfolio content.
- Visit `http://localhost:8000` for the public-facing portfolio website.

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Clone your fork:
   ```bash
   git clone https://github.com/YOUR_USERNAME/GO2COD-FS-03.git
   ```
3. Create a new branch:
   ```bash
   git checkout -b feature-branch
   ```
4. Commit your changes:
   ```bash
   git commit -m "Add new feature"
   ```
5. Push to your fork:
   ```bash
   git push origin feature-branch
   ```
6. Submit a pull request to the main repository.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## GitHub Repository

You can view the source code and contribute to the project here:  
[Portfolio Website GitHub Repository](https://github.com/J0-Y0/GO2COD-FS-03)
