import MetaTrader5 as mt5
 
# подключимся к MetaTrader 5
def initialize(login, password, server):
    if not mt5.initialize(login = login, password = password, server= server):
        print("initialize() failed")
        mt5.shutdown()
 
 
# завершим подключение к MetaTrader 5
#mt5.shutdown()
