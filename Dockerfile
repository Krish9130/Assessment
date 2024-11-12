# Use an official Apache HTTP Server image
FROM httpd:latest

# Copy a custom HTML file to the server's default directory
COPY ./index.html /usr/local/apache2/htdocs/

# Expose port 80
EXPOSE 80

# Start the NGINX web server in the foreground to prevent the container from exiting.
# The 'daemon off;' directive ensures NGINX runs in the foreground instead of as a background process.
CMD ["nginx", "-g", "daemon off;"]
