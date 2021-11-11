
# Functions to complete:

## Get a list of uncompleted tasks
def get_uncompleted_tasks(list):
    # uncompleted_tasks = []
    # for task in list:
    #     if task["completed"] == False:
    #         uncompleted_tasks.append(task)
    # return uncompleted_tasks
    return get_tasks_by_status(list, False)

## Get a list of completed tasks
def get_completed_tasks(list):
    # completed_tasks = []
    # for task in list:
    #     if task["completed"] == True:
    #         completed_tasks.append(task)
    # return completed_tasks
    return get_tasks_by_status(list, True)

## Get tasks where time_taken is at least a given time
def get_tasks_taking_at_least(list, time):
    at_least_time = []
    for task in list:
        if task["time_taken"] >= time:
            at_least_time.append(task)
    return at_least_time

## Find a task with a given description
def get_task_with_description(list, description):
    for task in list:
        if task["description"] == description:
            return task
    return None   

# Extention (Function): 

## Get a list of tasks by status
def get_tasks_by_status(list, status):
    if status == False:
        uncompleted_tasks = []
        for task in list:
            if task["completed"] == False:
                uncompleted_tasks.append(task)
        return uncompleted_tasks
    else:
        completed_tasks = []
        for task in list:
            if task["completed"] == True:
                completed_tasks.append(task)
        return completed_tasks

def mark_task_complete(task):
    task["completed"] = True

def create_task(description, time_taken):
    task = {}
    task["description"] = description
    task["completed"] = False
    task["time_taken"] = time_taken

    return task

def add_to_list(list, task):
    list.append(task)

