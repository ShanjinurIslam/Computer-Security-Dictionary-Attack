If you do not know know root password :

Reset password by following this link:

https://websiteforstudents.com/resetting-mysql-root-password-on-ubuntu-16-04-17-10-and-18-04-lts/

To install phpmyadmin, follow this link:

https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-phpmyadmin-on-ubuntu-16-04


First Create MySQL Database Name : mywebsite

CREATE TABLE users (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

Paste the server codes to /var/www/html/ folder

In Terminal write :

sudo service apache2 start (If it is not started already)

To check status of apache2 Web Server
sudo service apache2 status

visit http://localhost/index.php and rest are demonstrated in this youtube link



Credits: https://www.tutorialrepublic.com/php-tutorial/php-mysql-login-system.php For Server Codes
