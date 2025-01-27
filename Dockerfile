# Use the official Python image as base
FROM python:3.12.2

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN python -m venv /venv
# Set the working directory in the container
WORKDIR /app

# Install dependencies

RUN pip install pandas 
RUN pip install numpy 
RUN pip install scikit-learn
RUN pip install streamlit

# Copy the backend source code to the working directory
COPY . .

# Copy Streamlit app and other necessary files
COPY streamlit_app ./streamlit_app
COPY diabetes.csv ./diabetes.csv

# Run Streamlit app
CMD ["streamlit", "run", "streamlit_app/app.py"]
