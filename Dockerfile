# Generate the requirements.txt file using Poetry
FROM python:3.12-slim AS generate-requirements

# Update the package list and install curl to fetch the Poetry installer
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# Install Poetry (version 1.2.2) for dependency management
RUN curl -sSL https://install.python-poetry.org | python3 - --version 1.2.2

# Copy the pyproject.toml and poetry.lock files to install dependencies
COPY pyproject.toml poetry.lock ./

# Use Poetry to export the dependencies to a requirements.txt file
RUN /root/.local/bin/poetry export -f requirements.txt --without-hashes -o requirements.txt

###

# Step 2: Build the production environment image
FROM python:3.12-slim AS production

# Set the working directory to /app
WORKDIR /app

# (Optional) Install system utilities if needed, such as build-essential
RUN apt-get update && apt-get install -y --no-install-recommends build-essential && rm -rf /var/lib/apt/lists/*

# Copy the requirements.txt file generated in the previous stage
COPY --from=generate-requirements /requirements.txt .

# Install the Python dependencies listed in the requirements.txt file
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files to the container
COPY . .

# Define the command to run the application with Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
