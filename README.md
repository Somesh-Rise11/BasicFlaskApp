# Neo4j Aura Flask App with OpenAI Integration

This is a Flask application that demonstrates the integration of a Neo4j Aura graph database with OpenAI's API. The application provides endpoints to interact with the Neo4j database and to ask questions to OpenAI's GPT-3 model.

## Features

- **Home Route:** Welcome message.
- **Nodes Route:** Retrieve a list of nodes from the Neo4j database.
- **Ask OpenAI Route:** Get answers from OpenAI's GPT-3 model based on user input.

## Prerequisites

- Python 3.7+
- Neo4j Aura account
- OpenAI API key

## Setup

1. **Clone the repository:**

    ```sh
    git clone https://github.com/your-username/neo4j-flask-openai.git
    cd neo4j-flask-openai
    ```

2. **Install the required packages:**

    ```sh
    pip install flask neo4j openai
    ```

3. **Update the OpenAI API key:**

    Replace `'your_openai_api_key_here'` with your actual OpenAI API key in the `app.py` file:

    ```python
    openai.api_key = 'your_openai_api_key_here'
    ```

4. **Run the application:**

    ```sh
    python app.py
    ```

## Endpoints

### Home Route

- **URL:** `/`
- **Method:** GET
- **Description:** Returns a welcome message.

### Nodes Route

- **URL:** `/nodes`
- **Method:** GET
- **Description:** Retrieves a list of nodes from the Neo4j database (limited to 25 nodes).
- **Response Example:**

    ```json
    [
        {
            "id": 1234,
            "labels": ["User"],
            "name": "Alice",
            "age": 30,
            "location": "New York"
        },
        ...
    ]
    ```

### Ask OpenAI Route

- **URL:** `/ask_openai`
- **Method:** POST
- **Description:** Sends a question to OpenAI's GPT-3 model and returns the answer.
- **Request Example:**

    ```json
    {
        "question": "What is the capital of France?"
    }
    ```

- **Response Example:**

    ```json
    {
        "answer": "The capital of France is Paris."
    }
    ```
