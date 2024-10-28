FROM python:3.9

WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install any dependencies from requirements.txt
RUN pip install -r requirements.txt

# Run the runall.py script
CMD ["python", "runall.py"]
