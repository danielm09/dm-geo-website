FROM python:3.10-slim

# Create and set the working directory
WORKDIR /app

# Copy application code into the container
COPY . /app

RUN pip install --no-cache-dir streamlit

EXPOSE 8502

CMD bash -c "streamlit run ./main.py --server.port=8502"