FROM python:3.7-slim

COPY requirements.txt .

RUN pip install -r requirements.txt

# Parameter for permisions on dev images
ARG ENV=PROD
ENV K_ENV $ENV
ENV DEV_USER=1000

WORKDIR /app
ADD test-receiver.py /app

# Permissions for Skafold dev Profile to allow file sync
RUN if [ "${K_ENV}" = "DEV" ] ; then \
  chown ${DEV_USER} /app && \
  chown ${DEV_USER} /app/test-sender.py; \
fi

CMD ["python3.7", "test-receiver.py"]
