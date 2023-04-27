import p60 as source
from p61 import make_model

source.game['room5']['toggle'] = source.toggle(1)

make_model(source.game, source.START_STATE)
