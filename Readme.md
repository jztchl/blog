<br />
<div align="center">
  <a href="https://github.com/kmvishnu625/blog">
    <img src="/static/assets/img/favicon.ico" alt="Logo" width="80" height="80">
  </a>

<h1 align="center">StrangeRover Blogs</h1>

  <p align="center">
   This is a blog website deigned to upload pictures and the story behind it
  </p>
</div>
<a href="https://strangeroverblogs.herokuapp.com/"  target=”_blank”>click here to check out the blog</a>

```markdown
# StrangeRover Blogs

![Logo](favicon.ico)

StrangeRover Blogs is a website designed to upload pictures and the stories behind them. This project is built using the Django framework.

[Check out the blog](https://your-blog-url.com)

## About

A simple and elegant blog platform where users can share pictures along with detailed stories or descriptions. The website is designed to be user-friendly, providing an enjoyable experience for both authors and readers.

## Features

- **Picture Upload**: Upload images to accompany your blog posts.
- **Storytelling**: Add detailed stories or descriptions to your images.
- **User Management**: Create, update, and manage user profiles.
- **Responsive Design**: Ensures the blog looks great on all devices.

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/jztchl/blog.git
   cd blog
   ```

2. **Create and Activate a Virtual Environment**
   ```bash
   python3 -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**
   ```bash
   python manage.py migrate
   ```

5. **Run the Server**
   ```bash
   python manage.py runserver
   ```

## Project Structure

- **app/**: Directory containing the main application logic.
- **project/**: Directory containing the project settings and configurations.
- **static/**: Directory for static files (CSS, JavaScript, images).
- **template/**: Directory for HTML templates.
- **db.sqlite3**: SQLite database file.
- **manage.py**: Django management script.
- **requirements.txt**: File listing required Python packages.
- **vercel.json**: Configuration file for Vercel deployment.
- **Procfile**: Configuration for deploying to platforms like Heroku.
- **build_files.sh**: Script for building the project for deployment.

## Deployment

The website can be deployed using platforms like Vercel or Heroku. Ensure you configure the necessary environment variables and follow platform-specific deployment guides.

## Contributing

Contributions are welcome! Please create an issue or submit a pull request for any improvements or bug fixes.

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Open a pull request

## License

This project is licensed under the MIT License.

## Contact

For any inquiries, please visit our [Contact Page](https://your-blog-url.com/contact).
```
