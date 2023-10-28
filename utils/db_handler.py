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

class TaskDone:
    def __init__(self, session):
        self.session = session

    def mark_done(self, title):
        title = title
        done = session.query(Tasks).filter(Tasks.title==title).first()
        if done : 
            done.is_done_id = 2
            self.session.commit()
            self.session.close()
            print('congrats, you did your task.')
        else: 
            print('Task not found')




if __name__ == '__main__':
    
    # task = AddTask(session)
    # task.add_task('Trash', 'Take out the trash')
    # task.add_task('Dishes', 'Wash the dishes', 2)

    done = TaskDone(session)
    done.mark_done('Trash')

