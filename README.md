# Autonomous Driving Methods for the Nvidia Jetson Nano

## Brief

Honestly I am just bored. This repo contains some of my favourite algorithms that I can use for self-driving and assisted driving using an Nvidia Jetson Nano.

I chose to write in Python for several reasons:
1. Its super simple and anyone can make alterations to it
2. Most cars don't travel at 100+kph, so speed is not always an issue
3. Its a language I know and am proficient in

I will eventually use C/C++ for actual implementation for this, and may use a version of [CommaAI OpenPilot](https://github.com/commaai/openpilot) for an actual real-world implementation.

## Further ideas

I'm kinda interested outside the realm of self-driving cars and more to the implementation with modern autonomous robotics. Robots are inherently quite bad at planning their environments, and exercises such as the [DARPA Subterranean Challenge](https://www.subtchallenge.com/) have highlighted how robots can be used for complex traversal in semi-permissive domains. Whilst my PhD is in robotics for manufacturing (specifically aerospace), my endgame is to transfer my specialty into robotics and trajectory planning in the real world.

Overall, this is a project. It won't be the best, it won't be the fastest and it sure as shit won't be the optimal solution. But it will be a solution everyone can use, on a variety of different hardware platforms in a variety of different vehicles.

## Support Hardware

I aim to allow the models and algorithms used in this project to work on a variety of different hardware specifications for embedded systems. I'm starting with the [Nvidia Jetson Nano](https://developer.nvidia.com/embedded/jetson-nano-developer-kit) as its pretty powerful and has GPU hardware acceleration. I'll move on to the [Raspberry Pi](https://www.raspberrypi.org/products/raspberry-pi-4-model-b/) once I'm confident the code works in C/C++.

- [] Computer System
- [] Nvidia Jetson Nano
- [] Raspberry Pi
