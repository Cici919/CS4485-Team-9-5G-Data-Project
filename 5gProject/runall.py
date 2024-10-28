import os

def main():
    # Command to start Docker Compose services
    os.system('docker-compose up --build')

if __name__ == '__main__':
    main()
