FROM node:18-slim as build
WORKDIR /app
COPY . /app
RUN echo "Placeholder build"

FROM nginx:alpine
COPY --from=build /app /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
