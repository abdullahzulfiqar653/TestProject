# Define .PHONY to avoid conflicts with files named like targets
.PHONY: services setup-env check-db help

# Default target when running `make`
help: 
	@echo "Available commands:"
	@echo "  make services      - Build and run the project with Docker Compose"
	@echo "  make setup-env     - Create .env file if it doesn't exist and configure environment variables"
	@echo "  make check-db      - Check if the database credentials are correctly set in the .env file"
	@echo "  make help          - Show this help message"

# Start the application services using Docker Compose
services: setup-env check-db
	docker-compose -f docker-compose.local.yml up --build

# Ensure .env exists and prompt the user to configure it
setup-env:
	@echo "Checking for .env file..."
	test -f .env || (echo ".env file not found. Creating one from .env.example."; cp .env.example .env)
	@echo "If this is the first time, configure the environment variables in .env (especially database settings)."

# Check database credentials in the .env file
check-db:
	@echo "Validating database credentials in .env..."
	@if ! grep -q "DB_HOST=" .env || ! grep -q "DB_PORT=" .env || ! grep -q "DB_NAME=" .env || ! grep -q "DB_USER=" .env || ! grep -q "DB_PASSWORD=" .env; then \
	  echo "⚠️  Missing database credentials in .env. Please set the following variables:"; \
	  echo "    - DB_HOST"; \
	  echo "    - DB_PORT"; \
	  echo "    - DB_NAME"; \
	  echo "    - DB_USER"; \
