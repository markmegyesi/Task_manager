from sqlalchemy import create_engine, Column,String,Integer,Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from db_url import DB_URL

engine=create_engine(DB_URL)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Tasks(Base):
    __tablename__='tasks'
    id = Column(Integer, primary_key = True)
    title = Column (Text)
    description = Column(Text)
    is_done_id = Column(Text)


class GetTaskByName:
    def __init__(self, session):
        self.session = session
    
    def get_task(self, title):
        title = title
        task = session.query(Tasks).filter(Tasks.title==title).first()
        return task


class AddTask:
    def __init__(self, session):
        self.session = session

    def add_task(self, title, description, is_done_id = None):
        if is_done_id != None:
            new_task=Tasks(title=title, description=description, is_done_id=is_done_id)
            
        else:
            new_task=Tasks(title=title, description=description, is_done_id = 1)
        self.session.add(new_task)
        self.session.commit()
        self.session.close()

class TaskDone(GetTaskByName):
    def __init__(self, session):
        super().__init__(session)

    def mark_done(self, title):
        done = self.get_task(title)
        if done : 
            done.is_done_id = 2
            self.session.commit()
            self.session.close()
            print('Congrats, you did your task.')
        else: 
            print(f"Task with title '{title}' not found.")

class ModifyTask(GetTaskByName):
    def __init__(self):
        super().__init__(session)
        
    
    def modify(self,title, new_title = None, new_description = None, is_done_id = None):
        task = self.get_task(title)
        if task:
            if new_title != None:
                task.title = new_title
            if new_description != None:
                task.description = new_description
            if is_done_id != None:
                task.is_done_id = is_done_id
            self.session.commit()
            self.session.close()
            print('You succesfully updated your task.')
        else:
            print(f"Task with title '{title}' not found.")


if __name__ == '__main__':
    
    # task = AddTask(session)
    # task.add_task('Trash', 'Take out the trash')
    # task.add_task('Dishes', 'Wash the dishes', 2)

    done = ModifyTask(session)
    done.modify('Trash', new_title= "Trash!", new_description='You should take out the trash.')

