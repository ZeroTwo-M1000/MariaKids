# MariaKids Project

Welcome to the MariaKids project repository. This backend service is crafted with FastAPI and Prisma, designed to power a robust and scalable application.

## Features 🌟

- **FastAPI**: Enjoy the high performance, easy to learn, fast to code, ready for production API framework.
- **Prisma**: Utilize the next-generation ORM for Node.js and TypeScript for efficient database management.
- **Uvicorn**: Get the lightning-fast ASGI server for Python, with auto-reload for seamless development.

## Prerequisites 📋

- Python 3.8+
- Git installed on your local system
- Basic understanding of Python programming and Prisma ORM

## Installation 🛠️

To get started with the MariaKids project, clone the repository and navigate to the project directory:

```bash
git clone https://github.com/ZeroTwo-M1000/MariaKids.git
cd MariaKids
```
## Usage 🔌

Use the following Makefile commands to manage the application:

### Setup

Prepare your development environment by installing dependencies, running database migrations, and generating the Prisma client:

```bash
make setup
```
### Running the application

Start the local development server with auto-reloading enabled:

```bash
make run
```
The application will be accessible at http://0.0.0.0:8000.

## Development Workflow :computer:

The Makefile contains commands for common development tasks:

- make setup: Set up the project by installing dependencies and preparing the database.
- make run: Launch the development server with hot reloading support.
- make setup-run: Execute both setup and run commands sequentially.
