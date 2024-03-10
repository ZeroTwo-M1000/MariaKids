# MariaKids Project

> Welcome to the MariaKids project repository. This fullstack application is crafted with FastAPI, Prisma and Vue, designed to power a robust and scalable application.

## Features 🌟

- **FastAPI**: Enjoy the high performance, easy to learn, fast to code, ready for production API framework.
- **Prisma**: Utilize the next-generation ORM for Node.js and TypeScript for efficient database management.
- **Uvicorn**: Get the lightning-fast ASGI server for Python, with auto-reload for seamless development.
- **PostgreSQL**: Provide a reliable and scalable database solution for your modern application.
- **Makefile**: Use the Makefile to manage the development workflow.

## Prerequisites 📋

- **Python** 3.8+
- **Git** installed on your local system
- Basic understanding of **Python** programming and **Prisma ORM**
- Basic understanding of **PostgreSQL**
- Basic understanding of **Make**

## Installation 🛠️

To get started with the **MariaKids** project, clone the repository and navigate to the project directory:

```bash
git clone https://github.com/ZeroTwo-M1000/MariaKids.git
cd MariaKids
```
## Usage 🔌

> Use the following **Makefile** commands to manage the application:

### Setup

Prepare your development environment by **installing dependencies**, running **database migrations**, and generating the **Prisma** client:

```bash
make setup
```

If you want to **setup** and **run** the application at the same time:

```bash
make setup-run
```

### Running the application

Start the local development server with **auto-reloading** enabled:

```bash
make run
```
The application will be accessible at **`http://0.0.0.0:8000`**.

## Development Workflow :computer:

The **Makefile** contains **commands** for common development tasks:

- `make setup`: Set up the project by installing dependencies and preparing the database.
- `make run`: Launch the development server with hot reloading support.
- `make setup-run`: Execute both setup and run commands sequentially.
- `make lint`: Python Black do formatting.
- `make migrate`: Run the database migrations.
- `make generate`: Generate the Prisma client.
- `make install`: Install the project dependencies.
