import netsnmp, threading, time

class Mon:

	router = '10.0.0.1'
	interface = 'ppp0'

	def __init__(self):
		Interfaces = netsnmp.snmpwalk('ifDescr',Version=2,DestHost=self.router,Community='public')
		self.index = Interfaces.index(self.interface)

	def get_in(self):
		In = netsnmp.snmpwalk('ifInOctets',Version=2,DestHost=self.router,Community='public')
		return In

	def get_out(self):
		Out = netsnmp.snmpwalk('ifOutOctets',Version=2,DestHost=self.router,Community='public')
		return Out

	def run(self):
		print self.get_in()[self.index]
		print self.get_out()[self.index]

	def main(self):
		threading.Thread(target=self.run,name=time.time()).start()

if __name__ == '__main__':
	mon = Mon()
	mon.run()