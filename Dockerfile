# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Create output directory
RUN mkdir -p generated_games

# Set default command
CMD ["python", "app/orchestrator.py"]
