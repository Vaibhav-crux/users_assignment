# Step 1: Use an official Python runtime as a parent image
FROM python:3.9-slim

# Step 2: Set the working directory in the container
WORKDIR /app

# Step 3: Copy the requirements file to the container
COPY requirements.txt .

# Step 4: Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy the rest of the application code to the container
COPY . .

# Step 6: Set environment variables (optional, but recommended for production)
ENV FLASK_ENV=production  
ENV PYTHONUNBUFFERED=1

# Step 7: Expose the Flask app port (if applicable)
EXPOSE 5000

# Step 8: Define the command to run your app
CMD ["python", "main.py"]
