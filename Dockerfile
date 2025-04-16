# =================================
# Stage 1: Build the React frontend
# =================================
FROM node:16 AS frontend-build

WORKDIR /app

COPY frontend/ .

RUN npm install
RUN npm run build

# =================================
# Stage 2: Set up the Flask backend
# =================================
FROM python:3.12.2

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY flask/ .

RUN pip install --upgrade pip
RUN pip install pandas scikit-learn Flask flask-cors

COPY --from=frontend-build /app/build ./build

EXPOSE 5000

CMD ["python", "app.py"]