ARG DJANGO_CONTAINER_VERSION=2.0.2

FROM us-docker.pkg.dev/uwit-mci-axdd/containers/django-container:${DJANGO_CONTAINER_VERSION} as app-container

USER root

RUN apt-get update && apt-get install libpq-dev -y

ADD --chown=acait:acait docker/start.sh /scripts
RUN chmod -R +x /scripts

USER acait

ADD --chown=acait:acait . /app/
ADD --chown=acait:acait docker/ /app/project/

RUN . /app/bin/activate && pip install .

FROM us-docker.pkg.dev/uwit-mci-axdd/containers/django-test-container:${DJANGO_CONTAINER_VERSION} as app-test-container

COPY --from=app-container /app/ /app/
COPY --from=app-container /static/ /static/
