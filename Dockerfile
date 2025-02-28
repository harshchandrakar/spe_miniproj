FROM python:3.10

# Set the working directory
WORKDIR /app

# Copy all necessary files into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run tests during the build process
RUN python -m pytest -v calculator_test.py

# Ensure the main script is executable
RUN chmod +x /app/scientific_calculator.py

# Set the default command to run the calculator
CMD ["python3", "/app/scientific_calculator.py"]
