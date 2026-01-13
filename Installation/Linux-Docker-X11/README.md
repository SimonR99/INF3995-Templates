# Linux Docker with integrated graphics and no VNC

Since You will be installing a lot of packages and libraries on your system, it might be easier to nuke the dev environment instead of reinstalling your distro in case of a major problem. It also makes cleaning up after the course much easier.

## How to use:

First, build the Dockerfile with:
```bash
docker build -t "rosgzbase" ./
```

Finally run the image using docker:
```bash
docker run --rm -it --network=host --device=/dev/dri --env DISPLAY=$DISPLAY rosgzbase
gz sim
```

### Warning:
You may need to install additional packages to get your GPU to work. If you have a nvidia GPU, you can run the following 
command : 

```bash
# 1. Configure the production repository
curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
  && curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | \
  sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#' | \
  sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list

# 2. Install the toolkit
sudo apt-get update
sudo apt-get install -y nvidia-container-toolkit

# 3. Configure Docker to use it
sudo nvidia-ctk runtime configure --runtime=docker
sudo systemctl restart docker
```