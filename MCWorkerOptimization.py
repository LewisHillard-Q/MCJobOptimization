import subprocess
import sys

# List of required modules
required_modules = ["nbtlib", "pulp"]

# Function to install a module using pip
def install_module(module_name):
    subprocess.check_call([sys.executable, "-m", "pip", "install", module_name])

# Check each module
for module in required_modules:
    try:
        # Try to import the module
        __import__(module)
    except ImportError:
        # If the module is not found, install it
        print(f"Installing {module} module...")
        install_module(module)

print("All required modules are ready.")

from nbtlib import File
import pulp

if len(sys.argv) < 2:
    print("Warning - You did not provide a datafile as an argument, proceeding with default: colony1.dat. Command format python3 MCWorkerOptimization.py colonyfile.dat")
    filename = "colony1.dat"
else:
    filename = sys.argv[1]

try:
    nbt_file = File.load(filename, gzipped=False)
except:
    print("Failed to load file, make sure a .dat file was provided or the script is in .minecraft\saves\YOURWORLD\minecolonies\minecraft\overworld")


skillDict = {
    0: 'Athletics',
    1: 'Dexterity',
    2: 'Strength',
    3: 'Agility',
    4: 'Stamina',
    5: 'Mana',
    6: 'Adaptability',
    7: 'Focus',
    8: 'Creativity',
    9: 'Knowledge',
    10: 'Intellegence'
}

jobs_dict = {
    'Alchemist': ['Dexterity', 'Mana'],
    'Archer': ['Agility', 'Adaptability'],
    'AssistantCook': ['Creativity', 'Knowledge'],
    'Baker': ['Knowledge', 'Dexterity'],
    'Beekeeper': ['Dexterity', 'Adaptability'],
    'Blacksmith': ['Strength', 'Focus'],
    'Builder': ['Adaptability', 'Athletics'],
    'Carpenter': ['Knowledge', 'Dexterity'],
    'ChickenFarmer': ['Adaptability', 'Agility'],
    'Composter': ['Stamina', 'Athletics'],
    'ConcreteMixer': ['Stamina', 'Dexterity'],
    'Cook': ['Adaptability', 'Knowledge'],
    'Courier': ['Agility', 'Adaptability'],
    'Cowhand': ['Athletics', 'Stamina'],
    'Crusher': ['Stamina', 'Strength'],
    'Druid': ['Mana', 'Focus'],
    'Dyer': ['Creativity', 'Dexterity'],
    'Enchanter': ['Mana', 'Knowledge'],
    'Farmer': ['Stamina', 'Athletics'],
    'Fisher': ['Focus', 'Agility'],
    'Fletcher': ['Dexterity', 'Creativity'],
    'Florist': ['Dexterity', 'Agility'],
    'Forester': ['Strength', 'Focus'],
    'Glassblower': ['Creativity', 'Focus'],
    'Healer': ['Mana', 'Knowledge'],
    'Knight': ['Adaptability', 'Stamina'],
    #'LibraryStudent': ['Intelligence', 'None'],
    'Mechanic': ['Knowledge', 'Agility'],
    'Miner': ['Strength', 'Stamina'],
    'NetherMiner': ['Adaptability', 'Strength'],
    'Planter': ['Agility', 'Dexterity'],
    'Pupil': ['Intelligence & Knowledge', 'Mana'],
    'Quarrier': ['Strength', 'Stamina'],
    'RabbitHerder': ['Agility', 'Athletics'],
    'Shepherd': ['Focus', 'Strength'],
    'Sifter': ['Focus', 'Strength'],
    'Smelter': ['Athletics', 'Strength'],
    'Stonemason': ['Creativity', 'Dexterity'],
    'StoneSmelter': ['Athletics', 'Dexterity'],
    'Swineherd': ['Strength', 'Athletics'],
    'Teacher': ['Knowledge', 'Mana'],
    'Undertaker': ['Strength', 'Mana'],
    'Researcher': ['Knowledge', 'Mana']
}


