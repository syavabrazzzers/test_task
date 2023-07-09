FROM node:latest
RUN mkdir /app
COPY . /app
WORKDIR /app
RUN yarn
CMD ["yarn", "start"]
#CMD ["yarn", "global", "add", "serve"]
#CMD ["serve", "-s", "build"]