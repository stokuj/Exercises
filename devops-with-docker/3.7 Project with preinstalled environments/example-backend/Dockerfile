FROM golang:1.23-alpine AS builder

WORKDIR /app

COPY go.mod go.sum* ./
RUN go mod download

COPY . .
RUN go test ./... && \
    CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o server .

FROM alpine:3.19

RUN apk --no-cache add ca-certificates

WORKDIR /root/

COPY --from=builder /app/server .

ENV PORT=8080 \
    REQUEST_ORIGIN=http://localhost:5000

EXPOSE ${PORT}

CMD ["./server"]