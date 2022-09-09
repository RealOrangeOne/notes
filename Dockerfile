FROM node:slim as build

ENV NODE_ENV=production

COPY package.json package-lock.json ./
RUN npm ci --no-audit --progress=false --omit=dev

COPY . .
RUN npm run build

FROM theorangeone/website-server:latest

COPY --from=build ./public /srv
