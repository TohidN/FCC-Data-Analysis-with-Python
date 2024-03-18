import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', sep=',', parse_dates=['date'])
df = df.set_index('date')

# Clean data
df = df.loc[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(12,8))
    plt.plot(df, label='lineplots', linewidth=1.0)
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()

    # Draw bar plot
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month
    print(df_bar)

    month_names = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July'
                , 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
    months = list(month_names.values())
    
    mapping = {month: i for i, month in enumerate(months)}
    key = df_bar['month'].map(mapping)
    df_bar.iloc[key.argsort()]


    df_bar['month'] = pd.Categorical(df_bar['month'].apply(lambda x: month_names[x]), categories=months, ordered=True)
    df_bar = df_bar.sort_values('month').groupby(['year', 'month'], as_index=False).mean()


    fig, ax = plt.subplots(figsize=(12, 8))
    sns.barplot(x="year", y="value", hue="month", data=df_bar, ax=ax, palette="cool")  # Pass ax directly to sns.barplot
    ax.set_xlabel("Years")  # Use descriptive variable name
    ax.set_ylabel("Average Page Views")  # Consistent capitalization
    plt.legend(title="Months", loc="upper left")  # Maintain legend placement


    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig
draw_bar_plot()

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, ax = plt.subplots(1, 2, figsize=(12, 8))

    # Yearly boxplot
    sns.boxplot(data=df_box, x="year", y="value", ax=ax[0])
    ax[0].set_title("Year-wise Box Plot (Trend)")
    ax[0].set_xlabel("Year")
    ax[0].set_ylabel("Page Views")

    # Monthly boxplot
    month_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    sns.boxplot(data=df_box, x="month", y="value", order=month_order, ax=ax[1])
    ax[1].set_title("Month-wise Box Plot (Seasonality)")
    ax[1].set_xlabel("Month")
    ax[1].set_ylabel("Page Views")
    
    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig