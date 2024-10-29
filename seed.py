from models import Pet, db 
from app import app 

db.drop_all()
db.create_all()

brighton = Pet(name='Brighton Rigsby', species='Dog', age='10', note='not great with kids. not great with dogs' )

clarissa = Pet(name="Clarissa", species='Cow', age='3', note='shes a good girl')

captain_holt = Pet(name='Captain Holt', species='Falcon', note='please watch your fingers')

db.session.add_all([brighton, clarissa, captain_holt])
db.session.commit()

