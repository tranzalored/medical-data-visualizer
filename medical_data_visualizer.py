import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
square_height=np.square(df['height']/100)
df['overweight']=(df['weight']/square_height)>25
df['overweight'].replace({False: 0, True: 1}, inplace=True)
df['overweight'] = df['overweight']

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholestorol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['cholesterol'].replace({1:0,2:1,3:1},inplace=True)
df['gluc'].replace({1:0,2:1,3:1},inplace=True)



# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars = ['cardio'], value_vars = ['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])


    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the collumns for the catplot to work correctly.
   # df_cat = None

    # Draw the catplot with 'sns.catplot()'
    fig = sns.catplot(data=df_cat, kind="count",  x="variable", hue="value", col="cardio")




    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat=df[(df['ap_lo'] <= df['ap_hi']) & (df['height'] >= df['height'].quantile(0.025)) & (df['height'] <= df['height'].quantile(0.975)) & (df['weight'] >= df['weight'].quantile(0.025)) & (df['weight'] <= df['weight'].quantile(0.975))]
    
    
    corr = round(df_heat.corr(),1)
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True

    # Generate a mask for the upper triangle
    with sns.axes_style("white"):
      fig, ax = plt.subplots(figsize=(9, 9))
      sns.heatmap(corr, mask=mask,annot=True, fmt='.1f', linewidths=1, vmax=.8, center=0.09,square=True, cbar_kws = {'shrink':0.5})




    # Set up the matplotlib figure
    #fig, ax = plt.subplots(figsize=(9,9))

    # Draw the heatmap with 'sns.heatmap()'
    #sns.heatmap(corr,annot=True, fmt='.1f', linewidths=1, mask=mask, #vmax=.8, center=0.09,square=True, cbar_kws = {'shrink':0.5})



    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
