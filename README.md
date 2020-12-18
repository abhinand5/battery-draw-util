# Battery Draw Util

CLI Utility to display real-time battery discharge rates in Debian derivatives (originally meant to be used in KDE Plasma's "Command Output widget" to display battery draw)   

![Sample Image](sample/sample.png)

> Open to acceptting Pull Requests

## Usage 

### Provided Binary

Run the shell script to set up the utility. 

```bash
$ chmod +x setup.sh
$ ./setup.sh
```

### Compiling yourself

You can use `pyinstaller` to compile the python script into a binary.

```bash
$ pip install pyinstaller # if you don't already have it installed
$ pyinstaller --onefile main.py --name bat-draw
$ chmod +x setup.sh # now set up the binary
$ ./setup.sh
```

### Testing the CLI

After setting up the binary. Test in your terminal if the command below is working without any errors.

```bash
$ bat-draw --help
Usage: bat-draw [OPTIONS]

Options:
  -m, --mode TEXT   Modes - [normal, short]
  -f, --field TEXT  Fields - [draw, tte]
  -a, --all         Displays all fields
  --help            Show this message and exit.
```

The tool can be used in two different modes. It shows two fields, user can choose what to show using the next two flags. 

> If you have plugged in your device it will not show any output. 

Below is an example of `normal` mode for all fields.

```
$ bat-draw -m normal -a
Btr-Draw: 4.322 W - 10.0 hours left
```

Below is an example of `short` mode for all fields.

```
$ bat-draw -m short -a
4.322 W - 10.0h
```

The output shows your current battery draw followed by estimated time it will last. 

### Using it as KDE Widget

1. First you have to install the [Command Output Widget for KDE](https://store.kde.org/p/1166510/).

2. Add the widget to your panel by right clicking on it and choosing `"Add Widgets"` option. 

3. Drag the widget and drop it where ever you need on the panel

4. Right-click on the widget you just added and paste the bat-draw commands seen above, do whatever customizations you like, apply and save. 

You must be able to see something similar to this in your KDE panel. 

![Sample Image](sample/sample.png)