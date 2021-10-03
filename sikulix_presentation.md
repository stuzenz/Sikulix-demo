---
title: BDD
separator: <!--s-->
verticalSeparator: <!--v-->
theme: blood
revealOptions:
transition: 'fade'
---

### A quick look into automation using Sikulix

Automation option using Sikulix with ArcGIS

_3 October 2021_

Stuart MacDonald, ETS PMO

---

### What is Sikulix

Originally came out of MIT Labs. 

The project was open sourced over 10 years ago


---
#### How I set up the environment

- Sikulix will work with Linux, MacOS and Windows
- For my set up, this demo github project has a nix.shell file
- The nix.shell file gives you a declarative environment build
- To use my set up you need to be using Linux or MacOS along with the nix package manager (which is open source from NixOS)

---
### Let's start the nix environment



---
#### Let's look at the code

- You can have the code run as a script or jar
- You can also use a normal IDE - versus the weird but useful IDE that comes with sikulix

---

#### What makes it good

- The API is very easy to use - I used the jython flavour of it;
- The test automation gives you reproducible test execution and the ability to add it into some of your regression testing;
- It only needs to watch for the screen change and manipulate the keyboard and screen;
- It is a maintained project with long term support in place for the OpenJDK that it runs on
---

### Let's run the demo

- The demo is pretty simple. 
- It barely touches the surface of the Sikulix API.

_The main point is that you can do anything that you can from the keyboard, mouse and screen_
---

### Let's build a jar out of of script and run it

---
#### That is the demo over with

With a little thinking and a little code, it is possible to run a number of different tests through the system while collecting performance metrics and other data while taking screenshots etc.

---
### Thanks

_If you have any questions, feel free to contact me_

_[Stuart MacDonald](stuart.macd@gmail.com)_

**Github - my demo:** [https://github.com/stuzenz/Sikulix-demo](https://github.com/stuzenz/Sikulix-demo)
**Sikulix - project site:** [https://sikulix.github.io/](https://sikulix.github.io/) 

