# Flask-WTF Demo

This repository demonstrates the use of Flask-WTF, an extension of Flask that integrates with WTForms to handle form validation and rendering in Flask applications.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Forms](#forms)
- [Routes](#routes)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Flask-WTF simplifies working with forms in Flask applications by providing a set of tools for form validation, CSRF protection, and rendering HTML forms. This demo project showcases how to create forms, validate user inputs, and handle form submissions securely using Flask-WTF.

## Features

- **Form Validation:** Easily validate user input with built-in and custom validators.
- **CSRF Protection:** Automatically protect forms from Cross-Site Request Forgery (CSRF) attacks.
- **Seamless Integration:** Integrates seamlessly with Flask to handle forms and user inputs.
- **Customizable Forms:** Build and customize forms using WTForms' flexible form field types.

## Prerequisites

Before running this project, ensure you have the following installed:

- Python 3.x
- Flask
- Flask-WTF

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/yourusername/flask-wtf-demo.git
    cd flask-wtf-demo
    ```

2. Create a virtual environment and activate it:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:

    ```bash
    flask run
    ```

## Usage

1. Access the application by navigating to `http://127.0.0.1:5000` in your web browser.
2. Fill out the form and submit it.
3. The server will validate the input and return the appropriate response.

## Project Structure

```plaintext
flask-wtf-demo/
│
├── app/
│   ├── __init__.py
│   ├── forms.py
│   ├── routes.py
│   └── templates/
│       └── form.html
├── venv/
│
├── requirements.txt
└── run.py
