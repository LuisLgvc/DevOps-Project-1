#!/usr/bin/env python3
import os
import subprocess

def deploy():
    print("Obtaining the code from the Git repository...")
    subprocess.run(["git", "pull"], check=True)
    print("Running tests (if any)...")
    # Unit tests would go here, if you had them
    print("Creating the application package...")
    # Logic to create a package (e.g., zip, tar) would go here
    print("Deploying the application...")
    # Simulate deployment by copying the file to a destination directory
    os.makedirs("destino", exist_ok=True)
    subprocess.run(["cp", "index.html", "destino/index.html"], check=True)
    print("Deployment completed in the 'destino' folder")

if __name__ == "__main__":
    deploy()
