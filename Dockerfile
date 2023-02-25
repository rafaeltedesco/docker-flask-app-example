FROM python

WORKDIR /app/www/

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENV PORT 3005
ENV APP_NAME "Docker Flask - APP"

CMD flask --app src/hello_world run --port ${PORT} --host 0.0.0.0