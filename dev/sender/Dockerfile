FROM python:3.7-slim
#FROM python:3.7-slim AS build-env

COPY requirements.txt .

RUN pip install -r requirements.txt


# FROM gcr.io/distroless/python3
# FROM python:3.7-slim 

# COPY --from=build-env /usr/local/lib/python3.7/site-packages/ \
#  /usr/lib/python3.7/

ARG ENV=PROD
ENV K_ENV $ENV
ENV DEV_USER=1000

# Skaffold sync has issues with permissions on the files.
# It tries to connect to the pod with the current user, if that user does not have permissions to modify the files
# then sync fails.
# Alternative1: 
#   Add ownership to the user that skaffold would use for sync, the pod running user.
#   chown $DEV_USER /app 
#   ADD --chown 1000 test-sender.py /appç
# Alternative2: user profiles for dev and prod so in dev can allow more open permissions
#   See: https://github.com/GoogleContainerTools/skaffold/tree/master/integration/examples/hot-reload

WORKDIR /app
ADD test-sender.py /app

# Permissions for Skafold dev Profile to allow file sync
RUN if [ "${K_ENV}" = "DEV" ] ; then \
  chown ${DEV_USER} /app && \
  chown ${DEV_USER} /app/test-sender.py; \
fi

CMD ["python3.7", "test-sender.py"]
