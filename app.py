from argparse import ArgumentParser
import json
from datetime import datetime

db = {}

def persist_db():
    with open('db.json', 'w') as dbf:
        json.dump(db, dbf)

def read_db():
    global db, meta_data
    try:
        with open('db.json', 'r') as f:
            db = json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        pass

def get_next_id():
    next_id = len(db)+1
    keys = list(db.keys())
    keys.sort()
    for i in range(len(keys)):
        if i+1!=int(keys[i]):
            return i+1
    return next_id

def create(args):
    id = get_next_id()
    db[id] = {
        'id':id,
        'description': args.task_description,
        'created_at': str(datetime.now()),
        'updated_at': str(datetime.now()),
        'status': 'ToDo' 
    }
    persist_db()
    print(f"Successfully created the task with id - {id} ")

def update(args):
    db[args.id]['status'] = args.status
    db[args.id]['updated_at'] = str(datetime.now())
    persist_db()
    print(f"Successfully updated the status of the task {args.id} to {args.status}")

def delete(args):
    if db.get(args.id, None) == None:
        print(f"Task with id {args.id} does not exist")
    else:
        db.pop(args.id)
        persist_db()
        print(f"Successfully deleted the task with id {args.id}")

def list_task(args):
    
    if args.status==None:
        filtered_db = db
    else:
        filtered_db = {}
        for k in db:
            if db[k]['status'] == args.status:
                filtered_db[k]=db[k]
    print("="*150)
    print("{:^4} {:^60} {:^10} {:^40} {:^40}".format('Id', 'Description', 'Status', 'Last Status Updated At', 'Created At') )
    print("="*150)

    for k in filtered_db:
        print("{:^4} {:^60} {:^10} {:^40} {:^10}".format(db[k]['id'], db[k]['description'], db[k]['status'], db[k]['updated_at'], db[k]['created_at']) )
        print("-"*150)

def main():

    read_db()

    parser = ArgumentParser(
        prog='taskd',
        description = "A program used to track and manage the tasks"
    )

    parser.add_argument('-s', '--status', help=" Status filter", choices=['Done', 'ToDo', 'In Progress'])
    parser.set_defaults(func=list_task)

    subparsers = parser.add_subparsers(help="Operations on task", dest='subparser_name')

    create_parser = subparsers.add_parser('add', help="Add task")
    create_parser.add_argument('task_description', help="Add the name and description of task")
    create_parser.set_defaults(func=create)

    update_parser = subparsers.add_parser('update', help="Update status of the task")
    update_parser.add_argument('id', help="Id of the task to be updated")
    update_parser.add_argument('status', help="New status of task", choices=['Done', 'ToDo', 'In Progress'])
    update_parser.set_defaults(func=update)

    delete_parser = subparsers.add_parser('delete', help="delete the task")
    delete_parser.add_argument('id', help="Id of the task to be deleted")
    delete_parser.set_defaults(func=delete)

    args = parser.parse_args()
    args.func(args)

if __name__=='__main__':
    main()