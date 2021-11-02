FROM python:3.9.7

EXPOSE 5000

ENV APP /app
WORKDIR $APP

COPY requirements.txt .
RUN python3 -m pip install -r requirements.txt

WORKDIR $APP
COPY . $APP
ENV PYTHONPATH "${PYTHONPATH}:$APP"

CMD [ "python3", "app.py"]