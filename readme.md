# Query Wizard: An AI-Driven Ticket Filtering System

## Overview

**Query Wizard** is an AI-driven ticket filtering system that interprets natural language queries and translates them into technical filter criteria for efficient ticket retrieval. The system consists of a backend API built with FastAPI and a frontend user interface implemented using Streamlit.

## Project Structure

Here’s the structure of the `nl_ticket_filter` project:

![Alt text]("https://github.com/TheerajSubhakaarAS/Query_Wizard/blob/main/data/asset/structure.jpg")


## Setup and Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-repo/nl_ticket_filter.git
cd nl_ticket_filter
```
### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
### 3. Install Dependencies

```bash
pip install -r requirements.txt
```
## Running the Application

### Backend

The backend is developed using `FastAPI` and can be started with `Uvicorn`. It provides the API endpoints for processing queries and retrieving tickets.

To run the backend server, use:

```bash
uvicorn backend.main:app --reload
```
This command starts the FastAPI server in development mode with auto-reload enabled. The backend will be available at `http://127.0.0.1:8000`.

### Frontend

The frontend is built with Streamlit, offering a user-friendly interface for inputting natural language queries and viewing results.

To start the Streamlit application, use:
```bash
streamlit run frontend/app.py
```

This command launches the Streamlit server, and the frontend will be accessible at `http://localhost:8501`. 

## Testing

To run the unit tests for the project, use:
```bash
pytest
```
Ensure that you have the `pytest` module installed in your virtual environment.

## Contact


This `README.md` provides a clean and informative guide for setting up, running, and testing your project, along with details on the project structure and contact information. Feel free to adjust any details such as the repository URL or contact information as needed.
