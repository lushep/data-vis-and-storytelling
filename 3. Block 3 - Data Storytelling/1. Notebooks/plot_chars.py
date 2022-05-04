import pandas as pd
import matplotlib.pyplot as plt

def plot_charts(**kinds):
    fig, axes = plt.subplots(2,3, figsize=(18,7))
    axes = [ax for sublist in axes for ax in sublist]

    for (file, kind), ax in zip(kinds.items(), axes):
        
        df = pd.read_csv(f"data/plots/{file}_plot.csv")

        x = df.columns[0]
        y = df.columns[1]
        df = df.set_index(x, drop=False)
        title = f"{x} vs {y}"
        
        if df.shape[1]>2 and kind not in ['pie', 'scatter']:
            y = list(df.columns[1:])
            title = f"{x} vs {y[0]} and {y[1]}"
        df.plot(x = x, y = y, ax=ax, kind=kind, title=title)
        plt.tight_layout()