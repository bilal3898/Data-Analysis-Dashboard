# Use official Node.js LTS Alpine image for lightweight build
FROM node:18-alpine AS build

# Set working directory inside the container
WORKDIR /app

# Copy package.json and package-lock.json for dependency installation
COPY package.json package-lock.json ./

# Install dependencies
RUN npm install --frozen-lockfile

# Copy the entire project
COPY . .

# Build the React app for production
RUN npm run build

# Use Nginx for serving static files
FROM nginx:stable-alpine

# Copy the build output from Node.js container to Nginx
COPY --from=build /app/dist /usr/share/nginx/html

# Expose port 80
EXPOSE 80

# Start Nginx server
CMD ["nginx", "-g", "daemon off;"]
