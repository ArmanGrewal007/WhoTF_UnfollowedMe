import socket
import time

def is_internet_available():
    try:
        # Attempt to resolve a hostname to verify internet connectivity
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        # Log the absence of an internet connection to a logfile (creates if not exists)
        with open('internet_connection.log', 'a') as file:
            file.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] No internet connection detected.\n")
        return False
    

# Main script execution

