# Devops - Technical Assessment
### 1. Write an Ansible playbook to copy a file to multiple hosts.
Description: This Ansible playbook copies a specified file from your control node to multiple remote hosts. Ansible simplifies the process by using copy or synchronize modules.

##### https://github.com/Krish9130/Assessment/blob/main/copy_file_to_hosts.yml


### 2. How to loop over a list in Ansible?
Description: In Ansible, you can loop over items using the with_items keyword or loop. Here’s an example that installs multiple packages.

##### https://github.com/Krish9130/Assessment/blob/main/copy_file_to_hosts.yml


### 3.Explain the difference between append() and extend() methods for a list. Provide examples.

Explanation:
append(item): Adds item as a single element to the end of the list.
extend(iterable): Adds each element of an iterable (e.g., another list) to the end of the list.
Example:

##### https://github.com/Krish9130/Assessment/blob/main/append_extend.py


### 4. Write a Python program to sort a list of tuples based on the second element.
Description: Sort a list of tuples by the second element in each tuple.

##### https://github.com/Krish9130/Assessment/blob/main/sort_tuple_inlist.py


### 5. Write a Docker file to create an Apache server.
Description: This Dockerfile creates a containerized Apache server.

##### https://github.com/Krish9130/Assessment/blob/main/Dockerfile



### 6. How do you list all running containers and How do you list all containers, including stopped ones?

Commands:
Running containers:

     $ docker ps

All containers (including stopped):

     $ docker ps -a


### 7. How to start and stop the container?
Commands:
Start a container:

     $ docker start <container_id_or_name>

Stop a container:

     $ docker stop <container_id_or_name>



### 8. How do you create an S3 bucket using AWS CLI
Ensure you have set up your AWS credentials using the aws configure command, which will store your access key, secret key, region, and output format.

     $ aws configure

Command:

     $ aws s3 mb s3://my-bucket-name




### Q9. SSH Command to Copy All Files from Local Directory to Remote Server
Command:

     $ scp -r /path/to/local/directory/ user@remote_host:/path/to/remote/destination/

#For example

#scp -r /home/ubuntu/ ubuntu@25.54.34.211:/opt/


Explanation:
**-r:** Recursively copies all files and directories from the source.

**/path/to/local/directory/:** means source directory or master ec2 instance path

**user@remote_host:** Specifies the user_name and remote server’s address or ip add

**/path/to/remote/destination/ :** destination path or node ec2 instance path




### Q10. View Running Processes and Check Memory Usage on a Linux System
Commands:
View running processes:

     $ ps aux
  
  or 
  
     $ top


Check memory usage:

     $ free -h

