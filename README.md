Here's the updated **README.md** file with database setup instructions and Makefile integration:

---

### **README.md**

# Project Setup Instructions

### **⚠️ Important Note: Database Configuration**

> ⚠️ **WARNING**:  
> The database is **NOT included in the Docker setup**.  
> You must configure the database credentials correctly in the `.env` file.  
> Double-check the following variables in the `.env` file to ensure they match your database setup:
>
> - `DB_HOST`
> - `DB_PORT`
> - `DB_NAME`
> - `DB_USER`
> - `DB_PASSWORD`  
>   Ensure your database is running independently and accessible by the application.

---

### **Prerequisites**

1. **Required Tools**:
   - **Docker**: [Install Docker](https://docs.docker.com/get-docker/)
   - **Docker Compose**: Pre-installed with Docker Desktop.
   - **Make**:
     - On **macOS/Linux**, it’s often pre-installed. Otherwise, install it using your package manager (`apt`, `yum`, or `brew`).
     - On **Windows**, install **Make** via [Chocolatey](https://chocolatey.org/):
       ```bash
       choco install make
       ```
     - Alternatively, use the equivalent raw commands provided below if `make` is unavailable.

---

### **Setup Instructions**

1. **Clone the Repository**:
   Clone the repository to your local machine:

   ```bash
   git clone <repository-url>
   cd <project-directory>
   ```

2. **Create the `.env` File**:

   - Copy the contents of `.env.example` to a new file named `.env`:
     ```bash
     cp .env.example .env
     ```
   - Open `.env` and update the required environment variables:
     - **Database Variables**: Ensure `DB_HOST`, `DB_PORT`, `DB_NAME`, `DB_USER`, and `DB_PASSWORD` match your database setup.

3. **Run the Project**:

   - **Using `make` (Recommended)**:
     - To build and start the project:
       ```bash
       make services
       ```
   - **Without `make`**:
     - Manually create the `.env` file (if not already done):
       ```bash
       test -f .env || cp .env.example .env
       ```
     - Then build and start the services:
       ```bash
       docker-compose -f docker-compose.local.yml up --build
       ```

4. **Access the Application**:
   - Once the containers are running, check the terminal logs for accessible URLs and ports.

---

### **Available Make Commands**

| Command          | Description                                                               |
| ---------------- | ------------------------------------------------------------------------- |
| `make services`  | Build and run the project with Docker Compose.                            |
| `make setup-env` | Create the `.env` file if it doesn't exist and prompt for variable setup. |
| `make check-db`  | Validate that database credentials are properly configured in the `.env`. |
| `make help`      | Show available make commands.                                             |

---

### **Common Issues**

1. **Database Connection Errors**:

   - Ensure the database service is running independently and reachable from the application.

2. **Environment File Issues**:

   - If `.env` is missing, Docker might fail to start. Follow the `.env` setup instructions above.

3. **Windows-Specific Issues**:
   - If `make` is unavailable, use the raw `docker-compose` commands provided.

---

Let me know if you need further assistance!
