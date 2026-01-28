# INF3995-Templates

Welcome To INF3995. This repo contains all the base templates you will need for this semester's project!

## Dev environment

We will be using Ubuntu 22.04 as a base environment for the project. There are many way to get am Ubuntu environment 
(WSL, Docker images, VMs, Dual booting, ect). Will will always try to help you to the best of our knowledge. However, we will only support two type of installation: A dual boot Ubuntu and a docker container with/without a VNC server.

The installation instructions are provided in the [Installation](Installation) folder

**Note:** This repository also includes a dev container configuration in the `.devcontainer` folder for VS Code users who prefer using Dev Containers.

## Running the base simulation

Since we are using ROS2 and gazebo harmonic, we will be providing you a modified version of the [proposed template](https://github.com/gazebosim/ros_gz_project_template/tree/fortress) that already includes the limo model. The template workspace is available in the [project_ws](project_ws) folder. We recommend you use this folder as a base for your project as it already comes with a lot of utilities that can be modified for your project.


## AI API usage

You can see example of how to use the AI API in the [ai_examples](ai_examples) folder. Their is two API. The first one is for image detection (bounding box) and the second one is for the LLM. You can test both with the default API key (rate limited). If you use those API, ask your TA for a specific API key.

**URLs:**
- API: https://inf3995.share.zrok.io
- Docs: https://inf3995.share.zrok.io/docs
- Health: https://inf3995.share.zrok.io/health

---