FROM ubuntu

RUN apt-get update && apt-get install -y nginx && touch index.html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
