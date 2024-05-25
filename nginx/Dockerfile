FROM nginx:1.25
RUN mkdir -p /var/www/certbot/.well-known/acme-challenge && \
    chmod -R 755 /var/www/certbot
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d