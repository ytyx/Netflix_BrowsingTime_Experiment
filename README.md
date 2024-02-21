# Netflix_BrowsingTime_Experiment

This project aims to optimize the user experience on Netflix's homepage by reducing browsing time. Using a 2k 
factorial experimental design, we analyzed interaction plots and p-values to identify key factors affecting 
browsing duration, supplemented by Response Surface Methodology for informed decision-making. Optimal 
settings were determined to be a Preview Length of 75 seconds and a Match Score of 75%, alongside the 
default Preview Type 'TT' and Tile Size of 0.2. This configuration resulted in a marked decrease in browsing 
time, with an optimal average of 9.9 minutes.

### Experiments
- Screening Experiment using a 2k factorial design: to identify the factors significantly influencing browsing duration
- Additional 3x3 factorial design: Find the most efficient Match Score and Preview Length combination to minimize browsing time. 
- Response Surface Methodology: The model employs Taylor’s Theorem to form a secondary model, considering main effects, 
interaction and quadratic effects of the two factors to approximate minimum browsing time.
