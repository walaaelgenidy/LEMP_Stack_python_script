import urllib
import tarfile
import os

os.system("sudo apt install nginx -y ")
os.system("sudo systemctl restart nginx ")
os.system("sudo systemctl enable nginx")
print("installing nginx comlpleted")


os.system("sudo apt update -y")
os.system("sudo apt install mysql -y")
os.system("sudo apt install mysql-server -y")
os.system("sudo mysql_secure_installation")
os.system("systemctl restart mysqld")
os.system("sudo mysql -u root ")

#install php php-fpm
os.system("sudo apt install php-fpm php-mysql  -y ")
print("installing php and php-fpm comlpleted")

#Configuring Nginx to Use PHP
os.system("sudo touch /etc/nginx/conf.d/mysite.conf")
os.system("cd /etc/nginx/conf.d")
fconf = open("/etc/nginx/conf.d/mysite.conf", "w")
fconf.writelines(
                "server { \n"  
                "listen 80; \n" 
                "listen [::]:80; \n" 
                "root /var/www/html/mysite; \n" 
                "index  index.php index.html index.htm; \n"
                "server_name 3.138.246.122 ; \n" 
                "location / { \n" 
                "       try_files $uri $uri/ /index.php?$args; \n" 
                " } \n" 
                " location ~ \.php$ { \n" 
                    " include snippets/fastcgi-php.conf; \n" 
                    " fastcgi_pass unix:/run/php/php7.4-fpm.sock; \n" 
                        "fastcgi_param   SCRIPT_FILENAME $document_root$fastcgi_script_name; \n" 
                " } \n"
               " } \n"
                )
fconf.close()


print("installing mysql comlpleted")


#  download latest wordpress version
os.system("wget -c http://wordpress.org/latest.tar.gz")
os.system("tar -xzvf latest.tar.gz")

#change ownership and permissions 
os.system("sudo cp -R wordpress/ /var/www/html/mysite")
os.system("sudo chown -R www-data:www-data /var/www/html/mysite" )
os.system("chmod -R 755 /var/www/html/mysite")
print("installing wordpress comlpleted")

#Configuring wordpress 
os.system("cd /var/www/html/mysite")
os.system("sudo mv wp-config-sample.php wp-config.php")
print("copy this command and edit the file with your configuration $$ sudo vim wp-config.php")


os.system("sudo rm /etc/nginx/sites-enabled/default")
os.system("sudo rm /etc/nginx/sites-available/default ")
os.system("sudo nginx -t ")
os.system("sudo systemctl restart nginx")
