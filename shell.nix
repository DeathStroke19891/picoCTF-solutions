{ pkgs ? import <nixpkgs> { } }:

pkgs.mkShell
{
  nativeBuildInputs = [
    pkgs.trashy
    pkgs.python312
    pkgs.python312Packages.pip
    pkgs.python312Packages.virtualenv
    nodejs_22
  ];
  
  shellHook = ''
    source env/bin/activate
    alias rm="trash -c always put"
  '';
}
