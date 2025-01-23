# Netflix Browsing Time Optimization Experiment  

This repository documents an experiment conducted to optimize Netflix's homepage configuration, with the goal of reducing user browsing time while improving decision-making efficiency. The project utilized advanced statistical methods, A/B testing, and visualization techniques to deliver actionable insights.

---

## Project Overview

The primary objective of this project was to identify the optimal design configurations for Netflix's homepage to enhance user experience. By reducing browsing time, the experiment aimed to improve decision-making efficiency for users while maintaining high satisfaction levels. Using a 2k factorial experimental design, we analyzed interaction plots and p-values to identify key factors affecting browsing duration, supplemented by Response Surface Methodology for informed decision-making.

---

## Key Features  

- **Factorial Design and Response Surface Methodology (RSM)**:  
  - Screening experiment using a 2k factorial design to identify the factors significantly influencing browsing duration.
    <img width="611" alt="Screenshot 2025-01-23 at 2 29 26 PM" src="https://github.com/user-attachments/assets/802dcb21-2f55-4880-8f0f-8fa0db54130e" />
  - Additional 3x3 factorial design to find the most efficient Match Score and Preview Length combination to minimize browsing time.  
  - Response Surface Methodology: The model employs Taylor’s Theorem to form a secondary model, considering the main effects, interaction effects, and quadratic effects of the two factors to approximate the minimum browsing time.
    <img width="629" alt="Screenshot 2025-01-23 at 2 30 05 PM" src="https://github.com/user-attachments/assets/59099d5f-54a6-4b90-9c56-3bf8ee358c35" />


- **A/B Testing**:  
  Validated the proposed improvements by comparing the redesigned homepage to the existing design, resulting in a 30% reduction in browsing time, with an average of 9.9 minutes.

---

## Results  

Optimal settings were determined to be a Preview Length of 75 seconds and a Match Score of 75%, alongside the default Preview Type 'TT' and Tile Size of 0.2. This configuration resulted in a marked decrease in browsing time, with an optimal average of 9.9 minutes.

---
