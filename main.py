import pandas as pd
import plotly.express as px

# Read the CSV file
df = pd.read_csv('data/sunspots_monthly_mean.csv', sep=';', header=None)
# Assign column names
df.columns = [
    'Year', 'Month', 'Fractional_Year', 
    'Monthly_Mean_Sunspot_Number', 'Monthly_Mean_Standard_Deviation', 
    'Number_of_Observations', 'Definitive_Indicator'
]

# Remove missing sunspot numbers (-1) (0)
df = df[(df['Monthly_Mean_Sunspot_Number']!=-1) & (df['Monthly_Mean_Sunspot_Number']!=0)]
# Combine Year, Month, and Day into a datetime column
df['Date'] = pd.to_datetime(df[['Year', 'Month']].assign(day=1))

# Create the interactive plot using Plotly
fig = px.line(df, x='Date', y='Monthly_Mean_Sunspot_Number', 
              title='Monthly Sunspot Number Over Time',
              labels={'Monthly_Mean_Sunspot_Number': 'Number of Sunspots', 'Date': 'Date'})

# Customize the layout to include a range slider and buttons
fig.update_layout(
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=1, label="1y", step="year", stepmode="backward"),
                dict(count=5, label="5y", step="year", stepmode="backward"),
                dict(count=10, label="10y", step="year", stepmode="backward"),
                dict(step="all")
            ])
        ),
        rangeslider=dict(visible=True),
        type="date"
    )
)

# Show the plot
fig.show()
