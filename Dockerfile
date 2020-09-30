# Site Build
FROM node:lts-slim as build

ENV NODE_ENV production

WORKDIR /app

COPY . /app

RUN npm ci --production

RUN npm run release

# Production run
FROM nginx:stable-alpine

COPY nginx.conf /etc/nginx/nginx.conf

COPY --from=build /app/public/ /usr/share/nginx/html
