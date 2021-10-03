{ pkgs ? import <nixpkgs> { } }:
let 
  myscript = pkgs.writeScriptBin "" ''MyProjectForSkikulix
    echo "ETS & ArcGIS" | figlet;
    echo "Sikulix shell ready"
  '';
in pkgs.mkShell {
    name = "MyProjectForSkikulix";
    buildInputs = with pkgs; [
        figlet
        myscript
        # openjdk11
        # opencv
        tesseract
        wmctrl
        xdotool

    ];

    shellHook = ''
      echo "welcome to my awesome shell";
    '';
}

