import click
import subprocess


def get_command(field):
    """Helper Function to create Popen command to fetch the given field

    Args:
        field (str): The output field to fetch from upower output
    """
    cmd = subprocess.Popen(
        f"upower -i $(upower -e | grep 'BAT') | grep \"{field}\"",
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    return cmd


def get_output(field):
    """Helper Function to execute the command and extract the output

    Args:
        field (str): The output field to fetch from upower output
    """
    cmd = get_command(field)
    out, _ = cmd.communicate()
    out = out.decode().split(":")[1].strip()

    return out


@click.command()
@click.option("-m", "--mode", help="Modes - [normal, short]")
@click.option("-f", "--field", help="Fields - [draw, tte]")
@click.option("-a", "--all", is_flag=True, help="Displays all fields")
def main(mode, field, all):
    """CLI Interface for displaying battery draw

    Args:
        mode (str): Output Modes - [normal, short]
        field (str): Fields to fetch- [draw, tte]
        all (str): Displays all fields
    """

    state = get_output("state")

    if state == "discharging":
        discharge_rate = get_output("energy-rate")
        tte = get_output("time to empty")

        if all and mode is None:
            print(f"Btr-Draw: {discharge_rate} - {tte} left")
        elif all and mode == "normal":
            print(f"Btr-Draw: {discharge_rate} - {tte} left")
        elif all and mode == "short":
            print(f"{discharge_rate} - {tte.split()[0]}h")
        elif field == "draw" and mode == "normal":
            print(f"Btr-Draw: {discharge_rate}")
        elif field == "draw" and mode == "short":
            print(f"{discharge_rate}")
        elif field == "tte" and mode == "normal":
            print(f"TTE: {tte}")
        elif field == "tte" and mode == "short":
            print(f"TTE: {tte.split()[0]}h")


if __name__ == "__main__":
    main()
