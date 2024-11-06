# Use an official Apache HTTP Server image
FROM httpd:latest

# Copy a custom HTML file to the server's default directory
COPY ./index.html /usr/local/apache2/htdocs/

# Expose port 80
EXPOSE 80


