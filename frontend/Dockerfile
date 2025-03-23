# Use official Node.js image
FROM node:18

# Set working directory inside the container
WORKDIR /app

# Copy package.json and install dependencies before copying other files
COPY . .
RUN npm install


# Build the React app
RUN npm run build

# Expose port 3000
EXPOSE 3000

# Serve the built app
CMD ["npx", "serve", "-s", "build", "-l", "3000"]
