import all

class AddBehaviorTreePacket(all, all.DataPacket):
	NETWORK_ID = ProtocolInfo.ADD_BEHAVIOR_TREE_PACKET

	def decodePayload(self):
		self.behaviorTreeJson = self.getString()
	

	def encodePayload(self):
		self.putString(self.behaviorTreeJson)
	

	def handle(self, session : NetworkSession) -> bool:
		return session.handleAddBehaviorTree(self)

