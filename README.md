# Project Setup Instructions

## Prerequisites

Before starting, ensure you have the following installed on your system:

- **Docker**
- **Docker Compose**
- **Make** (Linux/macOS users) or a compatible tool (Windows users)

## Steps to Run the Project

### 1. Setup the `.env` File

1. Locate the `.env.example` file in the project directory.
2. Create a new `.env` file:
   - On macOS/Linux:
     ```bash
     cp .env.example .env
     ```
   - On Windows:
     ```cmd
     copy .env.example .env
     ```
3. Open the `.env` file and configure all required environment variables as needed.

### 2. Start the Services

Depending on your operating system, follow the instructions below:

#### For macOS/Linux Users

1. Open your terminal.
2. Run the following command to start the project using the `Makefile`:
   ```bash
   make services
   ```

#### For Windows Users

Windows does not natively support `make`. You can:

1. Install `make` using [Chocolatey](https://chocolatey.org/) or another package manager:
   ```cmd
   choco install make
   ```
2. Alternatively, run the `docker-compose` command directly from the `Makefile`:
   ```cmd
   test -f .env || type nul > .env
   docker-compose -f docker-compose.local.yml up --build
   ```

### 3. Access the Project

Once the services are running, you can access the application as defined in your `docker-compose.local.yml` file (e.g., at `http://localhost:8000`).

## Notes

- Ensure your `.env` file is correctly set up before starting the services.
- If you encounter any issues, verify that Docker and Docker Compose are correctly installed and configured.
- To stop the services, press `Ctrl+C` or run the following command:
  ```bash
  docker-compose -f docker-compose.local.yml down
  ```

Feel free to reach out if you have questions or encounter any issues during setup.
