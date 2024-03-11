POETRY = poetry
PRISMA = $(POETRY) run prisma
UVICORN = $(POETRY) run uvicorn
SRC_DIR = src
HOST = 0.0.0.0
PORT = 8000
APP_PATH = main:app
YARN = yarn
BUILD = $(YARN) build
CLIENT_DIR = client

.PHONY: setup install migrate generate run, lint, client

install:
	@echo "Installing dependencies..."
	$(POETRY) install

migrate:
	@echo "Running database migrations..."
	$(PRISMA) migrate dev --name init

client:
	@echo "Installing dependencies..."
	(cd $(CLIENT_DIR) && $(YARN) && $(BUILD))

build:
	@echo "Building..."
	(cd $(CLIENT_DIR) && $(BUILD))

generate:
	@echo "Generating Prisma client..."
	$(PRISMA) generate

run:
	@echo "Starting the development server..."
	(cd $(SRC_DIR) && $(UVICORN) $(APP_PATH) --reload --host $(HOST) --port $(PORT))

lint:
	@echo "Running linter..."
	$(POETRY) run black $(SRC_DIR)


setup: install migrate generate client

setup-run: setup run
