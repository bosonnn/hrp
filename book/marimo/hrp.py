import marimo

__generated_with = "0.11.2"
app = marimo.App()


@app.cell
def _(mo):
    mo.md(r"""# Demo pyhrp""")
    return


@app.cell
def _(__file__):
    from pathlib import Path

    data = Path(__file__).parent / "data"
    return Path, data


@app.cell
def _(data):
    import pandas as pd

    prices = pd.read_csv(data / "stock_prices.csv", index_col=0)
    returns = prices.pct_change().dropna(axis=0, how="all").fillna(0.0)
    return pd, prices, returns


@app.cell
def _(returns):
    cor = returns.corr().values
    cov = returns.cov()
    return cor, cov


@app.cell
def _(cor):
    # The implementation by Marcos Lopez de Prado is based on the 'single' metric
    from pyhrp.hrp import Dendrogram

    dendrogram_before = Dendrogram.build(cor, method="single")
    dendrogram_before.plot()
    return Dendrogram, dendrogram_before


@app.cell
def _(Dendrogram, cor):
    # The dendrogram suffers because of the 'chaining' effect. LdP is using
    # now only the order of the leaves (e.g. the assets) and
    # constructs a second Dendrogram.
    dendrogram_bisection = Dendrogram.build(cor, method="single", bisection=True)
    dendrogram_bisection.linkage
    return (dendrogram_bisection,)


@app.cell
def _(dendrogram_bisection):
    dendrogram_bisection.plot()
    return


@app.cell
def _():
    import marimo as mo

    return (mo,)


if __name__ == "__main__":
    app.run()
