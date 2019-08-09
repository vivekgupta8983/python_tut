#!/bin/usr/python
import subprocess
import platform
import os
import sys
import copy
import urllib
import urllib2
import zipfile
import re
import shutil
import tarfile
import fileinput


def print_menu():
    print(30 * "-" , "MENU" , 30 * "-")
    print("1. Deploy for RedHat or CentOS Family")
    print("2. Deploy for Ubuntu or Debian Family")
    print("3. If you Don't Knowns")
    print("4. Configure MySQL")
    print("5. Install Wordpress")
    print("6. Configure your VitualHost")
    print("7. exit")
    print(67 * "-")


    def deploy_httpd():
        commands_to_run = ['yum', '-y', 'install', 'httpd', 'mariadb', 'mariadb-server', 'php', 'php-mysql', 'mod_ssl'],
        ['systemctl', 'start', 'httpd.service'], ['systemctl', 'enable', 'httpd.service'], ['systemctl', 'start', 'mariadb'],
        ['systemctl', 'enable', 'mariadb.service'], ['systemctl', 'restart', 'httpd.service']
    
        for x in commands_to_run:
            print(subprocess.check_output(x))

    def deploy_apache():
        commands_to_run = ['apt', '-y', 'install', 'apache2', 'mariadb', 'mariadb-server', 'php', 'php-mysql', 'libapache2-mod-php', 'php-mcrypt', 'php-rpcxml']
        ['systemctl', 'start', 'apache2'], ['systemctl', 'enable', 'apache2.service'], ['systemctl', 'start', 'mariadb'],
        ['systemctl', 'enable', 'mariadb.service'], ['systemctl', 'restart', 'apache2.service']

        for x in commands_to_run
        print(subprocess.check_output(x))
    
    def check_dist():
        tuple_platform = platform.dist()
        current_platform = tuple_platform[0]
        if "Ubuntu" in current_platform:
            print("ubuntu")
            deploy_apache()
        elif "CentOS" in current_platform:
            print("centos")
            deploy_httpd90
        elif "Redhat" in current_platform:
            print(Redhat)
            deploy_httpd()
    def mysql_server():
        DB_NAME = input("Enter Database Name:")
        DB_ROOT_PASSWORD = input("Enter Database Password:")
        """Install MySQL/MariaDB"""
            # add logging support
        if os.environ['DB_ROOT_PASSWORD'] != "":
            db_root_password = os.environ['DB_ROOT_PASSWORD']
        else:
            db_root_password = False
            
        if os.environ['DB_NAME'] != "":
            db_name = os.environ['DB_NAME']
        else:
            db_name = False

    def wordpress():
        os.system('wget https://wordpress.org/latest.tar.gz')
        tar = tarfile.open('latest.tar.gz') 
        tar.extractall('path=/var/www/html/') # untar file into same directory
        tar.close()
        os.chdir('/var/www/html/wordpress/')
        shutil.copy('cp wp-config-sample.php wp-config.php')
        


    loop=True
    while loop:
        print_menu()
        choice = input("Enter your choice [1-7]: ")
           
        if choice=='1':
            print("Deploy LAMP server on Redhat or CentOS Family, Selected")
        #Functions go here
            deploy_httpd()
        elif choice=='2':
            print("Deploy LAMP server on Ubuntu or Debian Family, Selected")
        #Functions go here
            deploy_apache()
        elif choice=='3':
            print("you Don't your Distributor we will help you")
                check_dist()
        elif choice == '4':
            print("Configure your MySQL Databases, Selected")
            mysql_server(db_root_password, db_name)
        elif choice == '5':
            print("Deploy wordpress")
            wordpress()
        elif choice == '6':
            print("Configure VitualHost")
            VitualHost()
            loop=False
        else:
            input("Wrong option selected. Enter any key to try again..")