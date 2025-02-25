# Use official Python image as a base
FROM python:3.11.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY . /app/

# Expose port 8000 for Django
EXPOSE 8000

# Run Django migrations and start the server
# CMD ["bash", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
ENTRYPOINT ["python", "manage.py"]

CMD ["migrate", "&&", "runserver", "0.0.0.0:8000"]
