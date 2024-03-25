#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 14:39:49 2024

@author: patrick.woods
"""

import pandas as pd

def mean_counts(input_file, rxn_norm = False):
    '''
    Takes input dataframe .csv file with colony counts from any number of 
    powdery mildew races, calculates the mean colony counts per genotype per race and 
    returns a dataframe object with calculations.

    Parameters
    ----------
    data : pandas.core.frame.DataFrame
        A .csv file containing the plant genotype and colony count information 
        for the multiple races of powdery mildew.
    rxn_norm : boolean
        Boolean argument that defaults to False. If False, the function will 
        return a dataframe containing the overall mean colony counts across all 
        dishes for each Identifier x Mildew Race combination. If True, the function will 
        return a datafarme in which only within dish colony counts are averaged. 
    The returned dataframe is ideal for plotting a reaction norm.
    Returns
    -------
    A single dataframe with either mean colony counts per IdentifierxMildew 
    combination OR a single dataframe with mean colony counts per Dish per 
    IdentifierxMildew combination.

    '''
    import pandas as pd

    print('Reading in ' + input_file + ' for analyses...')
    
    file = pd.read_csv(input_file)
    
    ### Calculate the mean depending on user specifications ###
    if rxn_norm == False:
        print('Calculating Mean Colony Counts per Identifer x Mildew Combination...')
        mean_by_race_mildew = file.groupby(['Identifier', 'Mildew'])[['Colony count']].mean()
        mean_by_race_mildew_pd = pd.DataFrame(mean_by_race_mildew)
        
        print('Done!')
        return mean_by_race_mildew_pd
    else:
        print('Calculating Mean Colony Counts for Each Dish x Identifier x Mildew Race Combination...')
        mean_by_dish_race_mildew = file.groupby(['Identifier','Dish','Mildew'])['Colony count'].mean()
        mean_by_dish_race_mildew_pd = pd.DataFrame(mean_by_dish_race_mildew)
        mean_by_dish_race_mildew_pd = mean_by_dish_race_mildew_pd.reset_index()
        
        print('Done!')
        return mean_by_dish_race_mildew_pd






