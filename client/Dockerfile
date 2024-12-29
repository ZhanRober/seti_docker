# Stage 1: Build React App
FROM node:16 AS build

# Set the working directory
WORKDIR /app

# Copy package.json and package-lock.json for installing dependencies
COPY package.json package-lock.json* ./

# Install dependencies and clean cache
RUN npm install --legacy-peer-deps && npm cache clean --force
RUN npm install ajv && npm cache clean --force

# Copy the application source files
COPY public ./public
COPY src ./src

# Build the React app
RUN npm run build

# Stage 2: Serve React App with Nginx
FROM nginx:alpine

# Copy built files from the previous stage to Nginx's html directory
COPY --from=build /app/build /usr/share/nginx/html

# Expose port 80
EXPOSE 80

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]
CMD ["nginx", "-g", "daemon off;"]