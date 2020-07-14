import all

class ActorFallPacket(all, all.DataPacket):
	NETWORK_ID = ProtocolInfo.ACTOR_FALL_PACKET
	
	
	def decodePayload(self):
		self.entityRuntimeId = self.getEntityRuntimeId()
		self.fallDistance = self.getLFloat()
		self.isInVoid = self.getBool()
	
	
	def encodePayload(self):
		self.putEntityRuntimeId(self.entityRuntimeId)
		self.putLFloat(self.fallDistance)
		self.putBool(self.isInVoid)
	
	
	def handle(self, session: NetworkSession) -> bool:
		return session.handleActorFall(self)
