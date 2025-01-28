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

# Copy the backend source code and other necessary files
COPY . .

# Expose the Streamlit default port
EXPOSE 8501

# Run Streamlit app
CMD ["streamlit", "run", "streamlit_app/app.py"]
