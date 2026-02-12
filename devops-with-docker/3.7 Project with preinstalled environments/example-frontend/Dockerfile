FROM node:16-alpine

WORKDIR /app

RUN apk --no-cache add ca-certificates

ENV REACT_APP_BACKEND_URL=/api

COPY package*.json ./
RUN npm install

COPY . .
RUN npm run build && \
    npm install -g serve

EXPOSE 5000

CMD ["serve", "-s", "build", "-l", "5000"]