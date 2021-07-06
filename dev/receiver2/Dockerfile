ARG GO_IMAGE="gcr.io/distroless/base"
FROM golang:1.16 as builder

# `skaffold debug` sets SKAFFOLD_GO_GCFLAGS to disable compiler optimizations
ARG SKAFFOLD_GO_GCFLAGS

WORKDIR /tmp_app
COPY main.go .
COPY go.mod .
COPY go.sum .

RUN go mod download

# TASK: How to control versions for the deps from repos?
# RUN set -x && \
#     go get github.com/kubemq-io/kubemq-go@v1.5.0 && \
#     go get github.com/nats-io/nuid@v1.0.1
    #go get github.com/2tvenom/go-test-teamcity && \  
#    dep ensure -v


#RUN dep ensure --vendor-only
RUN go build -gcflags="${SKAFFOLD_GO_GCFLAGS}" -o /app main.go
#RUN go build -o /app main.go

RUN ls /


FROM ${GO_IMAGE} as final   
# FROM alpine:3
# Define GOTRACEBACK to mark this container as using the Go language runtime
# for `skaffold debug` (https://skaffold.dev/docs/workflows/debug/).
# Maybe use an ARG config for this variable.
RUN mkdir /lib64 && ln -s /lib/libc.musl-x86_64.so.1 /lib64/ld-linux-x86-64.so.2
ENV GOTRACEBACK=single 
COPY --from=builder /app .
RUN ls -lh
#CMD ["./app"]
CMD ["sleep", "3000"]