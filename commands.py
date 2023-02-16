"""
Commands module [commands]
Provides cli commands for interacting with Meathead Math.
"""
import click

# called in main.py so needs to be lib.mhm
import lib.mhm as mhm
import lib.vis as vis
import lib.filemanager as fm


@click.group()
def cli():
    pass


@click.command()
@click.option("-r", prompt="Reps", type=float, help="Number of reps")
@click.option("-w", prompt="Weight", type=float, help="Weight used")
def est_max(r, w):
    """Using reps and weight estimate one rep max."""
    max = int(mhm.one_rep_max(r, w))
    click.echo(f"Estimated One Rep Max => {max}")


@click.command()
@click.option("-r", prompt="Reps", type=float, help="Number of reps")
@click.option("-w", prompt="Weight", type=float, help="Weight used")
@click.option("-rm", prompt="One Rep Max", type=float, help="One Rep Max")
def rel_int(r, w, rm):
    """Using reps, weight, & one rep max determine relative intensity"""
    ai, ri = map(lambda x: x * 100, mhm.relative_intensity(r, w, rm))
    click.echo(f"Relative Intensity => {ri}%.")
    click.echo(f"Absolute Intensity => {ai}%.")


@click.command()
@click.option("-r", prompt="Reps", type=int, help="Number of reps")
@click.option(
    "-ri",
    prompt="Relative Intesity",
    type=float,
    help="Desired relative intensity at given rep range.",
)
def new_ri(r, ri):
    """Calculate absolute intensity for desired relative intensity at a rep range."""
    ai = mhm.increased_ai(r, ri)
    click.echo(f"Estimated Absolute Intensity => {ai * 100}%")


@click.command()
@click.option("-n", prompt="Name", type=str, help="Name of lift")
@click.option(
    "-rm", prompt="One Rep Max", type=float, help="One Rep Max for given lift"
)
def show_lift_graph(n, rm):
    """Create a graph of relative intensity and volume over time for a lift."""
    res = vis.show_bar_charts(n, rm)
    if res == "":
        click.echo(f"{n} graph rendering...")
    else:
        click.echo(res)


@click.command()
@click.option("-n", prompt="Name", type=str, help="Name of lift")
def new_lift(n):
    """Create a new csv for the given lift name."""
    res = fm.create_lift(n)
    if res == "":
        click.echo(f"{n}.csv created")
    else:
        click.echo(res)


"""add commands"""
cli.add_command(est_max)
cli.add_command(rel_int)
cli.add_command(new_ri)
cli.add_command(new_lift)
cli.add_command(show_lift_graph)
