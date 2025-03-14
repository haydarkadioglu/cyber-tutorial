### Basic Linux Commands for Termux

**File and Directory Operations**
- `pwd` - Shows the current directory.
- `ls` - Lists files and folders in the current directory.
  - `ls -a` - Shows hidden files.
  - `ls -l` - Lists with detailed information.
- `cd directory_name` - Changes directory to the specified one.
- `cd ..` - Moves up one directory.
- `mkdir directory_name` - Creates a new directory.
- `rmdir directory_name` - Deletes an empty directory.
- `rm file_name` - Removes a file.
  - `rm -r directory_name` - Removes a directory and its contents.
- `cp source_file destination` - Copies files.
- `mv old_name new_name` - Moves or renames files.

**Viewing File Contents**
- `cat file_name` - Displays the contents of a file.
- `less file_name` - Views file contents page by page.
- `head file_name` - Shows the first 10 lines of a file.
- `tail file_name` - Shows the last 10 lines of a file.

**Text Editing**
- `nano file_name` - Opens a basic text editor.
- `vim file_name` - Opens a powerful text editor.

**Package Management**
- `pkg update` - Updates the package list.
- `pkg upgrade` - Upgrades installed packages.
- `pkg install package_name` - Installs a new package.
- `pkg uninstall package_name` - Uninstalls a package.
- `pkg list-all` - Lists all available packages.

**Downloading Files**
- `wget URL` - Downloads a file from the specified URL.
- `curl URL -o file_name` - Downloads a file from a URL with a specified name.

**System Information**
- `uname -a` - Displays system information.
- `df -h` - Shows disk usage.
- `free -h` - Displays RAM usage.
- `top` - Shows running processes.
- `htop` - Shows detailed running processes.

**Search Operations**
- `find . -name file_name` - Searches for a file in the current and subdirectories.
- `grep pattern file_name` - Searches for a specific pattern inside a file.

**File Permissions and User Operations**
- `chmod permission_code file_name` - Changes file or directory permissions.
- `chmod +x file_name` - Makes a file executable.
- `whoami` - Displays the current user name.
- `passwd` - Changes user password.

**Network Operations**
- `ping domain.com` - Tests connection by pinging a domain.
- `ifconfig` - Displays network settings and IP addresses.
- `curl ifconfig.me` - Displays your public IP address.

**Compressing and Extracting Files**
- `tar -czvf file.tar.gz directory_name` - Compresses a directory.
- `tar -xzvf file.tar.gz` - Extracts a compressed file.
- `zip file.zip file_name` - Compresses files into a zip.
- `unzip file.zip` - Extracts zip files.

**System Shutdown and Restart (root permissions might be required)**
- `shutdown` - Shuts down the system.
- `reboot` - Restarts the system.

These commands will help enhance your Linux experience on Termux and facilitate efficient usage.

