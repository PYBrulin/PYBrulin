{ pkgs, ... }:

{
  languages.python = {
    enable = true;
    version = "3.10.10";
    venv = {
      enable = true;
      requirements = ''
        beautifulsoup4
      '';
    };
  };
}
