# MCJobOptimization

### Installation
In necessary Install python3
- https://www.python.org/downloads/

Navigate to %appdata%\.minecraft\saves\WORLDNAME\minecolonies\minecraft\overworld OR equivalent save folder in mod loader.
- Place the python script here

Open command prompt
- navigate to %appdata%\.minecraft\saves\WORLDNAME\minecolonies\minecraft\overworld OR equivalent save folder in mod loader.

    ```cd %appdata%\.minecraft\saves\WORLDNAME\minecolonies\minecraft\overworld ```
- run python script with the dat file (default is colony1.dat)

    ``` python3 MCWorkerOptimization.py ``` (runs on colony1.dat)
    
    ``` python3 MCWorkerOptimization.py colonyname.dat ```

### How to use
- Some buildings have multiple job roles that cannot all be filled. You must select what you want in your colony
  - For each mine you must select miner or quarrier
    - You will be prompted once for each mine you have. It does not matter which mine is which.
  - For each guard or barracks tower you must choose which type to fill with or leave the slot empty
    - IMPORTANT: You must plan this out beforehand. see the example below.

- After than you can rank any jobs you want to priorize such as a builder or a courier
  - If no ranking is provided then all jobs will be given the same priority
    - No ranking is techinically optimal but prioritize as you like.

### Issues
- Only one researcher will appear.
- Not tested on some buildings such as combat academy or late game buildings

### Example

#### My colony requirements
In my colony I have two guard towers with 1 knight and the other slot empty in each and two barracks towers, each with a knight and an archer, with the other slot empty.
I have two mines with, one with a miner and one with a quarrier.


#### Output
```All required modules are ready.
Warning - You did not provide a datafile as an argument, proceeding with default: colony1.dat. Command format python3 MCWorkerOptimization.py colonyfile.dat
Choose a job for the miner building (miner / quarrier): miner
Choose a job for 1 of 3 guards in the guardtower (knight / archer / druid / 0 (empty)): knight
Choose a job for 2 of 3 guards in the guardtower (knight / archer / druid / 0 (empty)): 0
Skipping... Remaining roles empty
Choose a job for 1 of 3 guards in the guardtower (knight / archer / druid / 0 (empty)): knight
Choose a job for 2 of 3 guards in the guardtower (knight / archer / druid / 0 (empty)): 0
Skipping... Remaining roles empty
Choose a job for the miner building (miner / quarrier): quarrier
Choose a job for 1 of 2 guards in the barrackstower (knight / archer / druid / 0 (empty)): knight
Choose a job for 2 of 2 guards in the barrackstower (knight / archer / druid / 0 (empty)): archer
Choose a job for 1 of 2 guards in the barrackstower (knight / archer / druid / 0 (empty)): knight
Choose a job for 2 of 2 guards in the barrackstower (knight / archer / druid / 0 (empty)): archer
1: Archer1
2: Archer2
3: Assistantcook1
4: Blacksmith1
5: Builder1
6: Builder2
7: Builder3
8: Carpenter1
9: Cook1
10: Courier1
11: Courier2
12: Courier3
13: Cowhand1
14: Farmer1
15: Fisher1
16: Forester1
17: Healer1
18: Knight1
19: Knight2
20: Knight3
21: Knight4
22: Librarystudent1
23: Miner1
24: Quarrier1
25: Researcher1
26: Smelter1
27: Stonemason1
28: Stonesmelter1
You have the option to rank some or all of the following jobs from highest to lowest importance. Input the job number followed by Enter. Start with the most important job. Enter 0 
to weight remaining roles equally.

Rank the next job (enter job number, p for current ranking or 0 to finish): 5

Rank the next job (enter job number, p for current ranking or 0 to finish): 10

Rank the next job (enter job number, p for current ranking or 0 to finish): 6

Rank the next job (enter job number, p for current ranking or 0 to finish): 11

Rank the next job (enter job number, p for current ranking or 0 to finish): 17

Rank the next job (enter job number, p for current ranking or 0 to finish): 25

Rank the next job (enter job number, p for current ranking or 0 to finish): p
Rank 1: Builder1
Rank 2: Courier1
Rank 3: Builder2
Rank 4: Courier2
Rank 5: Healer1
Rank 6: Researcher1

Rank the next job (enter job number, p for current ranking or 0 to finish): 16

Rank the next job (enter job number, p for current ranking or 0 to finish): p
Rank 1: Builder1
Rank 2: Courier1
Rank 3: Builder2
Rank 4: Courier2
Rank 5: Healer1
Rank 6: Researcher1
Rank 7: Forester1

Rank the next job (enter job number, p for current ranking or 0 to finish): 0

Thank you. The job rankings are as follows:
Rank 1: Builder1
Rank 2: Courier1
Rank 3: Builder2
Rank 4: Courier2
Rank 5: Healer1
Rank 6: Researcher1
Rank 7: Forester1
Rank 8: Archer1
Rank 8: Archer2
Rank 8: Assistantcook1
Rank 8: Blacksmith1
Rank 8: Builder3
Rank 8: Carpenter1
Rank 8: Cook1
Rank 8: Courier3
Rank 8: Cowhand1
Rank 8: Farmer1
Rank 8: Fisher1
Rank 8: Knight1
Rank 8: Knight2
Rank 8: Knight3
Rank 8: Knight4
Rank 8: Librarystudent1
Rank 8: Miner1
Rank 8: Quarrier1
Rank 8: Smelter1
Rank 8: Stonemason1
Rank 8: Stonesmelter1
Status: Optimal
Archer1 : Asuna Yuuki
Archer2 : Jaxson J. Goodenouth
Assistantcook1 : Bourey W. Grenefeld
Blacksmith1 : Otto U. Johnston
Builder1 : Byron V. Hambard
Builder2 : Queen L. Arnold
Builder3 : Dakota S. Glennon
Carpenter1 : Brennan M. Grafton
Cook1 : Flynn M. Coggshall
Courier1 : Humphrey Q. McDonald
Courier2 : Azariah A. Rao
Courier3 : Marcellus T. Annesley
Cowhand1 : Ariella E. Gorst
Farmer1 : Kylen I. Church
Fisher1 : Thatcher F. Greene
Forester1 : Genevieve J. Brown
Healer1 : Roman J. Basset
Knight1 : Conrad F. Glover
Knight3 : Jalen O. Ito
Knight4 : Zayn I. Ito
Miner1 : Jazlyn Z. Coffin
Quarrier1 : Gerardo L. Complin
Researcher1 : Chelsea S. Bell
Smelter1 : Reece R. Harris
Stonemason1 : Jazmine R. Cheverell```
Stonesmelter1 : Abraham E. Gorney
