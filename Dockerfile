FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements_streamlit.txt

COPY streamlit_app ./streamlit_app
COPY diabetes.csv ./diabetes.csv

CMD ["streamlit", "run", "streamlit_app/app.py", "--server.port=8501", "--server.address=0.0.0.0"]