job_type_mapping = {
    'Cookassistant': 'AssistantCook',
    'Fisherman': 'Fisher',
    'Lumberjack': 'Forester',
    'Deliveryman': 'Courier',
    'Sawmill': 'Carpenter',
    'Student': 'LibraryStudent',
    'Ranger': 'Archer',
    'Stonesmeltery': 'StoneSmelter',
    'Cowboy': 'Cowhand',
    'ChickenHerder': 'ChickenFarmer',
    'NetherWorker': 'NetherMiner',
    'Research': 'Researcher'
}


from collections import defaultdict

jobs = {}
job_counter = defaultdict(int)


for building in nbt_file['buildingManager']['buildings']:
    skipFlag=0
    #print("next building")
    for key in building.keys():
        if 'minecolonies:' in key:
            job_type = key.split(':')[1].capitalize()  # Get the job type, which comes after 'minecolonies:'
            if job_type not in jobs_dict:
                # If the job_type does not exist in jobs_dict, use the mapping
                job_type = job_type_mapping.get(job_type, job_type)

            if building['type'].split(':')[1] == 'miner':
                skipFlag=1
                # If the building is a miner, prompt the user to pick between miner and quarrier
                user_choice = input("Choose a job for the miner building (miner / quarrier): ").capitalize()
                if user_choice in jobs_dict:
                    job_type = user_choice
                    
                else:
                    print(f"Invalid choice '{user_choice}'. Skipping...")
                
                job_counter[job_type] += 1
                job_name = f"{job_type.capitalize()}{job_counter[job_type]}"  # Create a unique job name

                if job_type in jobs_dict:
                    # For other types of buildings, assign the job directly from jobs_dict
                    primary_skill, secondary_skill = jobs_dict[job_type]
                    jobs[job_name] = [primary_skill, secondary_skill]
                    break
                else:
                    print(f"Warning: Job type '{job_type}' not found in jobs_dict!")
                    break

            elif building['type'].split(':')[1] in ['barrackstower', 'guardtower']:
                # If the job_type is a tower, prompt the user to assign jobs based on the building level
                for level in range(building['level']):
                    if level+1 == int(building['level']):
                        skipFlag=1
                    
                    user_choice = input(f"Choose a job for {level + 1} of {int(building['level'])} guards in the {building['type'].split(':')[1] } (knight / archer / druid / 0 (empty)): ").capitalize()
                    if user_choice in jobs_dict:
                        job_type = user_choice
                    elif user_choice == str(0):
                        skipFlag=1
                        print("Skipping... Remaining roles empty")
                        break
                    else:
                        print(f"Invalid choice '{user_choice}'. Skipping...")
                        break
                    
                    job_counter[job_type] += 1
                    job_name = f"{job_type.capitalize()}{job_counter[job_type]}"  # Create a unique job name

                    if job_type in jobs_dict:
                        # For other types of buildings, assign the job directly from jobs_dict
                        primary_skill, secondary_skill = jobs_dict[job_type]
                        jobs[job_name] = [primary_skill, secondary_skill]
                        if skipFlag==1:
                            break
                    else:
                        skipFlag=1
                        print(f"Warning: Job type '{job_type}' not found in jobs_dict!")
                        break
            else:
                job_counter[job_type] += 1
                job_name = f"{job_type.capitalize()}{job_counter[job_type]}"  # Create a unique job name

                if job_type in jobs_dict:
                    # For other types of buildings, assign the job directly from jobs_dict
                    primary_skill, secondary_skill = jobs_dict[job_type]
                    jobs[job_name] = [primary_skill, secondary_skill]
                    if skipFlag==1:
                        break
                else:
                    #print(f"Warning: Job type '{job_type}' not found in jobs_dict!")
                    break
              

        if skipFlag==1:
            break
        

