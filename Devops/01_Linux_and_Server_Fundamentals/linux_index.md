# Linux Terminal in depth
- What is Linux
- Distributions (Ubuntu, Debian, CentOS)
- CLI vs GUI
- Terminals, Consoles, Shells and Commands
- Linux Command Structure
- Getting Help, Man Pages (man, type, help, apropos)
- Commands - Getting Help
- Mastering the Terminal: The TAB Key
- Mastering the Terminal: Keyboard Shortcuts
- Commands - Keyboard Shortcuts
- Mastering the Terminal: The Bash History
- Running Commands Without Leaving a Trace
- Recording the Date and Time for Each Line in History
- Commands - The Bash History
- root vs. Non-privileged Users. Getting root Access (sudo, su, passwd)
- Commands - Getting root access
- Linux Terminal Challange

# Linux Files System
- Intro to The Linux Files System
- The Filesystem Hierarchy Standard (FHS)
- Absolute vs. Relative Paths. Walking through the File System (pwd, cd, tree)
- Commands - Paths
- The LS Command In Depth (ls)
- Commands - ls
- Understanding File Timestamps: atime, mtime, ctime (stat, touch, date)
- Sorting Files by Timestamp
- File Types in Linux (ls -F, file)
- Commands - File Types and Timestamps
- Viewing Files - Part 1 (cat)
- Viewing Files - Part 2 (less)
- Viewing Files - Part 3 (tail, head, watch)
- Commands - Viewing Files
- Creating Files and Directories (touch, mkdir)
- Copying Files and Directories (cp)
- Moving and Renaming Files and Directories (mv)
- Removing Files and Directories (rm, shred)
- Commands - touch, mkdir, cp, mv, rm, shred
- Working With Pipes in Linux (|, wc)
- Command Redirection (>, >>, 2> &>, cut, tee)
- Commands - Piping and Redirection
- Finding Files and Directories - Part 1 (which, plocate)
- Commands - plocate, find
- Finding Files and Directories - Part 2 (find)
- Find and Exec
- Searching for String Patterns in Text Files (grep)
- Commands - grep
- Searching for Strings in Binary Files (strings)
- Comparing Files (cmp, diff, sha256)
- The Basics of VIM Text Editor
- The VIM Editor In Depth - Part 1
- The VIM Editor In Depth - Part 2
- Commands - VIM
- Compressing and Archiving Files and Directories (tar, gzip)
- Hard Links and the Inode Structure
- Working With Symlinks. Symlinks vs. Hard Links
- Linux File System Challange

# Mastering sed and Regex in Linux
- Automating Text Editing with sed (Stream Editor)
- Real-World sed Use Case — Configuring sshd_config Automatically
- Diving into Regular Expressions
- Advanced sed and Regex Techniques for Sysadmins

# User Account Management
- Understanding passwd and shadow files
- Understanding Linux Groups (groups, id)
- Creating User Accounts (useradd)
- Changing and Removing User Accounts (usermod, userdel)
- Creating Admin Users
- Group Management (groupadd, groupdel, groupmod)
- User Account Monitoring (whoami, who am i, who, id, w, uptime, last)
- Commands - Account Management
- User Account Management Challange

# Linux File Permissions
- Understanding File Permissions
- Octal (Numeric) Notation of File Permissions
- Changing File Permissions (chmod)
- The Effect of Permissions on Directories
- Combining Find and Chmod Commands Together
- Changing File Ownership (chown, chgrp)
- Understanding SUID (Set User ID)
- Understanding SGID (Set Group ID)
- Understanding the Sticky Bit
- Umask
- Understanding Files Attributes (lsattr, chattr)
- Commands - File Permissions
- Linux File Permissions Challange

# Linux Processes Management
- Processes and The Linux Security Model
- Listing Processes (ps, pstree)
- Commands - ps, pstree, pgrep
- Getting a Dynamic Real-Time View of the Running System (top, htop)
- Commands - top
- Signals and Killing Processes (kill, pkill, killall, pidof)
- Foreground and Background Processes
- Job Control (jobs, fg, bg)
- Commands - kill, pkill, killall, jobs, fg, bg, nohup
- Linux Processes Management Challange

# Networking in Linux
- Getting Information about the Network Interfaces (ip, ifconfig)
- Configuring the Network On The Fly (ifconfig, ip, route)
- Commands - ifconfig, ip, route
- Setting Up Static IP on Ubuntu (netplan)
- Commands - netplan
- Testing and Troubleshooting Network Connectivity
- Using SSH
- Troubleshooting SSH
- Securing the OpenSSH Server (sshd)
- Commands - SSH
- Copying Files Over the Network (scp)
- Synchronizing Files and Directories using rsync
- Using rsync Over the Network
- Commands - scp, rsync
- Using wget
- Checking for Listening Ports (netstat, ss, lsof, telnet, nmap)
- Commands - wget, netstat, ss, nmap

# Software Management in Linux
- DPKG (Debian and Ubuntu Based Distros)
- Intro to APT
- Using APT (Advanced Package Tool)
- Commands - dpkg, apt
- Compiling Programs from Source Code vs. Package Manager
- Compiling C Programs
- Compiling Software From Source Code: Lab ProFTPD

# Containerization Application with podman
- Introduction to Podman
- Getting Started with Podman
- Running an Nginx Server on Alpine in a Podman Container
- Diving into Pods: A Real-World Example
- Monitoring Pods and Containers
- Ensuring Data Persistence with Volumes

# System Administration
- Task Automation and Scheduling Using Cron (crontab)
- Commands - Cron
- Scheduling Tasks Using Anacron (anacron)
- Mounting and Unmounting File Systems (df, mount, umount, fdisk, gparted)
- Working With Device Files (dd)
- Getting System Hardware Information (lwhw, lscpu, lsusb, lspci,dmidecode,hdparm)
- Commands - Getting Hardware Information
- Intro to systemd
- Service Management (systemd and systemctl)
- Commands - systemd, systemctl

# Configuration of Linux Server From scratch
- Overview: The Big Picture
- Running a Linux Server in the Cloud
- Securing SSH with Key Authentication
- Getting a Domain Name
- Diving into the DNS Protocol and Installing a DNS Server (Bind9)
- Setting Up the Authoritative BIND9 DNS Server
- Installing a Web Server (Apache2)
- Setting Up Virtual Hosting
- Securing Apache with OpenSSL and Digital Certificates
- Installing PHP
- Installing and Securing the MySql Server
- Installing a Web Application (WordPress)
- Securing WordPress

# Bash Shell Scripting
- Bash Aliases
- Commands - Aliases
- Intro to Bash Shell Scripting
- The Bash Shebang and Comments
- Running Scripts
- Variables in Bash
- Environment Variables
- Getting User Input
- Special Variables and Positional Arguments
- Coding - Variables in Bash
- If, Elif and Else Statements
- Testing Conditions For Numbers
- Multiple Conditions and Nested If Statements
- Command Substitution
- Comparing Strings in If Statements
- Lab: Testing Network Connections
- Coding - If...Elif...Else Statements
- For Loops
- Lab: Dropping a List of IP addresses Using a For Loop
- While Loops
- Case Statement
- Functions in Bash
- Variable Scope in Functions
- Menus in Bash. The Select Statement
- Lab: System Administration Script using Menus
- Intro to Bash Arrays
- Arrays In Depth
- Using the Readarray Command
- Iterating Over Arrays
- Project: Account Creation
- Running a DoS Attack Without root Access (ulimit)