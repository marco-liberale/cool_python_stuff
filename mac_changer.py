import os
# very basic mac address changer made by Marco Liberale
# I cannot be held responsible if this tool is used maliciously.
# human made code
# AI generated comments with Machinet AI (GPT-4 based)

# Check if the script is run as root
if os.geteuid() != 0:
    print("This script must be run as root!")
    exit(1)
else:
    print("Script is running as root.")

# Print a basic message
print("marco's basic MAC changer\n enjoy :)")

# Get the MAC address from the user
mac = input("Enter MAC address\n")

# Get the network interface from the user
inter = input("Enter interface\n")

# Bring the network interface down
os.system("sudo ifconfig " + inter + " down")

# Change the MAC address of the network interface
os.system("sudo ifconfig " + inter + " hw ether " + mac)

# Bring the network interface back up
os.system("sudo ifconfig " + inter + " up")

# Display the current configuration of the network interface
os.system("sudo ifconfig " + inter)

# Print a success message
print("MAC changed :)")
