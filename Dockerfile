## Install python demo package
FROM ubuntu:20.04 as py-builder

RUN apt-get -y update
RUN apt-get -y install \
        python3-setuptools python3-wheel python3-pip

ENV PYTHONUSERBASE=/srv/pod-lifecycle-demo
COPY . /src/
RUN pip3 install --user /src


## Runtime image
FROM ubuntu:20.04
ARG version=v1

RUN apt-get -y update && \
    apt-get -y install --no-install-recommends \
        python3

COPY --from=py-builder /srv/pod-lifecycle-demo/ /srv/pod-lifecycle-demo/

ENV PYTHONUSERBASE=/srv/pod-lifecycle-demo
ENV FLASK_APP=demo.app
ENV VERSION=$version
CMD $PYTHONUSERBASE/bin/flask run --host=0.0.0.0
