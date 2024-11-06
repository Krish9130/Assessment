**###Devops - Technical Assessment**
1. Write an Ansible playbook to copy a file to multiple hosts.
Description: This Ansible playbook copies a specified file from your control node to multiple remote hosts. Ansible simplifies the process by using copy or synchronize modules.


---
- name: Copy a file to multiple hosts
  hosts: all
  become: yes
  tasks:
    - name: Copy a file to remote hosts
      ansible.builtin.copy:
        src: /path/to/local/file.txt
        dest: /path/to/remote/destination/file.txt
        owner: root
        group: root
        mode: '0644'



2. How to loop over a list in Ansible?
Description: In Ansible, you can loop over items using the with_items keyword or loop. Here’s an example that installs multiple packages.

---
- name: Install packages on remote hosts
  hosts: all
  become: yes
  tasks:
    - name: Install multiple packages
      ansible.builtin.yum:
        name: "{{ item }}"
        state: present
      loop:
        - git
        - nginx
        - vim


3.Explain the difference between append() and extend() methods for a list. Provide examples.

Explanation:
append(item): Adds item as a single element to the end of the list.
extend(iterable): Adds each element of an iterable (e.g., another list) to the end of the list.
Example:

# Using append
my_list = [1, 2, 3]
my_list.append([4, 5])
print(my_list)  # Output: [1, 2, 3, [4, 5]]

# Using extend
my_list = [1, 2, 3]
my_list.extend([4, 5])
print(my_list)  # Output: [1, 2, 3, 4, 5]


4. Write a Python program to sort a list of tuples based on the second element.
Description: Sort a list of tuples by the second element in each tuple.
# Sample list of tuples
my_list = [(1, 'apple'), (3, 'banana'), (2, 'cherry')]

# Sorting by the second element
sorted_list = sorted(my_list, key=lambda x: x[1])
print(sorted_list)





5. Write a Docker file to create an Apache server.
Description: This Dockerfile creates a containerized Apache server.
# Use an official Apache HTTP Server image
FROM httpd:latest

# Copy a custom HTML file to the server's default directory
COPY ./index.html /usr/local/apache2/htdocs/

# Expose port 80
EXPOSE 80




6. How do you list all running containers and How do you list all containers, including stopped ones?

Commands:
Running containers:


docker ps


All containers (including stopped):

docker ps -a


7. How to start and stop the container?
Commands:
Start a container:


docker start container_id_or_name


Stop a container:


docker stop container_id_or_name



8. How do you create an S3 bucket using AWS CLI?
Command:
aws s3 mb s3://my-bucket-name





9. SSH Command to Copy All Files from Local Directory to Remote Server
Command:
scp -r /path/to/local/directory/ user@remote_host:/path/to/remote/destination/

# For example
# scp -r /home/ubuntu/ ubuntu@25.54.34.211:/opt/


Explanation:
-r: Recursively copies all files and directories from the source.
user@remote_host: Specifies the user_name and remote server’s address or ip add.





10. View Running Processes and Check Memory Usage on a Linux System
Commands:
View running processes:
ps aux

or


top


Check memory usage:


free -h


