# Sentiment Analysis - backend

## Description

The `sas-backend-service` is the core backend component of the Sentiment Analysis. It provides a RESTful API for analyzing the sentiment of text input using a powerful AI-based sentiment analysis model.

## Features

* **Sentiment Analysis API:**
    * **POST /sentiment-analysis/create/:** Creates a new sentiment analysis for the given text input.
    * **GET /sentiment-analysis/:** Retrieves a list of previous sentiment analyses.
* **AI-Powered Model:** Utilizes a state-of-the-art sentiment analysis model (TextBlob) to accurately determine polarity (positive, negative, neutral) and subjectivity.
* **Scalable Architecture:** Built with Django and Django REST Framework for robust performance and scalability.
* **Database Integration:** Stores analysis results in a MySQL database for persistence and retrieval.
* **OpenAPI Documentation:** Interactive API documentation is available via Swagger UI at `/swagger/` url
* **Postman Collection:** A Postman collection is provided in the `postman/` directory to facilitate API testing.

## Architecture

The application follows a microservices architecture, consisting of two main components:

- **Client ([sas-client](https://github.com/giandonatoinverso/sas-client)):** Django web application that allows users to analyze the sentiment of a given text input.
- **Database ([sas-db](https://github.com/giandonatoinverso/sas-db)):** Stores the results of the sentiment analysis in a MySql database


## Installation with Docker Compose

1. **Prerequisites:**
   - Docker and Docker Compose installed on your system.
   - A `.env` file in the project's root directory containing the necessary environment variables (e.g., MySQL root password).

2. **Start the application:**
   ```bash
   docker compose build --no-cache && docker-compose up -d
   ```
3. **Accessing the Application**
   - Open your web browser and navigate to *http://localhost:8000* (or the address specified in your docker-compose.yml).

## API Documentation

Explore the interactive API documentation using Swagger UI:

- Navigate to *http://localhost:8080/swagger/* for Swagger UI style documentation.
- Navigate to *http://localhost:8080/redoc/* for ReDoc style documentation.
- Navigate to *http://localhost:8080/swagger.json* or *http://localhost:8080/swagger.yaml* to get the schema in JSON or YAML format.

## API Testing

The Postman collection in the *postman/* directory provides pre-configured requests for testing the API endpoints.

## Customization

The *sas-backend-service* is designed for flexibility and customization. The sentiment analysis functionality is implemented through a *sentiment_analyzer.py* interface, which can be easily swapped out with different implementations.

- *Current Implementation*: The default implementation uses TextBlob, a popular Python library for natural language processing.
- *Alternative Implementations*: You can replace TextBlob with other sentiment analysis tools or machine learning models, such as VADER, Stanford CoreNLP, or custom-trained models.

To customize the sentiment analysis engine, simply create a new class that implements the *sentiment_analyzer.py* interface and update the backend configuration to use your new implementation.

## Building and Publishing

This project includes a *taskfile.yml* script that simplifies the process of building and publishing a new version of the Docker image.

To build and publish the Docker image, run the following command:

```bash
task publish-docker
```