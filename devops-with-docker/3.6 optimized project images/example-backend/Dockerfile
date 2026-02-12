FROM golang:1.16-buster AS builder

WORKDIR /app

COPY go.mod go.sum* ./
RUN go mod download

COPY . .
RUN go test ./... && \
    CGO_ENABLED=0 GOOS=linux go build -o server .

FROM ubuntu:22.04

RUN apt-get update && \
    apt-get install -y ca-certificates && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /root/

COPY --from=builder /app/server .

ENV PORT=8080 \
    REQUEST_ORIGIN=http://localhost:5000

EXPOSE ${PORT}

CMD ["./server"]