jobs = dict(sorted(jobs.items()))

# Create a list of all jobs
all_jobs = list(jobs.keys())

# Store the user's rankings here
job_rankings = {}

for i, job in enumerate(all_jobs, start=1):
    print(f"{i}: {job}")

print("You have the option to rank some or all of the following jobs from highest to lowest importance. Input the job number followed by Enter. Start with the most important job. Enter 0 to weight remaining roles equally.")

equal_rank_value = None

while True:
    #if equal_rank_value is not None:
    #    # If the user has previously entered '0', assign the remaining jobs equal rank
    #    job_rankings[job] = equal_rank_value
    #else:
    job_num = input("\nRank the next job (enter job number, p for current ranking, or 0 to finish): ")
    if job_num=='p':
        for job, rank in job_rankings.items():
            print(f"Rank {rank}: {job}")
        continue

    job_num = int(job_num)-1
    if job_num == -1:
        # The user entered '0'. Assign the remaining jobs equal rank
        equal_rank_value = len(job_rankings) + 1
        break 
    elif job_num not in range(len(all_jobs)):
        print("Invalid job number, please try again.")
        continue
    elif all_jobs[job_num] in job_rankings.values():
        print("This job has already been ranked, please try again.")
        continue
    else:
        rank = len(job_rankings) + 1
        job_rankings[all_jobs[job_num]] = rank
    #endelse

for i, job in enumerate(all_jobs, start=1):
    if job in job_rankings:
        #print("skipping")
        continue
    else:
        job_rankings[job] = equal_rank_value

print("\nThank you. The job rankings are as follows:")
for job, rank in job_rankings.items():
    print(f"Rank {rank}: {job}")

# Create job_weights from job_rankings

job_weights = {job: max(job_rankings.values()) - rank + 1 for job, rank in job_rankings.items()}


citizens = {}

for citizen in nbt_file['citizenManager']['citizens']:
    citizen_name = str(citizen['name'])
    #print(citizen_name)
    citizen_skills = {}
    for skill in citizen['newSkills']['levelMap']:
        skillID = skill['skill']  # integer that must mapped to skill name
        skillLevel = skill['level']
        skillName = skillDict[skillID]  # map the skill ID to its name
        citizen_skills[skillName] = int(skillLevel)  # assign the level to the skill name
    citizens[citizen_name] = citizen_skills  # assign the skills dictionary to the citizen

# Now the 'citizens' dictionary contains each citizen's skills
#print(citizens)


# Define the problem
prob = pulp.LpProblem("WorkerAssignmentProblem", pulp.LpMaximize)

# Create a binary variable to state that a job is assigned to a worker or not
x = pulp.LpVariable.dicts("jobs", [(i, j) for i in jobs for j in citizens], cat='Binary')

# Objective function

prob += pulp.lpSum([x[(i, j)] * job_weights[i] * 
                (citizens[j].get(jobs[i][0], 0) + citizens[j].get(jobs[i][1], 0)) 
                    for i in jobs for j in citizens])

# Constraints
for i in jobs:
    prob += pulp.lpSum([x[(i, j)] for j in citizens]) <= 1  # Each job can be assigned at most once

for j in citizens:
    prob += pulp.lpSum([x[(i, j)] for i in jobs]) <= 1  # Each worker can be assigned at most one job

# Solve the problem
prob.solve(pulp.PULP_CBC_CMD(msg=0))

# Print the results
print("Status:", pulp.LpStatus[prob.status])
for v in prob.variables():
    if v.varValue > 0:
        job_and_name = v.name.split("_", 2)  # Split the string into two parts
        job = job_and_name[1].replace("('", '').replace("',",'')  # Extract the job
        name = job_and_name[2].replace('_', ' ').replace("'",'').replace(")",'')  # Extract the name and replace underscores with spaces

        print(f"{job} : {name}")


#print("Total skills utilized = ", pulp.value(prob.objective))