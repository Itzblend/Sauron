FROM ubuntu:18.04 AS ubuntu_base

ARG KAFKA_VERSION="3.2.0"
ARG KAFKA_DIR="/usr/kafka"

RUN \
  sed -i 's/# \(.*multiverse$\)/\1/g' /etc/apt/sources.list && \
  apt-get update && \
  apt-get -y upgrade && \
  apt-get install -y build-essential && \
  apt-get install -y software-properties-common && \
  apt-get install -y byobu curl git htop man unzip vim wget nano && \
  rm -rf /var/lib/apt/lists/* && \
  add-apt-repository ppa:webupd8team/java && \
  apt install default-jdk -y && \
  apt install default-jre -y

FROM ubuntu_base AS kafka_base
RUN \
    mkdir ${KAFKA_DIR} && \
    curl "https://archive.apache.org/dist/kafka/$KAFKA_VERSION/kafka_2.12-3.2.0.tgz" -o ${KAFKA_DIR}/kafka.tgz && \
    tar -xzf ${KAFKA_DIR}/kafka.tgz -C ${KAFKA_DIR} --strip-components 1 && \
    rm ${KAFKA_DIR}/kafka.tgz


# Set environment variables.
ENV HOME /root
ENV KAFKA_BIN ${KAFKA_DIR}/bin
ENV KAFKA_HOME ${KAFKA_DIR}
ENV PATH="$KAFKA_BIN:$PATH"

COPY config.sh $KAFKA_DIR/config.sh

# Define working directory.
WORKDIR /root

# Define default command.
CMD ["bash"]

# Build image
# docker build -t kafka_base .
# docker run -it -p 9010:9092 --rm --name kafka_base1 kafka_base
# docker cp config/kafka1/server.properties kafka_base1:/usr/kafka/config/kraft/server.properties
# docker exec -it kafka_base1 bash