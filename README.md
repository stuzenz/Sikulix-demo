# ETS & ArcGIS Test automation with Sikulix

This short demo project provides an overview of how Sikulix can be used to automate across any application that uses the screen, keyboard and mouse.

# Dependencies

For this environment setup, I have chosen to use NixOS as the host, this allows for fully reproducible and declaratively setup environments per project, per system and per user. This project set up is defined in the nix.shell file

The NixOS package manager is installable on Linux or MacOS - and can provide the same capability to declaratively set up your environment in Linux or MacOS environments.

Even when using NixOS, due to github file size limitations, I have not included the following file

`sikulixide-2.0.5-lux.jar`

Please download it from here for the Linux version
`wget https://launchpad.net/sikuli/sikulix/2.0.5/+download/sikulixide-2.0.5-lux.jar`

If not using NixOS or the nix-shell capability, please follow the instructions at Sikulix

- [sikulix install instructions](https://sikulix.github.io/docs/start/installation)
- [sikulix](https://github.com/RaiMan/SikuliX1/wiki/About-actual-release-version)

# Building the executable jar files from scripts

From the Sikulix IDE,

`File menu` --> `Export as Runnable jar`

# Executing the scripts

When in the shell with the environment set up, run

`java -jar sikuli-scripts_sikuli.jar`

# Links

- [Latest documentation](https://sikulix.github.io/)
- [SikuliX Github project](https://github.com/RaiMan/SikuliX1)
- [Installation](https://sikulix.github.io/docs/start/installation)

# Other options

- [robotgo](https://github.com/go-vgo/robotgo)

    - Through looking for Sikulix which I had not used for a decade, I did come across this golang project which does something similar, but by looking at the API examples, it does not seem to be as fully featured as sikulix. Who knows though, it could be good. It is kind of understandable that it is not fully featured, as you would likely know, golang as a community has a philosophy of being very Linux like. In general, they don't build batteries included frameworks, you pull together your own needs from more 'one purpose' libraries and roll your own solutions up from there.

## Sikuli notes

The methods supporting the use of special keys are `type()`, `keyDown()`, and `keyUp()`.

### Key Modifiers

Methods where key modifiers can be used include: click(), dragDrop() , doubleClick() , rightClick(), type().

Use KeyModifier.CTRL, KeyModifier.ALT, KeyModifier.SHIFT, KeyModifier.META instead.