{ pkgs ? import <nixpkgs> { } }:

pkgs.mkShell
{
  nativeBuildInputs = [
    pkgs.trashy
    pkgs.python312
    pkgs.python312Packages.pip
    pkgs.python312Packages.virtualenv
    pkgs.ghidra-bin
    pkgs.gdb
    pkgs.wine-wayland
  ];
  
  shellHook = ''
    source .venv/bin/activate
    alias rm="trash -c always put"
  '';
}
