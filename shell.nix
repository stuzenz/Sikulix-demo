{ pkgs ? import <nixpkgs> { } }:
let 
  welcome = pkgs.writeScriptBin "ETS" ''
    echo "ETS & ArcGIS" | figlet;
  '';
in pkgs.mkShell {
    name = "MysikulixShell";
    buildInputs = with pkgs; [
        figlet
        welcome
        adoptopenjdk-bin # version 11
        wmctrl
        xdotool
        wget
        jython
        peek # screen recording

        # The following can probably can be refactored out
        # - according to 
        # https://github.com/RaiMan/SikuliX1/wiki/About-actual-release-version
        tesseract # OCR
        opencv # screen monitoring

        # required for Linux to stop a couple of small errors
        libcanberra-gtk3
        

    ];

    shellHook = ''
      clear
      ETS
      echo "Welcome to the Sikulix environment";
      echo """
      This shell was set up using declarative configuration
      using nix-shell and nix.flake to lock all packages

      The configuration is visible at nix.shell
      in this root project directory

      I have not included sikuli in this github project file due to file sizes, 
      if you have not already downloaded sikulixide

      wget https://launchpad.net/sikuli/sikulix/2.0.5/+download/sikulixide-2.0.5-lux.jar
      
      Run the following command to start the sikulix IDE
      
      java -jar sikulixide-2.0.5-lux.jar
            """
    '';
}
